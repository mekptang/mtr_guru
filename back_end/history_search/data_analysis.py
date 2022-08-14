import pandas as pd
from IPython.display import display

import history_search.hr_data as hr
import history_search.lr_data as lr


# ttnt_eta_cal: Calculate column 'ttnt_eta' 
def ttnt_eta_cal(df): 

    # Calculate and append missing train arrival records
    temp_1 = df.loc[(df['ttnt_eta'].shift(-1) - df['ttnt_eta'] > 1) & 
                    (df['ttnt_eta'] != 0) & 
                    (df['route_no'].shift(-1) == df['route_no'])].reset_index(drop=True)

    temp_2 = df.loc[(df['ttnt_eta'] - df['ttnt_eta'].shift(1) > 1) & 
                    (df['ttnt_eta'].shift(1) != 0) & 
                    (df['route_no'].shift(1) == df['route_no'])].reset_index(drop=True)
                    
    temp_1['curr_time'] = temp_1['curr_time'] + (temp_2['curr_time'] - temp_1['curr_time'])/2
    temp_1['ttnt_eta'] = 0

    df = df.append(temp_1, ignore_index=True).sort_values(by=['route_no', 'curr_time']).reset_index(drop=True)
    df['curr_time'] = pd.to_datetime(df['curr_time']).apply(lambda x: x.replace(microsecond=0))

    # Calculate and append missing waiting time records

    return df

 
# ttnt_real_cal_1: Calcuate column 'ttnt_real' for individual line sceneario
def ttnt_real_cal_1(df):

    df['ttnt_real'] = df['ttnt_eta']

    for i in df.index:
        temp_1 = df.iloc[i:]
        temp_1 = temp_1.loc[(temp_1['route_no'] == df.at[i, 'route_no']) & (temp_1['ttnt_eta'] == 0)].head(1)
        
        if not temp_1.empty:
            time_diff_s = (temp_1['curr_time'] - df.at[i, 'curr_time']).values[0].astype('timedelta64[s]').astype(int)
            time_diff_m = round(time_diff_s / 60) if ((time_diff_s >= 30) or (time_diff_s == 0)) else 1
            
            df.at[i, 'ttnt_real'] = time_diff_m

    return df


# ttnt_real_cal_2: Calculate column 'ttnt_real' for combined lines sceneario
def ttnt_real_cal_2(df):

    # Calculate individual lines real waiting time pattern ('ttnt_real')
    df = ttnt_real_cal_1(df)

    # Calculate combined lines real waiting time pattern ('ttnt_real')
    df.sort_values(by=['curr_time', 'ttnt_real'], inplace=True)
    df = df.reset_index(drop=True)

    temp_2 = pd.DataFrame()

    for i in df.index:
        temp_1 = df.iloc[i:]
        temp_1 = temp_1.loc[(temp_1['ttnt_real'] == 0)].head(1).reset_index(drop=True)
        
        if not (temp_1.empty):
            if (df.at[i, 'route_no'] == temp_1.iloc[0]['route_no']):
                temp_2 = temp_2.append(df.iloc[i], ignore_index=True)
        else:
            temp_2 = temp_2.append(df.iloc[i], ignore_index=True)

    temp_2 = temp_2.reset_index(drop=True)
    temp_2 = temp_2.groupby(['curr_time']).first().reset_index()

    df = temp_2

    return df


# ttnt_eta_delay_cal: Calcuate column 'ttnt_eta_delay'
def ttnt_eta_delay_cal(df):

    df['ttnt_eta_delay'] = 0
    df['ttnt_eta_delay'] = df['ttnt_real'] - df['ttnt_eta']

    return df


# ttnt_real_delay_cal: Calcuate column 'ttnt_real_delay'
def ttnt_real_delay_cal(df):

    df['ttnt_real_delay'] = 0

    # Extract train arrival records and drop duplicate records
    df = df.drop(df[(df['curr_time'].diff().dt.seconds < 120) & 
                    (df['ttnt_real'] == 0) & 
                    (df['ttnt_real'].shift(1) == 0) & 
                    (df['route_no'].shift(1) == df['route_no'])].index)
    
    # Calculate 'ttnt_real_delay' by finding the difference between 
    # eta time and real waiting time right after departure of previous train
    df = df[(df['ttnt_real'].shift(1) == 0)]
    df['ttnt_real_delay'] = df['ttnt_eta_delay']
    df = df.reset_index(drop=True)

    return df


# find_train_arrival: Extract train arrivals record
def find_train_arrival(df):

    # Extract train arrival records and drop duplicate records
    df = df.drop(df[(df['curr_time'].diff().dt.seconds < 120) & 
                    (df['ttnt_real'] == 0) & 
                    (df['ttnt_real'].shift(1) == 0) & 
                    (df['route_no'].shift(1) == df['route_no'])].index)
    
    df = df[df['ttnt_real'] == 0]

    return df


# group_train_arrival: Group train arrivals record
def group_train_arrival(df, parm):

    if parm['mode'] == 1:
        df = df.groupby([pd.Grouper(key='curr_time', freq=parm['freq']), 'route_no']).agg({'ttnt_real': 'count'}).reset_index()

    elif parm['mode'] == 2:
        df['curr_time'] = df['curr_time'].dt.floor(parm['freq'])

    return df