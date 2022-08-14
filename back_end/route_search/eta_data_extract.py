import asyncio
from asyncio.windows_events import NULL
import aiohttp
from urllib.parse import urlparse, parse_qs
import json

import route_search.route_network as rn

import platform
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


# TYPE 1: Sub-Routine Functions
async def gather_with_concurrency(n, *tasks):

    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
             return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def hr_get_async(url, session, results):

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


# TYPE 2: Application Functions
# eta_raw_extract: Extract eta information with data cleaning
async def eta_raw_extract(station_id_list):

    # STEP 1: Initialise api urls
    hr_urls = []
    lr_urls = []

    for item in station_id_list:

        if (len(item) > 4):
            hr_urls.append(f"https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line={item[:3]}&sta={item[-3:]}")
        
        elif (len(item) <= 3):
            lr_urls.append(f"https://rt.data.gov.hk/v1/transport/mtr/lrt/getSchedule?station_id={item}")


    # STEP 2: Gather data
    hr_results = {}
    lr_results = {}
    conc_req = 40

    conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    session = aiohttp.ClientSession(connector=conn)

    await gather_with_concurrency(conc_req, *[hr_get_async(i, session, hr_results) for i in hr_urls])
    await gather_with_concurrency(conc_req, *[lr_get_async(i, session, lr_results) for i in lr_urls])

    results = {
        'hr': hr_results,
        'lr': lr_results
    }

    await session.close()

    return results


# hr_eta_clean_extract: Extract eta information with data cleaning
def hr_eta_clean_extract(hr_eta_raw, station_id, platform_list):

    # Extract required eta data
    eta_clean = []
    first_wait_time = 0
    last_wait_time = 0
    avg_wait_time = 0

    if ('data' in hr_eta_raw.keys()):
        for key_1, value_1 in hr_eta_raw['data'][station_id].items():
            if (key_1 == 'UP') or (key_1 == 'DOWN'):

                for item in value_1:
                    if item['plat'] in platform_list['platform']:

                        # Insert data
                        data = {}

                        if platform_list['route'][0] == 'TML':
                            data['route_no'] = '屯馬線'
                        else:
                            data['route_no'] = '東涌線'

                        data['dest_station'] = rn.station_name_find(item['dest'])['station_name']
                        data['platform_id'] = item['plat']
                        data['ttnt_eta'] = int(item['ttnt'])

                        if (len(eta_clean) < 4):
                            eta_clean.append(data)

                            # Gather waiting time statistics
                            first_wait_time = data['ttnt_eta'] if (item['seq'] == '1') else first_wait_time
                            last_wait_time = data['ttnt_eta'] if (data['ttnt_eta'] > last_wait_time) else last_wait_time

        eta_clean_len = len(eta_clean) if (len(eta_clean) > 0) else 1
        avg_wait_time = ((last_wait_time - first_wait_time) / (eta_clean_len - 1)) if (eta_clean_len > 1) else first_wait_time
        avg_wait_time = round(avg_wait_time)

    # Pack required eta data
    eta_clean = sorted(eta_clean, key=lambda d: d['ttnt_eta']) 

    result = {
        'eta_list': eta_clean,
        'first_wait_time': first_wait_time,
        'avg_wait_time': avg_wait_time
    }

    return result
        

# lr_eta_clean_extract: Extract eta information with data cleaning
def lr_eta_clean_extract(lr_eta_raw, station_id, platform_list):

    # Extract required eta data
    eta_clean = []
    first_wait_time = 100
    last_wait_time = 0
    avg_wait_time = 0

    if ('platform_list' in lr_eta_raw.keys()):

        # Loop through selected routes and platform
        for i in range(len(platform_list['route'])):
            
            curr_route_no = platform_list['route'][i]
            curr_platform = platform_list['platform'][i]

            # Loop through data to search the target route and platform
            for item_1 in lr_eta_raw['platform_list']:

                if (int(item_1['platform_id']) == int(curr_platform)) & ('route_list' in item_1):
                    if (item_1['route_list']):

                        for item_2 in item_1['route_list']:

                            if item_2['route_no'] == curr_route_no:

                                # Insert data
                                data = {}
                                data['route_no'] = item_2['route_no']
                                data['dest_station'] = item_2['dest_ch']
                                data['platform_id'] = item_1['platform_id']

                                if (item_2['time_en'] in ['Arriving', 'Departing', '-']):
                                    data['ttnt_eta'] = 0
                                else:
                                    data['ttnt_eta'] = int(item_2['time_en'].split()[0])

                                if (len(eta_clean) < 4):
                                    eta_clean.append(data)

                                    # Gather waiting time statistics
                                    first_wait_time = data['ttnt_eta'] if ((data['ttnt_eta'] < first_wait_time) or (len(eta_clean) == 1)) else first_wait_time
                                    last_wait_time = data['ttnt_eta'] if (data['ttnt_eta'] > last_wait_time) else last_wait_time

        eta_clean_len = len(eta_clean) if (len(eta_clean) > 0) else 1

        print(first_wait_time)
        print(last_wait_time)
        print(eta_clean_len)

        avg_wait_time = ((last_wait_time - first_wait_time) / (eta_clean_len - 1)) if (eta_clean_len > 1) else first_wait_time
        avg_wait_time = round(avg_wait_time)

    # Pack required eta data
    eta_clean = sorted(eta_clean, key=lambda d: d['ttnt_eta']) 

    result = {
        'eta_list': eta_clean,
        'first_wait_time': first_wait_time,
        'avg_wait_time': avg_wait_time
    }

    return result