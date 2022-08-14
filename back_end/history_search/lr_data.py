import pandas.io.sql as sqlio
import history_search.db_connection as db

import pandas as pd
from IPython.display import display

import history_search.data_analysis as da


### Type 1: Data Extraction ###
# raw_lr_1_extract: Extract train waiting time data of single station
def raw_lr_1_extract(query):

    connection = db.connect()

    sql_lr_1 = '''Select lr_base_data.sys_time, lr_route_list.route_no, lr_route_list.train_length, lr_base_data.station_id, lr_route_list.dest_en, lr_route_list.time_en from lr_base_data, lr_route_list
                        where lr_base_data.lr_data_id = lr_route_list.lr_data_id
                            and lr_base_data.station_id = '{0}'
                            and lr_route_list.platform_id = '{1}'
                            and lr_base_data.sys_time >= '{2}'
                            and lr_base_data.sys_time < '{3}'
                        order by lr_base_data.sys_time asc;'''.format(query['start_station_id'], query['platform_id'], query['start_time'], query['end_time'])

    result = sqlio.read_sql_query(sql_lr_1, connection)

    return(result)


### Type 2: Data Cleaning + Append ###
# df_lr_base_append: Conduct basic data cleaning + data append
def df_lr_base_append(df_lr):

    # Part 1: Fix the formatting of data columns
    df_lr = df_lr.rename(columns={
                            'sys_time': 'curr_time', 
                            'route_no': 'route_no',
                            'train_length': 'train_len',
                            'station_id': 'curr_station_id', 
                            'dest_en': 'dest_station_id',
                            'time_en': 'ttnt_eta'})

    df_lr.loc[df_lr['ttnt_eta'] == 'Arriving', 'ttnt_eta'] = '1 min'
    df_lr.loc[df_lr['ttnt_eta'] == 'Departing', 'ttnt_eta'] = '0 min'
    df_lr.loc[df_lr['ttnt_eta'] == '-', 'ttnt_eta'] = '0 min'
    df_lr['ttnt_eta'] = df_lr['ttnt_eta'].str.split(' ', 0).str[0]

    df_lr = df_lr.astype({
                    'curr_time': 'datetime64[ns]',
                    'route_no': 'str', 
                    'train_len': 'int', 
                    'curr_station_id': 'str',
                    'dest_station_id': 'str',
                    'ttnt_eta': 'int'})

    df_lr = df_lr.reindex(columns=['curr_time', 'route_no', 'train_len', 'curr_station_id', 'dest_station_id', 'ttnt_eta'])

    # Part 2: Reorder the data according to route and time + Pick only the data of next train
    df_lr.sort_values(by=['curr_time', 'route_no', 'ttnt_eta'], inplace=True)
    df_lr = df_lr.reset_index(drop=True)

    df_lr = df_lr.groupby(['curr_time', 'route_no'], as_index=False).first()
    df_lr.sort_values(by=['route_no', 'curr_time'], inplace=True)
    df_lr = df_lr.reset_index(drop=True)


    return df_lr


# df_lr_1_create: Create dataframe for chart type p_lr_1
def df_lr_1_create(query, column_flag):

    # Step 1 - Extract the data
    df_lr_1 = raw_lr_1_extract(query)

    # Step 2 - Conduct data cleaning + data analysis
    # Append basic information
    df_lr_1 = df_lr_base_append(df_lr_1)

    # Append time information
    if column_flag['ttnt_eta'] == 1:
        df_lr_1 = da.ttnt_eta_cal(df_lr_1)

    if column_flag['ttnt_real'] == 1:
        df_lr_1 = da.ttnt_real_cal_1(df_lr_1)

    if column_flag['ttnt_eta_delay'] == 1:
        df_lr_1 = da.ttnt_eta_delay_cal(df_lr_1)

    if column_flag['ttnt_real_delay'] == 1:
        df_lr_1 = da.ttnt_real_delay_cal(df_lr_1)   
    
    return df_lr_1


# df_lr_2_create: Create dataframe for chart type p_lr_2
def df_lr_2_create(query, column_flag):

    # Step 1 - Extract the data
    df_lr_2 = raw_lr_1_extract(query)

    # Step 2 - Conduct data cleaning + data analysis
    # Append basic information
    df_lr_2 = df_lr_base_append(df_lr_2)

    # Append time information
    if column_flag['ttnt_eta'] == 1:
        df_lr_2 = da.ttnt_eta_cal(df_lr_2)

    if column_flag['ttnt_real'] == 1:
        df_lr_2 = da.ttnt_real_cal_2(df_lr_2)

    if column_flag['ttnt_eta_delay'] == 1:
        df_lr_2 = da.ttnt_eta_delay_cal(df_lr_2)

    if column_flag['ttnt_real_delay'] == 1:
        df_lr_2 = da.ttnt_real_delay_cal(df_lr_2)   
    
    return df_lr_2
