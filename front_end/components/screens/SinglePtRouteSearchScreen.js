import { StyleSheet, Text, View, ScrollView, SafeAreaView, TouchableOpacity } from 'react-native';
import React, { useState, useEffect, useLayoutEffect } from 'react';

import { data } from '../data'
import { useRouteUpdate } from '../RouteProvider'
import RNPickerSelect from 'react-native-picker-select';
import DatePicker from '../DatePicker'


const RouteSearchScreen = ({ navigation }) => {
  
  const [ singleRoute, setSingleRoute ] = useState('TML');
  const [ singleStation, setSingleStation ] = useState(Object.keys(data['TML'])[0]);
  const [ singleStationList, setSingleStationList ] = useState(Object.keys(data['TML']));

  const [ startDate, setStartDate ] = useState(new Date())
  const [ endDate, setEndDate ] = useState(new Date())

  const [ platformID, setPlatformID ] = useState(1)
  const [ direction, setDirection ] = useState('up')
  const [ graphID, setGraphID ] = useState('p_hr_1a')
  const [ isMTR, setIsMTR ] = useState(true)

  
  useLayoutEffect(() => {
    setSingleStation(Object.keys(data[singleRoute])[0])
    setSingleStationList(Object.keys(data[singleRoute]))

    if (singleRoute != 'LRT'){
      setIsMTR(true)
    }
    else {
      setIsMTR(false)
    }
  }, [ singleRoute ]);


  const updateRoute = useRouteUpdate()

  const onSubmit = () => {

    updateRoute({
      'singleRoute': singleRoute,
      'singleStation': singleStation,
      'startDate': startDate,
      'endDate': endDate,
      'platformID': platformID,
      'direction': direction,
      'graphID': graphID,
      'isMTR': isMTR
    })

    navigation.navigate('SinglePtRouteInfo')

  };

  const genStationArray = (singleStationList) => {
    let arr = []

    singleStationList.map((item) => {
      arr.push({ label: item.toString(), value: item.toString()})
    })
    return arr
  }

  const genDirectionArray = (Station) => {
    let arr = []
    let direction_name = []
    let direction_id = []
    let length = 0

    if (data[singleRoute][singleStation] != undefined) {
      direction_name = data[singleRoute][singleStation]['direction_name']
      direction_id = data[singleRoute][singleStation]['direction_id']
      length = direction_name.length
    }
    else {
      direction_name = data[singleRoute][Object.keys(data[singleRoute])[0]]['direction_name']
      direction_id = data[singleRoute][Object.keys(data[singleRoute])[0]]['direction_id']
      length = direction_name.length
    }

    for (let i = 0; i < length ; i++) {
      arr.push({ label: direction_name[i].toString(), value: direction_id[i].toString()})
    }
    
    return arr
  }

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <View style={[styles.picker, {marginTop: 20}]}>
          <View style={styles.subPicker1}>
            <Text style={styles.textHeader}>地點</Text>
          </View>

          <View style={styles.subPicker2}>
            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>路線</Text>
              </View>

              <View style={styles.subPickerItem}>
                <RNPickerSelect
                  placeholder={{}}
                  onValueChange={(itemValue, itemIndex) => setSingleRoute(itemValue)}
                  items={[
                    {label: '地鐵 - 屯馬線', value: 'TML'},
                    {label: '地鐵 - 東涌線', value: 'TCL'},
                    {label: '輕鐵', value: 'LRT'}
                  ]}
                  style={pickerSelectStyles}
                  value={singleRoute}
                />
              </View>
            </View>
          
            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>車站</Text>
              </View>

              <View style={styles.subPickerItem}>
                <RNPickerSelect
                  placeholder={{}}
                  onValueChange={(itemValue, itemIndex) => setSingleStation(itemValue)}
                  items={genStationArray(singleStationList)}
                  style={pickerSelectStyles}
                  value={singleStation}
                />
              </View>
            </View>
            
            { 
              isMTR ? 
                <View style={styles.subPicker3}>
                  <View style={styles.subPickerTitle}>
                    <Text style={styles.textBody}>方向</Text>
                  </View>

                  <View style={styles.subPickerItem}>
                    <RNPickerSelect
                      placeholder={{}}
                      onValueChange={(itemValue, itemIndex) => setDirection(itemValue)}
                      items={genDirectionArray(singleStation)}
                      style={pickerSelectStyles}
                      value={direction}
                    />
                  </View>
                </View>
              
              :

                <View style={styles.subPicker3}>
                  <View style={styles.subPickerTitle}>
                    <Text style={styles.textBody}>月台</Text>
                  </View>

                  <View style={styles.subPickerItem}>
                    <RNPickerSelect
                      placeholder={{}}
                      onValueChange={(itemValue, itemIndex) => setPlatformID(itemValue)}
                      items={genDirectionArray(singleStation)}
                      style={pickerSelectStyles}
                      value={platformID}
                    />
                  </View>
                </View>
            }
          </View>
        </View>

        <View style={styles.picker}>
          <View style={styles.subPicker1}>
            <Text style={styles.textHeader}>時間</Text>
          </View>

          <View style={styles.subPicker2}>
            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>開始</Text>
              </View>

              <View style={styles.subPickerItem}>
                <DatePicker date={startDate} setDate={setStartDate} style={styles.subPickerItem}/>
              </View>
            </View>

            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>結束</Text>
              </View>

              <View style={styles.subPickerItem}>
                <DatePicker date={endDate} setDate={setEndDate} style={styles.subPickerItem}/>
              </View>
            </View>
          </View>
        </View>
        
        <View style={styles.picker}>
          <View style={styles.subPicker1}>
            <Text style={styles.textHeader}>過往紀錄</Text>
          </View>

          <View style={styles.subPicker2}>
            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>類別</Text>
              </View>
            
              { 
                isMTR ? 
                  <View style={styles.subPickerItem}>
                    <RNPickerSelect
                      placeholder={{}}
                      onValueChange={(itemValue, itemIndex) => setGraphID(itemValue)}
                      items={[
                        {label: '候車時間', value: 'p_hr_1a'},
                        {label: '班次密度', value: 'p_hr_1b'},
                        {label: '候車時間延誤', value: 'p_hr_1c'}
                      ]}
                      style={pickerSelectStyles}
                    /> 
                  </View>

                :

                  <View style={styles.subPickerItem}>
                    <RNPickerSelect
                      placeholder={{}}
                      onValueChange={(itemValue, itemIndex) => setGraphID(itemValue)}
                      items={[
                        {label: '候車時間', value: 'p_lr_1a'},
                        {label: '班次密度', value: 'p_lr_1b'},
                        {label: '班次延誤', value: 'p_lr_1c'},
                      ]}
                      style={pickerSelectStyles}
                    />
                  </View>
              }
            </View>
          </View>
        </View>
      </ScrollView>

      <View style={styles.countContainer}>
        <TouchableOpacity
          style={styles.searchButton}
          onPress={onSubmit}
        >
          <Text style={styles.buttonText}>立即搜尋!</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({

  container: {
    paddingTop: 12,
    flex: 1,
    backgroundColor: '#fff',
    width: '100%',
  },
  
  picker: {
    borderRadius: 12,
    backgroundColor: 'white',
    flex: 1,
    marginHorizontal: 20,
    marginVertical: 15,

    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.5,
    shadowRadius: 2, 
  },

  subPicker1: {
    backgroundColor: '#D8EAFA',
    flexDirection: 'row',
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
    paddingVertical: 12,
    paddingHorizontal: 15,
  },

  subPicker2: {
    paddingTop: 10,
    paddingVertical: 10,
    paddingHorizontal: 10,
  },

  subPicker3: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginVertical: 2.5,
  },

  subPickerTitle: {
    width: '20%',
    alignItems: 'center',
    justifyContent: 'center',
    height: 40,
  },

  subPickerItem: {
    width: '80%',
  },

  textHeader: {
    textAlign: 'left',
    fontWeight: 'bold',
    fontStyle: 'italic',
    fontSize: 20,
  },

  textBody:{
    textAlign: 'center',
    fontSize: 18,
  },

  searchButton:{
    padding: 20,
    marginBottom: 10,
    width: '70%',
    alignItems: 'center',
    backgroundColor: '#d8d9fa',
    borderRadius: 8,

    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.5,
    shadowRadius: 2, 
  },

  buttonText: {
    fontSize: 18,
  },
  
  countContainer: {
    alignItems: 'center',
    padding: 10
  }
  
});

const pickerSelectStyles = StyleSheet.create({

  inputIOS: {
    textAlign: 'center',
    color: '#2f7cf6',
    fontSize: 18,
    fontWeight: 'bold',
    height: 40,
    paddingTop: 1.2,

    borderWidth: 1,
    borderRadius: 8,
    borderColor: '#e6e6fa',
    marginLeft: 10,
    marginRight: 10
  },

  inputAndroid: {
    textAlign: 'center',
    color: '#2f7cf6',
    fontSize: 18,
    fontWeight: 'bold',
    height: 40,
  }

});

export default RouteSearchScreen;