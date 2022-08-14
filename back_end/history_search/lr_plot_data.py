import pandas as pd
from IPython.display import display

import history_search.lr_data as lr
import history_search.data_analysis as da
import history_search.res_data_formatter as rd


### TYPE 1 - PLOTS RELATED TO STATION ###
# p_lr_1a - Display real waiting time patterns (LineChart)
def json_p_lr_1a_create(query):

    column_flag = {
        'ttnt_eta': 1,
        'ttnt_real': 1,
        'ttnt_eta_delay': 0,
        'ttnt_real_delay': 0
    }

    plot_parm = {
        'x': 'curr_time',
        'y': 'ttnt_real',
        'group_by': ['route_no']
    }

    # STEP 1 - Generate suitable dataframe (i.e. df_p_lr_1a)
    df_p_lr_1a = lr.df_lr_1_create(query, column_flag)

    # STEP 2 - Reshape dataframe to response json
    df_p_lr_1a = df_p_lr_1a.astype({'curr_time': 'string'})
    result = rd.line_chart_convert(df_p_lr_1a, plot_parm)

    return result


# p_lr_1b - Count number of train arrivals (StackedBarChart)
def json_p_lr_1b_create(query):

    column_flag = {
        'ttnt_eta': 1,
        'ttnt_real': 1,
        'ttnt_eta_delay': 0,
        'ttnt_real_delay': 0
    }

    group_parm = {
        'mode': 1,
        'freq': '30Min'
    }

    plot_parm = {
        'x': 'curr_time',
        'y': 'ttnt_real',
        'group_by': ['route_no']
    }

    # STEP 1 - Generate suitable dataframe (i.e. df_p_lr_1b)
    df_p_lr_1b = lr.df_lr_1_create(query, column_flag)
    df_p_lr_1b = da.find_train_arrival(df_p_lr_1b)
    df_p_lr_1b = da.group_train_arrival(df_p_lr_1b, group_parm)

    # STEP 2 - Reshape dataframe to response json
    df_p_lr_1b = df_p_lr_1b.astype({'curr_time': 'string'})
    result = rd.stacked_bar_chart_convert(df_p_lr_1b, plot_parm)

    return result


# p_lr_1c - Display eta delay time patterns (LineChart)
def json_p_lr_1c_create(query):

    # STEP 1 - Generate suitable dataframe (i.e. df_p_lr_1c)
    column_flag = {
        'ttnt_eta': 1,
        'ttnt_real': 1,
        'ttnt_eta_delay': 1,
        'ttnt_real_delay': 0
    }

    plot_parm = {
        'x': 'curr_time',
        'y': 'ttnt_eta_delay',
        'group_by': ['route_no']
    }

    df_p_lr_1c = lr.df_lr_1_create(query, column_flag)

    # STEP 2 - Reshape dataframe to response json
    df_p_lr_1c = df_p_lr_1c.astype({'curr_time': 'string'})
    result = rd.line_chart_convert(df_p_lr_1c, plot_parm)

    return result


# p_lr_1d - Display real delay time patterns (ScatterChart)
def json_p_lr_1d_create(query):

    column_flag = {
        'ttnt_eta': 1,
        'ttnt_real': 1,
        'ttnt_eta_delay': 1,
        'ttnt_real_delay': 1
    }

    group_parm = {
        'mode': 2,
        'freq': '30Min'
    }

    plot_parm = {
        'x': 'curr_time',
        'y': 'ttnt_real_delay',
        'group_by': ['route_no']
    }

    # STEP 1 - Generate suitable dataframe (i.e. df_p_lr_1d)
    df_p_lr_1d = lr.df_lr_1_create(query, column_flag)
    df_p_lr_1d = da.group_train_arrival(df_p_lr_1d, group_parm)

    # STEP 2 - Reshape dataframe to response json
    df_p_lr_1d = df_p_lr_1d.astype({'curr_time': 'string'})
    result = rd.scatter_chart_convert(df_p_lr_1d, plot_parm)
    
    return result


### TYPE 2 - PLOTS RELATED TO TRIPS BETWEEN TWO STATIONS ###
# df_p_lr_2a - Display combined waiting time of ALL available routes to a station (Line Chart)
def json_p_lr_2a_create(query):

    # STEP 1 - Generate suitable dataframe (i.e. df_p_lr_2a)
    column_flag = {
        'ttnt_eta': 1,
        'ttnt_real': 1,
        'ttnt_eta_delay': 0,
        'ttnt_real_delay': 0
    }

    plot_parm = {
        'x': 'curr_time',
        'y': 'ttnt_real',
        'group_by': ['route_no']
    }
    
    df_p_lr_2a = lr.df_lr_2_create(query, column_flag)

    # STEP 2 - Reshape dataframe to response json
    df_p_lr_2a = df_p_lr_2a.astype({'curr_time': 'string'})
    result = rd.line_chart_convert(df_p_lr_2a, plot_parm)

    return result
