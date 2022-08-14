import psycopg2
import config
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        # """
        # SET timezone to '+8'
        # """,
        """
        CREATE TABLE IF NOT EXISTS base_data (
            base_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            ts TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
            curr_time TIMESTAMP NOT NULL,
            sys_time TIMESTAMP NOT NULL,
            isdelay BOOLEAN NOT NULL,
            station VARCHAR(20) NOT NULL,
            status INTEGER NOT NULL,
            message VARCHAR(20) NOT NULL
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS up_data (
            up_id SERIAL PRIMARY KEY,
            base_id UUID,
            ttnt INTEGER NOT NULL,
            valid BOOLEAN NOT NULL,
            plat VARCHAR(20) NOT NULL,
            time TIMESTAMP NOT NULL,
            source VARCHAR(20) NOT NULL,
            dest VARCHAR(20) NOT NULL,
            seq VARCHAR(20) NOT NULL,
            CONSTRAINT fk_base_data
                FOREIGN KEY (base_id)
                    REFERENCES base_data (base_id)
            )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS down_data (
            down_id SERIAL PRIMARY KEY,
            base_id UUID,
            ttnt INTEGER NOT NULL,
            valid BOOLEAN NOT NULL,
            plat VARCHAR(20) NOT NULL,
            time timestamp NOT NULL,
            source VARCHAR(20) NOT NULL,
            dest VARCHAR(20) NOT NULL,
            seq VARCHAR(20) NOT NULL,
            CONSTRAINT fk_base_data
                FOREIGN KEY (base_id)
                    REFERENCES base_data (base_id)
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS lr_base_data (
            lr_data_id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            ts TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
            sys_time TIMESTAMP NOT NULL,
            status INTEGER NOT NULL,
            station_id VARCHAR(10) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS lr_route_list (
            route_list_id SERIAL PRIMARY KEY,
            lr_data_id UUID,
            platform_id INTEGER NOT NULL,
            train_length INTEGER NOT NULL,
            arrival_departure VARCHAR(5) NOT NULL,
            dest_en VARCHAR(20) NOT NULL,
            time_en VARCHAR(20) NOT NULL,
            route_no VARCHAR(20) NOT NULL,
            stop INTEGER NOT NULL,
            CONSTRAINT fk_lr_base_data
                FOREIGN KEY (lr_data_id)
                    REFERENCES lr_base_data (lr_data_id)
            )
        """)

    conn = None

    try:
        # read the connection parameters
        params = config.conn_str
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()