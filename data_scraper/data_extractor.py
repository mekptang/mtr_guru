import psycopg2
import config
from psycopg2.pool import ThreadedConnectionPool
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp
import time
from urllib.parse import urlparse
from urllib.parse import parse_qs
from db_create_table import create_tables
import json
import logging

logging.basicConfig(filemode="w",format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",level=logging.INFO)

try:
    postgreSQL_pool = ThreadedConnectionPool(2, 60, **config.conn_str)

    def is_MTR_Base_Record_Exist(postgreSQL_pool, curr_time, sys_time, station):
        conn = postgreSQL_pool.getconn()
        c = conn.cursor()
        c.execute(f"SELECT \"base_id\" FROM base_data WHERE curr_time='{curr_time}' AND sys_time='{sys_time}' AND station='{station}'")
        result = c.fetchone() is not None
        postgreSQL_pool.putconn(conn)
        return result

    def is_LR_Base_Record_Exist(postgreSQL_pool, sys_time, station_id):
        conn = postgreSQL_pool.getconn()
        c = conn.cursor()
        c.execute(f"SELECT \"lr_data_id\" FROM lr_base_data WHERE sys_time='{sys_time}' AND station_id='{station_id}'")
        result = c.fetchone() is not None
        postgreSQL_pool.putconn(conn)
        return result

    def MTR_insert_data( postgreSQL_pool, **data):
        if "up" in data or "down" in data:
            conn = postgreSQL_pool.getconn()
            c = conn.cursor()
            base_data_insert = \
                f"""
                INSERT INTO base_data(
                    curr_time, sys_time, isdelay, station, status, message
                    ) VALUES (
                        '{data['curr_time']}',
                        '{data['sys_time']}',
                        '{str(data['isdelay']).lower()}',
                        '{data['station']}',
                        '{data['status']}',
                        '{data['message']}'
                    ) RETURNING base_id;
                """   

            c.execute(base_data_insert)
            uuid = c.fetchone()[0]
            if "up" in data:
                for up in data["up"]:
                    up_data_insert = \
                        f"""
                        INSERT INTO up_data(
                            base_id, ttnt, valid, plat, time, source, dest, seq
                            ) VALUES (
                                '{uuid}',
                                '{up['ttnt']}',
                                '{str(up['valid']).lower()}',
                                '{up['plat']}',
                                '{up['time']}',
                                '{up['source']}',
                                '{up['dest']}',
                                '{up['seq']}'
                            )
                        """
                    c.execute(up_data_insert)

            if "down" in data:
                for dw in data["down"]:
                    down_data_insert = \
                        f"""
                        INSERT INTO down_data(
                            base_id, ttnt, valid, plat, time, source, dest, seq
                            ) VALUES (
                                '{uuid}',
                                '{dw['ttnt']}',
                                '{str(dw['valid']).lower()}',
                                '{dw['plat']}',
                                '{dw['time']}',
                                '{dw['source']}',
                                '{dw['dest']}',
                                '{dw['seq']}'
                            )
                        """
                    c.execute(down_data_insert)
            conn.commit()
            postgreSQL_pool.putconn(conn)
            return uuid
        else:
            return "Out of Service"

    def LR_insert_data(postgreSQL_pool, **data):
        if "routes_list" in data:
            # print("LR_insert_data")
            # print(data)
            conn = postgreSQL_pool.getconn()
            c = conn.cursor()
            lr_base_data_insert = \
                f"""
                INSERT INTO lr_base_data(
                    sys_time, status, station_id
                    ) VALUES (
                        '{data['sys_time']}',
                        '{data['status']}',
                        '{data['station_id']}'
                    ) RETURNING lr_data_id;
                """   
            c.execute(lr_base_data_insert)
            uuid = c.fetchone()[0]
            for route in data["routes_list"]:
                route_insert = \
                        f"""
                        INSERT INTO lr_route_list(
                            lr_data_id, platform_id, train_length, arrival_departure, dest_en, time_en, route_no, stop
                            ) VALUES (
                                '{uuid}',
                                '{route['platform_id']}',
                                '{route['train_length']}',
                                '{route['arrival_departure']}',
                                '{route['dest_en']}',
                                '{route['time_en']}',
                                '{route['route_no']}',
                                '{route['stop']}'
                            )
                        """
                c.execute(route_insert)
            conn.commit()
            postgreSQL_pool.putconn(conn)
            return uuid
        else:
            return "Out of Service"

    async def gather_with_concurrency(n, *tasks):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(task):
            async with semaphore:
                return await task

        return await asyncio.gather(*(sem_task(task) for task in tasks))

    async def mtr_get_async(url, session, results):
        async with session.get(url) as response:
            if (response.status == 200):
                parsed_url = urlparse(url)
                line = parse_qs(parsed_url.query)['line'][0]
                sta = parse_qs(parsed_url.query)['sta'][0]
                obj = await response.text()
                results[f"{line}-{sta}"] = json.loads(obj)
            if (response.status == 429):
                print("Too many requests!")
            if (response.status == 500):
                print("Internal Server Error!")
    
    async def lr_get_async(url, session, results):
        async with session.get(url) as response:
            if (response.status == 200):
                parsed_url = urlparse(url)
                sta_id = parse_qs(parsed_url.query)['station_id'][0]
                obj = await response.text()
                results[sta_id] = json.loads(obj)
            if (response.status == 429):
                print("Too many requests!")
            if (response.status == 500):
                print("Internal Server Error!")

    async def main():
        create_tables()
        md = config.mtr_dict
        ld = config.lr_dict
        mtr_urls = []
        lr_urls = []

        # Initialise api urls
        for k, v in md.items():
            for i in v:
                mtr_urls.append(f"https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line={k}&sta={i}")
        
        for k in ld.keys():
            lr_urls.append(f"https://rt.data.gov.hk/v1/transport/mtr/lrt/getSchedule?station_id={k}")

        while(True):
            try:
                conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
                session = aiohttp.ClientSession(connector=conn)
                MTR_results = {}
                LR_result = {}
                MTR_tf_results = []
                LR_tf_results = []
                conc_req = 40
                now = time.time()
                await gather_with_concurrency(conc_req, *[mtr_get_async(i, session, MTR_results) for i in mtr_urls])
                await gather_with_concurrency(conc_req, *[lr_get_async(i, session, LR_result) for i in lr_urls])
                time_taken = time.time() - now

                for key in MTR_results.keys():
                    data = {}
                    data["station"] = key
                    data["curr_time"] = MTR_results[key]["curr_time"]
                    data["sys_time"] = MTR_results[key]["sys_time"]
                    data["isdelay"] = MTR_results[key]["isdelay"]
                    data["status"] = MTR_results[key]["status"]
                    data["message"] = MTR_results[key]["message"]
                    if 'UP' in MTR_results[key]['data'][key]:
                        data["up"] = MTR_results[key]['data'][key]["UP"]
                    if 'DOWN' in MTR_results[key]['data'][key]:
                        data["down"] = MTR_results[key]['data'][key]["DOWN"]
                    MTR_tf_results.append(data)

                for key, value in LR_result.items():
                    data = {}
                    routes_list = []
                    if "platform_list" in value:
                        for i in value["platform_list"]:
                            if "route_list" in i:
                                for j in i["route_list"]:
                                    route = {}
                                    route["platform_id"] = i["platform_id"]
                                    route["train_length"] = j["train_length"]
                                    route["arrival_departure"] = j["arrival_departure"]
                                    route["dest_en"] = j["dest_en"]
                                    route["time_en"] = j["time_en"]
                                    route["route_no"] = j["route_no"]
                                    route["stop"] = j["stop"]
                                    routes_list.append(route)
                                data["routes_list"] = routes_list
                    data["status"] = value["status"]
                    data["sys_time"] = value["system_time"]
                    data["station_id"] = key
                    LR_tf_results.append(data)
                # print(LR_tf_results[0])

                with ThreadPoolExecutor(max_workers=40) as pool:
                    MTR_results = [ "Records Exists" if pool.submit(is_MTR_Base_Record_Exist, postgreSQL_pool, i["curr_time"], i["sys_time"], i["station"]).result() \
                        else pool.submit(MTR_insert_data, postgreSQL_pool, **i).result() \
                            for i in MTR_tf_results ]
                    LR_result = ["Records Exists" if pool.submit(is_LR_Base_Record_Exist, postgreSQL_pool, i["sys_time"], i["station_id"]).result() else pool.submit(LR_insert_data, postgreSQL_pool, **i).result() for i in LR_tf_results ]
                    logging.info(LR_result)
                    logging.info(MTR_results)

                logging.info(time_taken)
                await asyncio.sleep(config.poll_interval)
            except Exception as e:
                logging.error(e)
            finally:
                await session.close()
                if postgreSQL_pool:
                    postgreSQL_pool.closeall

    asyncio.run(main())
    
except (Exception, psycopg2.DatabaseError) as error:
    logging.error(error)
finally:
    if postgreSQL_pool:
        postgreSQL_pool.closeall
    logging.info("PostgreSQL connection pool is closed")
