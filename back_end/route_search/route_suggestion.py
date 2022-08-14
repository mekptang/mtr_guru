import pandas as pd
from IPython.display import display
import networkx as nx
import itertools
import asyncio
import json
import math

import route_search.route_network as rn
import route_search.eta_data_extract as eta
import history_search.hr_data as hr
import history_search.lr_data as lr
import history_search.data_analysis as da


def suggest_route(input_parm):

    start_station_id = input_parm['start_station_id']
    dest_station_id = input_parm['dest_station_id']
    mode = input_parm['mode']


    # Find route combinations
    all_route_list = ['505', '507', '610', '614', '615', '615P', '705', '706', '751', '761P']
    start_route_list = rn.route_list_all_find(start_station_id)
    dest_route_list = rn.route_list_all_find(dest_station_id)
    
    rn.route_list_all_find(dest_station_id)

    df_rn = rn.df_route_graph_create()
    G_all = nx.from_pandas_edgelist(df_rn['ALL'], 'source', 'target', edge_attr=True, create_using=nx.MultiDiGraph())


    # Generate possible routes
    path_all = []

    for i in start_route_list:
        for j in dest_route_list:
            for k in all_route_list:

                # Generate combined graph of candidate routes
                df_rn_temp_1 = pd.concat([df_rn[i], df_rn[j], df_rn[k], df_rn['WALK']]).drop_duplicates()
                df_rn_temp_2 = pd.concat([df_rn[i], df_rn[j], df_rn['TML'], df_rn['TCL'], df_rn['WALK']]).drop_duplicates()

                G_1 = nx.from_pandas_edgelist(df_rn_temp_1, 'source', 'target', edge_attr=True, create_using=nx.MultiDiGraph())
                G_2 = nx.from_pandas_edgelist(df_rn_temp_2, 'source', 'target', edge_attr=True, create_using=nx.MultiDiGraph())
            
                # Generate candidate graph
                if (G_1.has_node(start_station_id)) & (G_1.has_node(dest_station_id)) & (nx.has_path(G_1, start_station_id, dest_station_id)):
                        path_temp = nx.dijkstra_path(G_1, start_station_id, dest_station_id, 'weight')
                        path_all.append(path_temp)

                if (G_2.has_node(start_station_id)) & (G_2.has_node(dest_station_id)) & (nx.has_path(G_2, start_station_id, dest_station_id)):
                        path_temp = nx.dijkstra_path(G_2, start_station_id, dest_station_id, 'weight')
                        path_all.append(path_temp)

                path_all.sort()
                path_all = list(k for k,_ in itertools.groupby(path_all))


    # Genereate trip info for each candidate route
    path_data_all = []

    for item in path_all:

        start = 0
        path_data = []
        total_travel_time = 0
        total_walk_time = 0
        total_wait_time = 0
        total_train_time = 0
        interchange = -1

        temp_walk_data = {}
        temp_path_data = {}

        temp_1 = start_route_list

        # Handle case with route that contains 2 stops
        if (len(item) == 2):

            route_list_1 = rn.route_list_edge_find(item[0], item[1])

            if (item[0].isalpha() == item[1].isalpha()):

                platform_list = rn.platform_list_edge_find(item[0], item[1], route_list_1)

                if (item[0].isalpha()):
                    eta_raw = asyncio.run(eta.eta_raw_extract([platform_list['route'][0] + '-' + item[0]]))
                    eta_raw = eta_raw['hr'][platform_list['route'][0] + '-' + item[0]]
                    eta_clean = eta.hr_eta_clean_extract(eta_raw, platform_list['route'][0] + '-' + item[0], platform_list)
                    
                    query = {
                        'graph': 'p_hr_1d',
                        'start_station_id': platform_list['route'][0] + '-' + item[0],
                        'direction': 'up',
                        'start_time': '2022-04-22 16:00',
                        'end_time': '2022-04-22 18:00'  
                    }

                    column_flag = {
                        'ttnt_eta': 1,
                        'ttnt_real': 1,
                        'ttnt_eta_delay': 1,
                        'ttnt_real_delay': 1
                    }

                    df_p_hr = hr.df_hr_1_create(query, column_flag)
                    df_p_hr = da.find_train_arrival(df_p_hr)
                    eta_delay_time = df_p_hr['ttnt_real_delay'].mean()

                    df_p_hr = lr.df_lr_1_create(query, column_flag)
                    eta_delay_time = df_p_hr['ttnt_eta_delay'].mean()

                else:
                    eta_raw = asyncio.run(eta.eta_raw_extract([item[0]]))
                    eta_raw = eta_raw['lr'][item[0]]
                    eta_clean = eta.lr_eta_clean_extract(eta_raw, item[0], platform_list)

                    query = {
                        'graph': 'p_lr_1d',
                        'start_station_id': item[0],
                        'platform_id': platform_list['platform'][0],
                        'start_time': '2022-04-22 16:00',
                        'end_time': '2022-04-22 18:00'  
                    }

                    column_flag = {
                        'ttnt_eta': 1,
                        'ttnt_real': 1,
                        'ttnt_eta_delay': 1,
                        'ttnt_real_delay': 1
                    }

                    df_p_lr = lr.df_lr_1_create(query, column_flag)
                    eta_delay_time = df_p_lr['ttnt_eta_delay'].mean()


                # Store Trip data
                temp_path_data = {
                    'start_station': rn.station_name_find(item[0])['station_name'],
                    'start_station_type': rn.station_name_find(item[0])['station_type'],
                    'end_station': rn.station_name_find(item[1])['station_name'],
                    'end_station_type': rn.station_name_find(item[1])['station_type'],
                    'route': temp_1,
                    'eta_list': eta_clean['eta_list'],
                    'transit_time': round(nx.path_weight(G_all, item, 'weight')),
                    'wait_time': eta_clean['first_wait_time'] if len(path_data) == 0 else eta_clean['avg_wait_time'],
                    'eta_delay_time': math.floor(eta_delay_time),
                    'path_id': len(path_data) + 1
                }

                total_travel_time = total_travel_time + (temp_path_data['transit_time'] + temp_path_data['wait_time'])
                total_walk_time = total_walk_time + 0
                total_wait_time = total_wait_time + temp_path_data['wait_time']
                total_train_time = total_train_time + temp_path_data['transit_time']
                interchange = interchange + 1

            else:

                temp_path_data = {
                    'start_station': rn.station_name_find(item[0])['station_name'],
                    'start_station_type': rn.station_name_find(item[0])['station_type'],
                    'end_station': rn.station_name_find(item[1])['station_name'],
                    'end_station_type': rn.station_name_find(item[1])['station_type'],
                    'route': ['WALK'],
                    'description': rn.station_description_find(item[0]),
                    'transit_time': round(nx.path_weight(G_all, item, 'weight')),
                    'wait_time': 0,
                    'eta_delay_time': 0,
                    'path_id': len(path_data) + 1
                }

                total_travel_time = total_travel_time + temp_path_data['transit_time']
                total_walk_time = total_walk_time + temp_path_data['transit_time']
                total_wait_time = total_wait_time + 0
                total_train_time = total_train_time + 0
                interchange = interchange + 1

            path_data.append(temp_path_data)


        # Handle case with route more than 2 stops
        else:

            for i in range(1, len(item) - 1):

                route_list_1 = rn.route_list_edge_find(item[i - 1], item[i])
                route_list_2 = rn.route_list_edge_find(item[i], item[i + 1])
                temp_1 = list(set(temp_1).intersection(route_list_1))
                temp_2 = list(set(temp_1).intersection(route_list_2))

                # If current stop need interchange
                if (len(temp_2) == 0):

                    # Extract ETA data
                    if (item[i-1].isalpha() == item[i].isalpha()):

                        platform_list = rn.platform_list_edge_find(item[start], item[start + 1], temp_1)

                        if (item[start].isalpha()):
                            eta_raw = asyncio.run(eta.eta_raw_extract([platform_list['route'][0] + '-' + item[start]]))
                            eta_raw = eta_raw['hr'][platform_list['route'][0] + '-' + item[start]]
                            eta_clean = eta.hr_eta_clean_extract(eta_raw, platform_list['route'][0] + '-' + item[start], platform_list)
                        
                            query = {
                                'graph': 'p_hr_1d',
                                'start_station_id': platform_list['route'][0] + '-' + item[0],
                                'direction': 'up',
                                'start_time': '2022-04-22 16:00',
                                'end_time': '2022-04-22 18:00'  
                            }

                            column_flag = {
                                'ttnt_eta': 1,
                                'ttnt_real': 1,
                                'ttnt_eta_delay': 1,
                                'ttnt_real_delay': 0
                            }

                            df_p_hr = hr.df_hr_1_create(query, column_flag)
                            eta_delay_time = df_p_hr['ttnt_eta_delay'].mean()

                        else:
                            eta_raw = asyncio.run(eta.eta_raw_extract([item[start]]))
                            eta_raw = eta_raw['lr'][item[start]]
                            eta_clean = eta.lr_eta_clean_extract(eta_raw, item[start], platform_list)

                            query = {
                                'graph': 'p_lr_1d',
                                'start_station_id': item[start],
                                'platform_id': platform_list['platform'][0],
                                'start_time': '2022-04-22 16:00',
                                'end_time': '2022-04-22 18:00'  
                            }

                            column_flag = {
                                'ttnt_eta': 1,
                                'ttnt_real': 1,
                                'ttnt_eta_delay': 1,
                                'ttnt_real_delay': 0
                            }

                            df_p_lr = lr.df_lr_1_create(query, column_flag)
                            eta_delay_time = df_p_lr['ttnt_eta_delay'].mean()

                        # Store Trip data
                        temp_path_data = {
                            'start_station': rn.station_name_find(item[start])['station_name'],
                            'start_station_type': rn.station_name_find(item[start])['station_type'],
                            'end_station': rn.station_name_find(item[i])['station_name'],
                            'end_station_type': rn.station_name_find(item[i])['station_type'],
                            'route': temp_1,
                            'eta_list': eta_clean['eta_list'],
                            'transit_time': round(nx.path_weight(G_all, item[start:(i + 1)], 'weight')),
                            'wait_time': eta_clean['first_wait_time'] if len(path_data) == 0 else eta_clean['avg_wait_time'],
                            'eta_delay_time': math.floor(eta_delay_time),
                            'path_id': len(path_data) + 1
                        }

                        total_travel_time = total_travel_time + (temp_path_data['transit_time'] + temp_path_data['wait_time'])
                        total_walk_time = total_walk_time + 0
                        total_wait_time = total_wait_time + temp_path_data['wait_time']
                        total_train_time = total_train_time + temp_path_data['transit_time']
                        interchange = interchange + 1

                        # Insert Walk Info to previous trip
                        if (len(path_data) > 0):
                            if (path_data[-1]['route'][0] != 'WALK') & (temp_path_data['route'][0] != 'WALK'):

                                if (temp_path_data['route'][0]) == 'TML':
                                    whole_text = '請步行至屯馬線月台'
                                elif (temp_path_data['route'][0]) == 'TCL':
                                    whole_text =  '請步行至東涌線月台'
                                else:
                                    whole_text = '請步行轉乘 ' + ', '.join(path_data[-1]['route']) + ' 線'

                                temp_walk_data = {
                                    'start_station': path_data[-1]['end_station'],
                                    'start_station_type': path_data[-1]['end_station_type'],
                                    'end_station': temp_path_data['end_station'],
                                    'end_station_type': temp_path_data['end_station_type'],
                                    'route': ['WALK'],
                                    'description': whole_text,                            
                                    'transit_time': rn.station_walk_time_find(path_data[-1]['route'][0], item[start], item[start + 1]),
                                    'wait_time': 0,
                                    'eta_delay_time': 0,
                                    'path_id': len(path_data) + 1
                                }

                                path_data.append(temp_walk_data)

                                total_travel_time = total_travel_time + temp_walk_data['transit_time']
                                total_walk_time = total_walk_time + temp_walk_data['transit_time']
                                total_wait_time = total_wait_time + 0
                                total_train_time = total_train_time + 0
                                interchange = interchange + 0
    
                    # Provide heavy rail transfer to/from light rail info
                    else:

                        temp_path_data = {
                            'start_station': rn.station_name_find(item[start])['station_name'],
                            'start_station_type': rn.station_name_find(item[start])['station_type'],
                            'end_station': rn.station_name_find(item[i])['station_name'],
                            'end_station_type': rn.station_name_find(item[i])['station_type'],
                            'route': ['WALK'],
                            'description': rn.station_description_find(item[start]),
                            'transit_time': round(nx.path_weight(G_all, item[start:(i + 1)], 'weight')),
                            'wait_time': 0,
                            'eta_delay_time': 0,
                            'path_id': len(path_data) + 1
                        }

                        total_travel_time = total_travel_time + temp_path_data['transit_time']
                        total_walk_time = total_walk_time + temp_path_data['transit_time']
                        total_wait_time = total_wait_time + 0
                        total_train_time = total_train_time + 0
                        interchange = interchange + 0

                    path_data.append(temp_path_data)

                    start = i
                    temp_1 = route_list_2
                    temp_2 = list(set(temp_1).intersection(route_list_2))


                # If next stop reach destination
                if (item[i + 1] == dest_station_id):

                    # Extract ETA data
                    if (item[i].isalpha() == item[i+1].isalpha()):

                        platform_list = rn.platform_list_edge_find(item[start], item[start + 1], temp_2)

                        if (item[start].isalpha()):
                            eta_raw = asyncio.run(eta.eta_raw_extract([platform_list['route'][0] + '-' + item[start]]))
                            eta_raw = eta_raw['hr'][platform_list['route'][0] + '-' + item[start]]
                            eta_clean = eta.hr_eta_clean_extract(eta_raw, platform_list['route'][0] + '-' + item[start], platform_list)
                        
                            query = {
                                'graph': 'p_hr_1d',
                                'start_station_id': platform_list['route'][0] + '-' + item[start],
                                'direction': 'up',
                                'start_time': '2022-04-22 16:00',
                                'end_time': '2022-04-22 18:00'  
                            }

                            column_flag = {
                                'ttnt_eta': 1,
                                'ttnt_real': 1,
                                'ttnt_eta_delay': 1,
                                'ttnt_real_delay': 0
                            }

                            df_p_hr = hr.df_hr_1_create(query, column_flag)
                            eta_delay_time = df_p_hr['ttnt_eta_delay'].mean()

                        else:
                            eta_raw = asyncio.run(eta.eta_raw_extract([item[start]]))
                            eta_raw = eta_raw['lr'][item[start]]
                            eta_clean = eta.lr_eta_clean_extract(eta_raw, item[start], platform_list)

                            query = {
                                'graph': 'p_lr_1d',
                                'start_station_id': item[start],
                                'platform_id': platform_list['platform'][0],
                                'start_time': '2022-04-22 16:00',
                                'end_time': '2022-04-22 18:00'  
                            }

                            column_flag = {
                                'ttnt_eta': 1,
                                'ttnt_real': 1,
                                'ttnt_eta_delay': 1,
                                'ttnt_real_delay': 0
                            }

                            df_p_lr = lr.df_lr_1_create(query, column_flag)
                            eta_delay_time = df_p_lr['ttnt_eta_delay'].mean()

                        # Store Trip data
                        temp_path_data = {
                            'start_station': rn.station_name_find(item[start])['station_name'],
                            'start_station_type': rn.station_name_find(item[start])['station_type'],
                            'end_station': rn.station_name_find(item[i+1])['station_name'],
                            'end_station_type': rn.station_name_find(item[i+1])['station_type'],
                            'route': temp_2,
                            'eta_list': eta_clean['eta_list'],
                            'transit_time': round(nx.path_weight(G_all, item[start:(i + 2)], 'weight')),
                            'wait_time': eta_clean['first_wait_time'] if len(path_data) == 0 else eta_clean['avg_wait_time'],
                            'eta_delay_time': math.floor(eta_delay_time),
                            'path_id': len(path_data) + 1
                        }

                        total_travel_time = total_travel_time + temp_path_data['transit_time'] + temp_path_data['wait_time']
                        total_walk_time = total_walk_time + 0
                        total_wait_time = total_wait_time + temp_path_data['wait_time']
                        total_train_time = total_train_time + temp_path_data['transit_time']
                        interchange = interchange + 1

                        # Insert Walk Info to previous trip
                        if (len(path_data) > 0):
                            if (path_data[-1]['route'][0] != 'WALK') & (temp_path_data['route'][0] != 'WALK'):

                                if (temp_path_data['route'][0]) == 'TML':
                                    whole_text = '請步行至屯馬線月台'
                                elif (temp_path_data['route'][0]) == 'TCL':
                                    whole_text =  '請步行至東涌線月台'
                                else:
                                    whole_text = '請步行轉乘 ' + ', '.join(path_data[-1]['route']) + ' 線'

                                temp_walk_data = {
                                    'start_station': path_data[-1]['end_station'],
                                    'start_station_type': path_data[-1]['end_station_type'],
                                    'end_station': temp_path_data['end_station'],
                                    'end_station_type': temp_path_data['end_station_type'],
                                    'route': ['WALK'],
                                    'description': whole_text,                            
                                    'transit_time': rn.station_walk_time_find(path_data[-1]['route'][0], item[start], item[start + 1]),
                                    'wait_time': 0,
                                    'eta_delay_time': 0,
                                    'path_id': len(path_data) + 1
                                }

                                path_data.append(temp_walk_data)

                                total_travel_time = total_travel_time + temp_walk_data['transit_time']
                                total_walk_time = total_walk_time + temp_walk_data['transit_time']
                                total_wait_time = total_wait_time + 0
                                total_train_time = total_train_time + 0
                                interchange = interchange + 0


                    # Provide heavy rail transfer to/from light rail info
                    else:

                        temp_path_data = {
                            'start_station': rn.station_name_find(item[start])['station_name'],
                            'start_station_type': rn.station_name_find(item[start])['station_type'],
                            'end_station': rn.station_name_find(item[i+1])['station_name'],
                            'end_station_type': rn.station_name_find(item[i+1])['station_type'],
                            'route': ['WALK'],
                            'description': rn.station_description_find(item[start]),
                            'transit_time': round(nx.path_weight(G_all, item[start:(i + 2)], 'weight')),
                            'wait_time': 0,
                            'eta_delay_time': 0,
                            'path_id': len(path_data) + 1
                        }

                        total_travel_time = total_travel_time + temp_path_data['transit_time']
                        total_walk_time = total_walk_time + temp_path_data['transit_time']
                        total_wait_time = total_wait_time + 0
                        total_train_time = total_train_time + 0
                        interchange = interchange + 0

                    path_data.append(temp_path_data)

                        
        # Return whole trip data
        path_data = {
            'total_travel_time': total_travel_time,
            'total_walk_time': total_walk_time,
            'total_wait_time': total_wait_time,
            'total_train_time': total_train_time,
            'interchange': interchange,
            'path_length': len(path_data) ,
            'path_data': path_data
        }

        path_data_all.append(path_data)

        if mode == '1':
            path_data_all = sorted(path_data_all, key=lambda d: d['total_travel_time']) 
        elif mode == '2':
            path_data_all = sorted(path_data_all, key=lambda d: d['interchange']) 
        elif mode == '3':
            path_data_all = sorted(path_data_all, key=lambda d: d['total_walk_time']) 

    path_data_all = json.dumps(path_data_all)

    return path_data_all