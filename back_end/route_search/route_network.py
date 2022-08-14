import pandas as pd
from IPython.display import display

import route_search.route_network_data as nd
import time


whole_train_network = nd.whole_graph_data

# df_graph_create: Create dataframe of graph for whole network and each route
def df_route_graph_create():

    # STEP 1: Convert heavy rail and light rail graph data
    df_graph_whole = pd.DataFrame()

    for key, value in whole_train_network.items():

        for item in value['route_data']:
            for i in range(len(item['route_no'])):

                graph_temp = {}
                graph_temp['route_no'] = item['route_no'][i]
                graph_temp['source'] = item['edge'][0]
                graph_temp['target'] = item['edge'][1]
                graph_temp['weight'] = item['edge'][2]
                graph_temp['platform'] = item['platform'][i]

                df_graph_whole = df_graph_whole.append(graph_temp, ignore_index=True)


    # STEP 2: Store data in terms of suitable groups
    # Store data of individual route
    datasets = {}

    for route_no, df_graph_route in df_graph_whole.groupby('route_no'):

        df_graph_route = df_graph_route.reset_index(drop=True)
        datasets[route_no] = df_graph_route
    
    # Store data of whole network
    datasets['ALL'] = df_graph_whole

    return datasets


# df_platform_create: Create dataframe of graph for whole network and each route
def df_station_platform_create():

    # STEP 1: Convert station platform data
    df_platform_whole = pd.DataFrame()

    for key_1, value_1 in whole_train_network.items():
        for item in value_1['platform_data']:

            df_platform_temp = pd.DataFrame()
            df_platform_temp['station_id'] = key_1
            df_platform_temp[['source', 'target', 'weight']] = item['edge'][0]
            df_platform_whole = df_platform_whole.append(df_platform_temp, ignore_index=True)
    
    df_graph_whole = df_graph_whole.reindex(columns=['station_id', 'source', 'target', 'weight'])

    return df_graph_whole


def station_id_find(station_name):

    # Loop the network
    for key_1 in whole_train_network.keys():
        for key_2, value_2 in whole_train_network[key_1].items():
            if station_name == value_2['name']:

                return key_2
    
    return ''


def station_name_find(station_id):

    # Loop the network
    result = {
        'station_name': whole_train_network[station_id]['station_name']['ch'],
        'station_type': 'hr' if (station_id.isalpha()) else 'lr'
    }

    return result


def route_list_all_find(station_id):

    route_list = list()

    for item_1 in whole_train_network[station_id]['route_data']:
        [route_list.append(x) for x in item_1['route_no'] if x not in route_list] 

    return route_list


def route_list_edge_find(start_station_id, end_station_id):

    route_list = list()

    for item in whole_train_network[start_station_id]['route_data']:
        if ((item['edge'][0] == start_station_id) & (item['edge'][1] == end_station_id)):
    
            route_list = item['route_no']

    return route_list


def platform_list_edge_find(start_station_id, end_station_id, temp_1):

    platform_list = []
    route_list = []

    for item in whole_train_network[start_station_id]['route_data']:
        if ((item['edge'][0] == start_station_id) & (item['edge'][1] == end_station_id)):
    
            for i in temp_1:
                for j in range(len(item['route_no'])):

                    if i == item['route_no'][j]:
                        route_list.append(i)
                        platform_list.append(item['platform'][j])

    result = {
        'route': route_list,
        'platform': platform_list
    }

    return result


def station_description_find(station_id):

    for item in whole_train_network[station_id]['route_data']:

        if 'remarks' in item:
            result = item['remarks']['ch']

    return result


def station_walk_time_find(start_platform_id, start_station_id, end_station_id):

    walk_time = 0

    for item in whole_train_network[start_station_id]['route_data']:
        if (item['edge'][0] == start_station_id) & (item['edge'][1] == end_station_id):
            end_platform_id = item['platform'][0]

    for item in whole_train_network[start_station_id]['platform_data']:
        if (item['edge'][0] == start_platform_id) & (item['edge'][1] == end_platform_id):
            walk_time = item['edge'][2]
        if (item['edge'][1] == start_platform_id) & (item['edge'][0] == end_platform_id):
            walk_time = item['edge'][2]

    return walk_time
