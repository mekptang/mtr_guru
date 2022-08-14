import pandas.io.sql as sqlio
import history_search.db_connection as db
import connectorx as cx

import pandas as pd
from IPython.display import display

import history_search.data_analysis as da


### Type 1: Data Extraction ###
# raw_hr_1_extract: Extract train waiting time data of single station
def raw_hr_1_extract(query):

    connection = db.connect()

    sql_hr_1 = '''Select base_data.curr_time, base_data.station, {1}_data.dest, {1}_data.ttnt as ttnt_eta from {1}_data, base_data
                        where {1}_data.base_id = base_data.base_id
                            and base_data.station = '{0}'
                            and base_data.curr_time >= '{2}'
                            and base_data.curr_time < '{3}'
                            and {1}_data.seq = '1'
                        order by base_data.curr_time asc;'''.format(query['start_station_id'], query['direction'], query['start_time'], query['end_time'])

    result = sqlio.read_sql_query(sql_hr_1, connection)

    return(result)


### Type 2: Data Cleaning + Append ###
# df_hr_base_append: Conduct basic data cleaning + data append
def df_hr_base_append(df_hr):

    # Fix the formatting of data columns
    df_hr = df_hr.rename(columns={
                            'curr_time': 'curr_time',
                            'station': 'curr_station_id',
                            'dest': 'dest_station_id',
                            'ttnt': 'ttnt_eta'})

    df_hr = df_hr.astype({
                    'curr_time': 'datetime64[ns]', 
                    'curr_station_id': 'str',
                    'dest_station_id': 'str', 
                    'ttnt_eta': 'int'})

    # Append Train Characteristics
    df_hr['route_no'] = df_hr['curr_station_id'].str[:3]
    df_hr['train_len'] = 8
    df_hr['curr_station_id'] = df_hr['curr_station_id'].str[-3:]

    df_hr = df_hr.reindex(columns=['curr_time', 'route_no', 'train_len', 'curr_station_id', 'dest_station_id', 'ttnt_eta'])

    return df_hr


# df_hr_1_create: Train waiting time/Train arrival information production
def df_hr_1_create(query, column_flag):

    # Step 1 - Extract the data
    df_hr_1 = raw_hr_1_extract(query)

    # Step 2 - Conduct data cleaning + data analysis
    # Append basic information
    df_hr_1 = df_hr_base_append(df_hr_1)

    # Append time information
    if column_flag['ttnt_eta'] == 1:
        df_hr_1 = da.ttnt_eta_cal(df_hr_1)

    if column_flag['ttnt_real'] == 1:
        df_hr_1 = da.ttnt_real_cal_1(df_hr_1)

    if column_flag['ttnt_eta_delay'] == 1:
        df_hr_1 = da.ttnt_eta_delay_cal(df_hr_1)

    if column_flag['ttnt_real_delay'] == 1:
        df_hr_1 = da.ttnt_real_delay_cal(df_hr_1)
    
    return df_hr_1