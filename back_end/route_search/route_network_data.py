# whole_graph_data: Store whole graph data
whole_graph_data = {

    # Heavy Rail
    # Tuen Ma Line
    'WKS': { 'station_name':  { 'ch': '烏溪沙',
                                'en': 'Wu Kai Sha' },
             'route_data':    [{'edge': ('WKS', 'MOS', 3), 'route_no': ['TML', 'TML'], 'platform': ['1', '2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'MOS': { 'station_name':  { 'ch': '馬鞍山',
                                'en': 'Ma On Shan' },
             'route_data':    [{'edge': ('MOS', 'HEO', 2.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('MOS', 'WKS', 3), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'HEO': { 'station_name':  { 'ch': '恆安',
                                'en': 'Heng On' },
             'route_data':    [{'edge': ('HEO', 'TSH', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('HEO', 'MOS', 2.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'TSH': { 'station_name':  { 'ch': '大水坑',
                                'en': 'Tai Shui Hang' },
             'route_data':    [{'edge': ('TSH', 'SHM', 3.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('TSH', 'HEO', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'SHM': { 'station_name':  { 'ch': '石門',
                                'en': 'Shek Mun' },
             'route_data':    [{'edge': ('SHM', 'CIO', 1.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('SHM', 'TSH', 3.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'CIO': { 'station_name':  { 'ch': '第一城',
                                'en': 'City One' },
             'route_data':    [{'edge': ('CIO', 'STW', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('CIO', 'SHM', 1.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },                             


    'STW': { 'station_name':  { 'ch': '沙田圍',
                                'en': 'Sha Tin Wai' },
             'route_data':    [{'edge': ('STW', 'CKT', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('STW', 'CIO', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },
        

    'CKT': { 'station_name':  { 'ch': '車公廟',
                                'en': 'Che Kung Temple' },
             'route_data':    [{'edge': ('CKT', 'TAW', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('CKT', 'STW', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] }, 


    'TAW': { 'station_name':  { 'ch': '大圍',
                                'en': 'Tai Wai' },
             'route_data':    [{'edge': ('TAW', 'HIK', 2.5), 'route_no': ['TML'], 'platform': ['3']},
                               {'edge': ('TAW', 'CKT', 2), 'route_no': ['TML'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 2)}] },


    'HIK': { 'station_name':  { 'ch': '顯徑',
                                'en': 'Hin Keng' },
             'route_data':    [{'edge': ('HIK', 'DIH', 4.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('HIK', 'TAW', 2.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },                            
            

    'DIH': { 'station_name':  { 'ch': '鑽石山',
                                'en': 'Diamond Hill'},
             'route_data':    [{'edge': ('DIH', 'KAT', 2.5), 'route_no': ['TML'], 'platform': ['3']},
                               {'edge': ('DIH', 'HIK', 4.5), 'route_no': ['TML'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 0)}] },


    'KAT': { 'station_name':  { 'ch': '啟德',
                                'en': 'Kai Tak' },
             'route_data':    [{'edge': ('KAT', 'SUW', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('KAT', 'DIH', 2.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'SUW': { 'station_name':  { 'ch': '宋皇臺',
                                'en': 'Sung Wong Toi'}, 
             'route_data':    [{'edge': ('SUW', 'TKW', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('SUW', 'KAT', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'TKW': { 'station_name':  { 'ch': '土瓜灣',
                                'en': 'To Kwa Wan'},
             'route_data':    [{'edge': ('TKW', 'HOM', 2.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('TKW', 'SUW', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    
     

    'HOM': { 'station_name':  { 'ch': '何文田',
                                'en': 'Ho Man Tin' },
             'route_data':    [{'edge': ('HOM', 'HUH', 2.5), 'route_no': ['TML'], 'platform': ['3']},
                               {'edge': ('HOM', 'TKW', 2.5), 'route_no': ['TML'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 0)}] },


    'HUH': { 'station_name':  { 'ch': '紅磡',
                                'en': 'Hung Hom' },
             'route_data':    [{'edge': ('HUH', 'ETS', 2.5), 'route_no': ['TML'], 'platform': ['3']},
                               {'edge': ('HUH', 'HOM', 2.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('2', '3', 0)}] },


    'ETS': { 'station_name':  { 'ch': '尖東',
                                'en': 'East Tsim Sha Tsui' },
             'route_data':    [{'edge': ('ETS', 'AUS', 3), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('ETS', 'HUH', 2.5), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'AUS': { 'station_name':  { 'ch': '柯士甸',
                                'en': 'Austin' },
             'route_data':    [{'edge': ('AUS', 'NAC', 3), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('AUS', 'ETS', 3), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'NAC': { 'station_name':  { 'ch': '南昌',
                                'en': 'Nam Cheong'},
             'route_data':    [{'edge': ('NAC', 'MEF', 3), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('NAC', 'AUS', 3), 'route_no': ['TML'], 'platform': ['2']},
                               {'edge': ('NAC', 'LAK', 4), 'route_no': ['TCL'], 'platform': ['3']},
                               {'edge': ('NAC', 'OLY', 2), 'route_no': ['TCL'], 'platform': ['4']}],
             'platform_data': [{'edge': ('1', '2', 2)},
                               {'edge': ('1', '3', 3)}, 
                               {'edge': ('1', '4', 0)},
                               {'edge': ('2', '3', 3)},
                               {'edge': ('2', '4', 3)}] },


    'MEF': { 'station_name':  { 'ch': '美孚',
                                'en': 'Mei Foo' },
             'route_data':    [{'edge': ('MEF', 'TWW', 4), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('MEF', 'NAC', 3), 'route_no': ['TML'], 'platform': ['2']}], 
             'platform_data': [{'edge': ('1', '2', 1)}] },    


    'TWW': { 'station_name':  { 'ch': '荃灣西',
                                'en': 'Tsuen Wan West' },
             'route_data':    [{'edge': ('TWW', 'MEF', 4), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('TWW', 'KSR', 6), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },    


    'KSR': { 'station_name':  { 'ch': '錦上路',
                                'en': 'Kam Sheung Road' },
             'route_data':    [{'edge': ('KSR', 'YUL', 3.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('KSR', 'TWW', 6), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'YUL': { 'station_name':  { 'ch': '元朗',
                                'en': 'Yuen Long' },
             'route_data':    [{'edge': ('YUL', 'LOP', 2), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('YUL', 'KSR', 3.5), 'route_no': ['TML'], 'platform': ['2']},
                               {'edge': ('YUL', '600', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 E / G1 出口步行至元朗輕鐵站',
                                                                                                                 'en': 'Go to Exit E / G1 to reach Yuen Long Light Rail Station' }}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    'LOP': { 'station_name':  { 'ch': '朗屏',
                                'en': 'Long Ping' },
             'route_data':    [{'edge': ('LOP', 'TIS', 3), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('LOP', 'YUL', 2), 'route_no': ['TML'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'TIS': { 'station_name':  { 'ch': '天水圍',
                                'en': 'Tin Shui Wai' },
             'route_data':    [{'edge': ('TIS', 'SIH', 4.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('TIS', 'LOP', 3), 'route_no': ['TML'], 'platform': ['2']},
                               {'edge': ('TIS', '430', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 E 出口步行至天水圍輕鐵站',
                                                                                                                 'en': 'Go to Exit E to reach Tin Shui Wai Light Rail Station' }}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'SIH': { 'station_name':  { 'ch': '兆康',
                                'en': 'Siu Hong' },
             'route_data':    [{'edge': ('SIH', 'TUM', 2.5), 'route_no': ['TML'], 'platform': ['1']},
                               {'edge': ('SIH', 'TIS', 4.5), 'route_no': ['TML'], 'platform': ['2']},
                               {'edge': ('SIH', '100', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 B 出口步行至兆康輕鐵站',
                                                                                                                 'en': 'Go to Exit B to reach Siu Hong Light Rail Station' }}],
             'platform_data': [{'edge': ('1', '2', 0)}] },    


    'TUM': { 'station_name':  { 'ch': '屯門',
                                'en': 'Tuen Mun' },
             'route_data':    [{'edge': ('TUM', 'SIH', 2.5), 'route_no': ['TML', 'TML'], 'platform': ['1', '2']},
                               {'edge': ('TUM', '295', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 B 出口步行至屯門輕鐵站',
                                                                                                                 'en': 'Go to Exit B to reach Tuen Mun Light Rail Station' }}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    # Tung Chung Line
    'HOK': { 'station_name':  { 'ch': '香港',
                                'en': 'Hong Kong' },
             'route_data':    [{'edge': ('HOK', 'KOW', 4), 'route_no': ['TCL', 'TCL'], 'platform': ['3', '4']}],
             'platform_data': [{'edge': ('3', '4', 0)}] },


    'KOW': { 'station_name':  { 'ch': '九龍',
                                'en': 'Kowloon'}, 
             'route_data':    [{'edge': ('KOW', 'OLY', 2), 'route_no': ['TCL'], 'platform': ['3']},
                               {'edge': ('KOW', 'HOK', 4), 'route_no': ['TCL'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 0)}] },


    'OLY': { 'station_name':  { 'ch': '奧運',
                                'en': 'Olympic' },
             'route_data':    [{'edge': ('OLY', 'NAC', 2), 'route_no': ['TCL'], 'platform': ['1']},
                               {'edge': ('OLY', 'KOW', 2), 'route_no': ['TCL'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },
    

    'LAK': { 'station_name':  { 'ch': '茘景',
                                'en': 'Lai King' },
             'route_data':    [{'edge': ('LAK', 'TSY', 2.5), 'route_no': ['TCL'], 'platform': ['3']},
                               {'edge': ('LAK', 'NAC', 4), 'route_no': ['TCL'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 1)}] },

    
    'TSY': { 'station_name':  { 'ch': '青衣',
                                'en': 'Tsing Yi' },
             'route_data':    [{'edge': ('TSY', 'SUN', 7), 'route_no': ['TCL'], 'platform': ['3']},
                               {'edge': ('TSY', 'LAK', 2.5), 'route_no': ['TCL'], 'platform': ['4']}],
             'platform_data': [{'edge': ('3', '4', 1)}] },
    

    'SUN': { 'station_name':  { 'ch': '欣澳',
                                'en': 'Sunny Bay' },
             'route_data':    [{'edge': ('SUN', 'TUC', 7), 'route_no': ['TCL'], 'platform': ['1']},
                               {'edge': ('SUN', 'TSY', 7), 'route_no': ['TCL'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },
    

    'TUC': { 'station_name':  { 'ch': '東涌',
                                'en': 'Tung Chung' }, 
             'route_data':    [{'edge': ('TUC', 'SUN', 7), 'route_no': ['TCL', 'TCL'], 'platform': ['1', '2']}],
             'platform_data': [{'edge': ('1', '2', 0)}] },


    # Light Rail
    '1':   { 'station_name':  { 'ch': '屯門碼頭',
                                'en': 'Tuen Mun Ferry Pier' },
             'route_data':    [{'edge': ('1', '240', 3.5), 'route_no': ['507', '614', '614P'], 'platform': ['2', '5', '5']},
                               {'edge': ('1', '10', 2.5), 'route_no': ['610', '615', '615P'], 'platform': ['4', '3', '3']}],
             'platform_data': [{'edge': ('2', '3', 1)},
                               {'edge': ('2', '4', 1)},
                               {'edge': ('2', '5', 1)},
                               {'edge': ('3', '4', 1)},
                               {'edge': ('3', '5', 1)},
                               {'edge': ('4', '5', 1)}] },


    '10':  { 'station_name':   { 'ch': '美樂',
                                 'en': 'Melody Garden' },
             'route_data':     [{'edge': ('10', '15', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                                {'edge': ('10', '1', 2.5), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data':  [{'edge': ('1', '2', 1)}] },


    '15':  { 'station_name':  { 'ch': '蝴蝶',
                                'en': 'Butterfly' },
             'route_data':    [{'edge': ('15', '20', 1), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('15', '10', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '20':  { 'station_name':  { 'ch': '輕鐵車廠',
                                'en': 'Light Rail Depot' },
             'route_data':    [{'edge': ('20', '30', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('20', '15', 1), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '30':  { 'station_name':  { 'ch': '龍門',
                                'en': 'Lung Mun' },
             'route_data':    [{'edge': ('30', '40', 1), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('30', '20', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },

 
    '40':  { 'station_name':  { 'ch': '青山村',
                                'en': 'Tsing Shan Tsuen' },
             'route_data':    [{'edge': ('40', '50', 1), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('40', '30', 1), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '50':  { 'station_name':  { 'ch': '青雲',
                                'en': 'Tsing Wun' },
             'route_data':    [{'edge': ('50', '200', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('50', '40', 1), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '60':  { 'station_name':  { 'ch': '建安',
                                'en': 'Kin On' },
             'route_data':    [{'edge': ('60', '190', 2.5), 'route_no': ['505'], 'platform': ['1']},
                               {'edge': ('60', '295', 1.5), 'route_no': ['505'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '70':  { 'station_name':  { 'ch': '河田',
                                'en': 'Ho Tin' },
             'route_data':    [{'edge': ('70', '75', 1), 'route_no': ['507', '751'], 'platform': ['1', '1']},
                               {'edge': ('70', '295', 1.5), 'route_no': ['507', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '75':  { 'station_name':  { 'ch': '蔡意橋',
                                'en': 'Choy Yee Bridge' },
             'route_data':    [{'edge': ('75', '230', 2), 'route_no': ['507'], 'platform': ['1']},
                               {'edge': ('75', '80', 2), 'route_no': ['751'], 'platform': ['1']},
                               {'edge': ('75', '70', 1), 'route_no': ['507', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '80':  { 'station_name':  { 'ch': '澤豐',
                                'en': 'Affluence' },
             'route_data':    [{'edge': ('80', '90', 1.5), 'route_no': ['610', '751'], 'platform': ['1', '1']},
                               {'edge': ('80', '75', 2), 'route_no': ['751'], 'platform': ['2']},
                               {'edge': ('80', '230', 1.5), 'route_no': ['610'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '90':  { 'station_name':  { 'ch': '屯門醫院',
                                'en': 'Tuen Mun Hospital' },
             'route_data':    [{'edge': ('90', '100', 3), 'route_no': ['610', '751'], 'platform': ['1', '1']},
                               {'edge': ('90', '80', 1.5), 'route_no': ['610', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '100': { 'station_name':  { 'ch': '兆康',
                                'en': 'Siu Hong' },
             'route_data':    [{'edge': ('100', '350', 2), 'route_no': ['751', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('100', '90', 3), 'route_no': ['751', '610'], 'platform': ['2', '2']},
                               {'edge': ('100', '340', 2), 'route_no': ['614', '614P'], 'platform': ['2', '5']},
                               {'edge': ('100', '120', 3.5), 'route_no': ['505', '615'], 'platform': ['5', '2']},
                               {'edge': ('100', '110', 2), 'route_no': ['615P'], 'platform': ['6']},
                               {'edge': ('100', 'SIH', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 B 出口步行至兆康地鐵站',
                                                                                                                 'en': 'Go to Exit B to reach Siu Hong Railway Station' }}],
             'platform_data': [{'edge': ('1', '2', 1)},
                               {'edge': ('1', '5', 0)},
                               {'edge': ('1', '6', 1)},
                               {'edge': ('2', '5', 1)},
                               {'edge': ('2', '6', 1)},
                               {'edge': ('5', '6', 1)}] },


    '110': { 'station_name':  { 'ch': '麒麟',
                                'en': 'Kei Lun' },
             'route_data':    [{'edge': ('110', '100', 2), 'route_no': ['505', '615P'], 'platform': ['1', '1']},
                               {'edge': ('110', '120', 2), 'route_no': ['615P'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '120': { 'station_name':  { 'ch': '青松',
                                'en': 'Ching Chung' },
             'route_data':    [{'edge': ('120', '110', 2), 'route_no': ['505', '615P'], 'platform': ['1', '1']},
                               {'edge': ('120', '100', 3.5), 'route_no': ['615'], 'platform': ['1']},
                               {'edge': ('120', '130', 1.5), 'route_no': ['505', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '130': { 'station_name':  { 'ch': '建生',
                                'en': 'Kin Sang' },
             'route_data':    [{'edge': ('130', '120', 1.5), 'route_no': ['505', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('130', '140', 1.5), 'route_no': ['505', '615', '615P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '140': { 'station_name':  { 'ch': '田景',
                                'en': 'Tin King' },
             'route_data':    [{'edge': ('140', '130', 1.5), 'route_no': ['505', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('140', '150', 1.5), 'route_no': ['505', '507', '615', '615P'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '150': { 'station_name':  { 'ch': '良景',
                                'en': 'Leung King' },
             'route_data':    [{'edge': ('150', '140', 1.5), 'route_no': ['505', '507', '615', '615P'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('150', '160', 1.5), 'route_no': ['505', '507', '615', '615P'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '160': { 'station_name':  { 'ch': '新圍',
                                'en': 'San Wai' },
             'route_data':    [{'edge': ('160', '150', 1.5), 'route_no': ['505', '507', '615', '615P'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('160', '170', 2.5), 'route_no': ['505', '615', '615P'], 'platform': ['2', '2', '2']},
                               {'edge': ('160', '212', 3), 'route_no': ['507'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '170': { 'station_name':  { 'ch': '石排',
                                'en': 'Shek Pai' },
             'route_data':    [{'edge': ('170', '160', 2.5), 'route_no': ['505', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('170', '212', 3), 'route_no': ['610'], 'platform': ['2']},
                               {'edge': ('170', '200', 2), 'route_no': ['505', '610', '615', '615P'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '180': { 'station_name':  { 'ch': '山景 (北)',
                                'en': 'Shan King (North)' },
             'route_data':    [{'edge': ('180', '170', 2), 'route_no': ['505'], 'platform': ['1']}],
             'platform_data': [] },


    '190': { 'station_name':  { 'ch': '山景 (南)',
                                'en': 'Shan King (South)' },
             'route_data':    [{'edge': ('190', '180', 1), 'route_no': ['505'], 'platform': ['1']}],
             'platform_data': [] },


    '200': { 'station_name':  { 'ch': '鳴琴',
                                'en': 'Ming Kum' },
             'route_data':    [{'edge': ('200', '170', 2), 'route_no': ['610', '615', '615P'], 'platform': ['1', '1', '1']},
                               {'edge': ('200', '50', 1.5), 'route_no': ['610', '615', '615P'], 'platform': ['2', '2', '2']},
                               {'edge': ('200', '60', 1.5), 'route_no': ['505'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '212': { 'station_name':  { 'ch': '大興 (北)',
                                'en': 'Tai Hing (North)' },
             'route_data':    [{'edge': ('212', '160', 3), 'route_no': ['507'], 'platform': ['1']},
                               {'edge': ('212', '170', 3), 'route_no': ['610'], 'platform': ['1']},
                               {'edge': ('212', '220', 2), 'route_no': ['507', '610'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '220': { 'station_name':  { 'ch': '大興 (南)',
                                'en': 'Tai Hing (South)' },
             'route_data':    [{'edge': ('220', '212', 2), 'route_no': ['507', '610'], 'platform': ['1', '1']},
                               {'edge': ('220', '230', 1), 'route_no': ['507', '610'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '230': { 'station_name':  { 'ch': '銀圍',
                                'en': 'Ngan Wai' },
             'route_data':    [{'edge': ('230', '220', 1), 'route_no': ['507', '610'], 'platform': ['1', '1']},
                               {'edge': ('230', '75', 2), 'route_no': ['507'], 'platform': ['2']},
                               {'edge': ('230', '80', 1.5), 'route_no': ['610'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '240': { 'station_name':  { 'ch': '兆禧',
                                'en': 'Siu Hei' },
             'route_data':    [{'edge': ('240', '250', 2.5), 'route_no': ['507', '614', '614P'], 'platform': ['1', '1', '1']},
                               {'edge': ('240', '1', 3.5), 'route_no': ['507', '614', '614P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '250': { 'station_name':  { 'ch': '屯門泳池',
                                'en': 'Tuen Mun Swimming Pool' },
             'route_data':    [{'edge': ('250', '260', 1.5), 'route_no': ['507', '614', '614P'], 'platform': ['1', '1', '1']},
                               {'edge': ('250', '240', 2.5), 'route_no': ['507', '614', '614P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '260': { 'station_name':  { 'ch': '豐景園',
                                'en': 'Goodview Garden' },
             'route_data':    [{'edge': ('260', '265', 2), 'route_no': ['507', '614', '614P'], 'platform': ['1', '1', '1']},
                               {'edge': ('260', '250', 1.5), 'route_no': ['507', '614', '614P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '265': { 'station_name':  { 'ch': '兆麟',
                                'en': 'Siu Lun' },
             'route_data':    [{'edge': ('265', '270', 1.5), 'route_no': ['505', '507', '614', '614P'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('265', '260', 2), 'route_no': ['507', '614', '614P'], 'platform': ['2', '2', '2']},
                               {'edge': ('265', '920', 2.5), 'route_no': ['505'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '270': { 'station_name':  { 'ch': '安定',
                                'en': 'On Ting' },
             'route_data':    [{'edge': ('270', '280', 2), 'route_no': ['505', '507', '614', '614P', '751'], 'platform': ['1', '1', '1', '1', '1']},
                               {'edge': ('270', '265', 1.5), 'route_no': ['505', '507', '614', '614P'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '275': { 'station_name':  { 'ch': '友愛',
                                'en': 'Yau Oi' },
             'route_data':    [{'edge': ('275', '270', 2), 'route_no': ['751'], 'platform': ['1']}],
             'platform_data': [] },
             

    '280': { 'station_name':  { 'ch': '市中心',
                                'en': 'Town Centre' },
             'route_data':    [{'edge': ('280', '295', 2), 'route_no': ['505', '507', '751'], 'platform': ['1', '1', '1']},
                               {'edge': ('280', '300', 2.5), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('280', '270', 2), 'route_no': ['505', '507', '614', '614P'], 'platform': ['4', '4', '4', '4']},
                               {'edge': ('280', '275', 3), 'route_no': ['751'], 'platform': ['4']}],
             'platform_data': [{'edge': ('1', '4', 1)}] },


    '295': { 'station_name':  { 'ch': '屯門',
                                'en': 'Tuen Mun' },
             'route_data':    [{'edge': ('295', '60', 1.5), 'route_no': ['505'], 'platform': ['1']},
                               {'edge': ('295', '70', 1.5), 'route_no': ['507', '751'], 'platform': ['1', '1']},
                               {'edge': ('295', '280', 2), 'route_no': ['505', '507', '751'], 'platform': ['2', '2', '2']},
                               {'edge': ('295', 'TUM', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 B 出口步行至屯門地鐵站',
                                                                                                                 'en': 'Go to Exit B to reach Tuen Mun Railway Station' }}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '300': { 'station_name':  { 'ch': '杯渡',
                                'en': 'Pui To' },
             'route_data':    [{'edge': ('300', '310', 1.5), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('300', '280', 2.5), 'route_no': ['614', '614P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '310': { 'station_name':  { 'ch': '何福堂',
                                'en': 'Hoh Fuk Tong' },
             'route_data':    [{'edge': ('310', '320', 1.5), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('310', '300', 1.5), 'route_no': ['614', '614P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '320': { 'station_name':  { 'ch': '新墟',
                                'en': 'San Hui' },
             'route_data':    [{'edge': ('320', '330', 1), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('320', '310', 1.5), 'route_no': ['614', '614P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '330': { 'station_name':  { 'ch': '景峰',
                                'en': 'Prime View' },
             'route_data':    [{'edge': ('330', '340', 1.5), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('330', '320', 1), 'route_no': ['614', '614P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '340': { 'station_name':  { 'ch': '鳳地',
                                'en': 'Fung Tei' },
             'route_data':    [{'edge': ('340', '100', 2), 'route_no': ['614', '614P'], 'platform': ['1', '1']},
                               {'edge': ('340', '330', 1.5), 'route_no': ['614', '614P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '350': { 'station_name':  { 'ch': '藍地',
                                'en': 'Lam Tei' },
             'route_data':    [{'edge': ('350', '360', 1.5), 'route_no': ['751', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('350', '100', 2), 'route_no': ['751', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '360': { 'station_name':  { 'ch': '泥圍',
                                'en': 'Nai Wai' },
             'route_data':    [{'edge': ('360', '370', 1.5), 'route_no': ['751', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('360', '350', 1.5), 'route_no': ['751', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '370': { 'station_name':  { 'ch': '鍾屋村', 
                                'en': 'Chung Uk Tsuen' },
             'route_data':    [{'edge': ('370', '380', 2), 'route_no': ['751', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('370', '360', 1.5), 'route_no': ['751', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '380': { 'station_name':  { 'ch': '洪水橋',
                                'en': 'Hung Shui Kiu' },
             'route_data':    [{'edge': ('380', '390', 3.5), 'route_no': ['615', '610', '614'], 'platform': ['1', '1', '1']},
                               {'edge': ('380', '425', 4), 'route_no': ['751'], 'platform': ['1'] },
                               {'edge': ('380', '370', 2), 'route_no': ['751', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '390': { 'station_name':  { 'ch': '塘坊村', 
                                'en': 'Tong Fong Tsuen' }, 
             'route_data':    [{'edge': ('390', '400', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('390', '425', 3), 'route_no': ['761P'], 'platform': ['2']},
                               {'edge': ('390', '380', 3.5), 'route_no': ['615', '610', '614'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '400': { 'station_name':  { 'ch': '屏山',
                                'en': 'Ping Shan' },
             'route_data':    [{'edge': ('400', '560', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('400', '390', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '425': { 'station_name':  { 'ch': '坑尾村',
                                'en': 'Hang Mei Tsuen' },
             'route_data':    [{'edge': ('425', '430', 2.5), 'route_no': ['751'], 'platform': ['1']},
                               {'edge': ('425', '445', 2.5), 'route_no': ['761P'], 'platform': ['1']},
                               {'edge': ('425', '380', 4), 'route_no': ['751'], 'platform': ['2']},
                               {'edge': ('425', '390', 3), 'route_no': ['761P'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '430': { 'station_name':  { 'ch': '天水圍',
                                'en': 'Tin Shui Wai' },
                                
             'route_data':    [{'edge': ('430', '435', 1.5), 'route_no': ['705', '751'], 'platform': ['1', '2']},
                               {'edge': ('430', '445', 3.5), 'route_no': ['706'], 'platform': ['3']},
                               {'edge': ('430', '425', 2.5), 'route_no': ['751'], 'platform': ['3']},
                               {'edge': ('430', 'TIS', 2), 'route_no': ['WALK'], 'platform': ['0'], 
                                'remarks': { 'ch': '請由 E 出口步行至天水圍地鐵站',
                                             'en': 'Go to Exit E to reach Tin Shui Wai Railway Station' }}],

             'platform_data': [{'edge': ('1', '2', 0)},
                               {'edge': ('1', '3', 1)},
                               {'edge': ('2', '3', 1)}] },


    '435': { 'station_name':  { 'ch': '天慈',
                                'en': 'Tin Tsz' },
             'route_data':    [{'edge': ('435', '450', 1), 'route_no': ['705', '751'], 'platform': ['1', '1']}, 
                               {'edge': ('435', '430', 1.5), 'route_no': ['706', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '445': { 'station_name':  { 'ch': '天耀',
                                'en': 'Tin Yiu' },
             'route_data':    [{'edge': ('445', '430', 3.5), 'route_no': ['705'], 'platform': ['1']}, 
                               {'edge': ('445', '425', 2.5), 'route_no': ['761P'], 'platform': ['1']},
                               {'edge': ('445', '448', 2), 'route_no': ['706', '761P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '448': { 'station_name':  { 'ch': '樂湖',
                                'en': 'Locwood' },
             'route_data':    [{'edge': ('448', '460', 1.5), 'route_no': ['706', '761P'], 'platform': ['1', '1']},
                               {'edge': ('448', '445', 2), 'route_no': ['705', '761P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '450': { 'station_name':  { 'ch': '天湖',
                                'en': 'Tin Wu' }, 
             'route_data':    [{'edge': ('450', '455', 1), 'route_no': ['705', '751'], 'platform': ['1', '1']},
                               {'edge': ('450', '435', 1), 'route_no': ['706', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '455': { 'station_name':  { 'ch': '銀座',
                                'en': 'Ginza' },
             'route_data':    [{'edge': ('455', '500', 1.5), 'route_no': ['705', '751'], 'platform': ['1', '1']}, 
                               {'edge': ('455', '450', 1), 'route_no': ['706', '751'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '460': { 'station_name':  { 'ch': '天瑞',
                                'en': 'Tin Shui' },
             'route_data':    [{'edge': ('460', '468', 3.5), 'route_no': ['706', '761P'], 'platform': ['1', '1']},
                               {'edge': ('460', '448', 1.5), 'route_no': ['705', '761P'], 'platform': ['2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },   


    '468': { 'station_name':  { 'ch': '頌富',
                                'en': 'Chung Fu' },
             'route_data':    [{'edge': ('468', '480', 1.5), 'route_no': ['706', '751', '761P'], 'platform': ['1', '1', '1']},                
                               {'edge': ('468', '460', 3.5), 'route_no': ['705', '761P'], 'platform': ['2', '2']}, 
                               {'edge': ('468', '490', 3), 'route_no': ['751'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '480': { 'station_name':  { 'ch': '天富',
                                'en': 'Tin Fu' },
             'route_data':    [{'edge': ('480', '550', 1.5), 'route_no': ['706', '751', '761P'], 'platform': ['1', '1', '1']},
                               {'edge': ('480', '468', 1.5), 'route_no': ['705', '751', '761P'], 'platform': ['2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },                       


    '490': { 'station_name':  { 'ch': '翠湖',
                                'en': 'Chestwood' },
             'route_data':    [{'edge': ('490', '500', 2), 'route_no': ['751'], 'platform': ['1']},
                               {'edge': ('490', '468', 3), 'route_no': ['751'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },    


    '500': { 'station_name':  { 'ch': '天榮',
                                'en': 'Tin Wing' },
             'route_data':    [{'edge': ('500', '510', 2), 'route_no': ['705'], 'platform': ['6']}, 
                               {'edge': ('500', '490', 2), 'route_no': ['751'], 'platform': ['6']},
                               {'edge': ('500', '455', 1.5), 'route_no': ['706', '751'], 'platform': ['7', '7']}],
             'platform_data': [{'edge': ('6', '7', 1)}] },  


    '510': { 'station_name':  { 'ch': '天悅',
                                'en': 'Tin Yuet' },
             'route_data':    [{'edge': ('510', '520', 1), 'route_no': ['705'], 'platform': ['1']}, 
                               {'edge': ('510', '500', 2), 'route_no': ['706'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },  


    '520': { 'station_name':  { 'ch': '天秀',   
                                'en': 'Tin Sau' },
             'route_data':    [{'edge': ('520', '530', 1.5), 'route_no': ['705'], 'platform': ['1']}, 
                               {'edge': ('520', '510', 1), 'route_no': ['706'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '530': { 'station_name':  { 'ch': '濕地公園',
                                'en': 'Wetland Park' },
             'route_data':    [{'edge': ('530', '540', 1.5), 'route_no': ['705'], 'platform': ['1']}, 
                               {'edge': ('530', '520', 1.5), 'route_no': ['706'], 'platform': ['2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '540': { 'station_name':  { 'ch': '天恒',
                                'en': 'Tin Heng' },
             'route_data':    [{'edge': ('540', '550', 1.5), 'route_no': ['705'], 'platform': ['2']},
                               {'edge': ('540', '530', 1.5), 'route_no': ['706'], 'platform': ['1']}],   
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '550': { 'station_name':  { 'ch': '天逸',
                                'en': 'Tin Yat' },
             'route_data':    [{'edge': ('550', '480', 1.5), 'route_no': ['705', '751', '761P'], 'platform': ['4', '1', '2']}, 
                               {'edge': ('550', '540', 1.5), 'route_no': ['706'], 'platform': ['5']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '560': { 'station_name':  { 'ch': '水邊圍',
                                'en': 'Shui Pin Wai' },
             'route_data':    [{'edge': ('560', '570', 1.5), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('560', '400', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] },


    '570': { 'station_name':  { 'ch': '豐年路',
                                'en': 'Fung Nin Road' },
             'route_data':    [{'edge': ('570', '580', 1), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('570', '560', 1.5), 'route_no': ['761P', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '580': { 'station_name':  { 'ch': '康樂路',
                                'en': 'Hong Lok Road' },
             'route_data':    [{'edge': ('580', '590', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('580', '570', 1), 'route_no': ['761P', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '590': { 'station_name':  { 'ch': '大棠路',
                                'en': 'Tai Tong Road' },
             'route_data':    [{'edge': ('590', '600', 4), 'route_no': ['761P', '615', '610', '614'], 'platform': ['1', '1', '1', '1']},
                               {'edge': ('590', '580', 2), 'route_no': ['761P', '615', '610', '614'], 'platform': ['2', '2', '2', '2']}],
             'platform_data': [{'edge': ('1', '2', 1)}] }, 


    '600': { 'station_name':  { 'ch': '元朗',
                                'en': 'Yuen Long' },
             'route_data':    [{'edge': ('600', '590', 4), 'route_no': ['761P', '615', '610', '614'], 'platform': ['5', '4', '3', '2']},
                               {'edge': ('600', 'YUL', 2), 'route_no': ['WALK'], 'platform': ['0'], 'remarks': { 'ch': '請由 E / G1 出口步行至元朗地鐵站',
                                                                                                                 'en': 'Go to Exit E / G1 to reach Yuen Long Railway Station' }}],
             'platform_data': [{'edge': ('1', '2', 1)},
                               {'edge': ('1', '3', 1)},
                               {'edge': ('1', '4', 1)},
                               {'edge': ('1', '5', 1)},
                               {'edge': ('2', '3', 1)},
                               {'edge': ('2', '4', 1)},
                               {'edge': ('2', '5', 1)},
                               {'edge': ('3', '4', 1)},
                               {'edge': ('3', '5', 1)},
                               {'edge': ('4', '5', 1)}] },
    

    '920': { 'station_name':  { 'ch': '三聖',
                                'en': 'Sam Shing' },
             'route_data':    [{'edge': ('920', '600', 2.5), 'route_no': ['505'], 'platform': ['1']}],
             'platform_data': [] }, 

}


# for key, item in whole_graph_data.items():

#     if not (key.isalpha()):

#         platform_list = []

#         for item_1 in item['route_data']:
#             platform_list = platform_list + item_1['platform']
                    
#         platform_list = list(dict.fromkeys(platform_list))
#         platform_list.sort()
#         result = '\'' + item['station_name']['ch'] + '\': { \'direction_name\': ' + str(platform_list) + ', \'direction_id\': ' + str(platform_list) + ' },'

#         if (len(platform_list) > 0):
#             print(result)
