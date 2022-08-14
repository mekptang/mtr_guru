import { StyleSheet, Text, View, ScrollView, SafeAreaView, TouchableOpacity } from 'react-native';
import React, { useState, useEffect } from 'react';
import { data } from "../data"
import { useRouteUpdate } from '../RouteProvider'
import RNPickerSelect from 'react-native-picker-select';

const RouteSearchScreen = ({ navigation }) => {
  const [ startRoute, setStartRoute ] = useState('TML');
  const [ startStation, setStartStation ] = useState();
  const [ endRoute, setEndRoute ] = useState('TML');
  const [ endStation, setEndStation ] = useState();

  const [ startStationList, setStartStationList ] = useState(Object.keys(data['TML']));
  const [ endStationList, setEndStationList ] = useState(Object.keys(data['TML']));

  const [ mode, setMode ] = useState(0);

  // const [startDate, setStartDate] = useState(new Date())
  // const [endDate, setEndDate] = useState(new Date())

  useEffect(() => {
    setStartStationList(Object.keys(data[startRoute]))
    setStartStation(Object.keys(data[startRoute])[0])
    // console.log('new Date()')
    // console.log(new Date())
  }, [ startRoute ]);

  useEffect(() => {
    setEndStationList(Object.keys(data[endRoute]))
    setEndStation(Object.keys(data[endRoute])[0])
    // console.log(endStationList)
  }, [ endRoute ]);

  const updateRoute = useRouteUpdate()

  const onSubmit = () => {
    updateRoute({
        "startRouteType":startRoute.split('-')[0].toLowerCase(),
        "start_station_id":startStation,
        "endRouteType":endRoute.split('-')[0].toLowerCase(),
        "dest_station_id":endStation,
        "mode":mode
        // "startDate":startDate,
        // "endDate":endDate
    })
    navigation.navigate("RouteInfo")
  };

  const genStationArray = (endStationList) => {
    let arr = []
    endStationList.map((item) => {
      arr.push({ label: item.toString(), value: item.toString()})
    })

    return arr
  }

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <View style={[styles.picker, {marginTop: 20}]}> 
          <View style={styles.subPicker1}>
            <Text style={styles.textHeader}>旅程資訊</Text>
          </View>

          <View style={styles.subPicker2}>

            <View style={styles.subPicker3}>
              <View style={[styles.subPickerTitle, {height: 30}]}>
                <Text style={[styles.textBody, {fontWeight: 'bold', textDecorationLine: 'underline'}]}>起點 </Text>
              </View>
              <View style={styles.subPickerItem}></View>
            </View>

            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>路線</Text>
              </View>

              <View style={styles.subPickerItem}>
                <RNPickerSelect
                  placeholder={{}}
                  onValueChange={(itemValue, itemIndex) => setStartRoute(itemValue)}
                  items={[
                    {label: '地鐵 - 屯馬線', value: 'TML'},
                    {label: '地鐵 - 東涌線', value: 'TCL'},
                    {label: '輕鐵', value: 'LRT'}
                  ]}
                  style={pickerSelectStyles}
                  value={startRoute}
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
                  onValueChange={(itemValue, itemIndex) => setStartStation(itemValue)}
                  items={genStationArray(startStationList)}
                  style={pickerSelectStyles}
                  value={startStation}
                />
              </View>
            </View>

            <View style={{height: 15}}></View>

            <View style={styles.subPicker3}>
              <View style={[styles.subPickerTitle, {height: 30}]}>
                <Text style={[styles.textBody, {fontWeight: 'bold', textDecorationLine: 'underline'}]}>終點 </Text>
              </View>
              <View style={styles.subPickerItem}></View>
            </View>

            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>路線</Text>
              </View>

              <View style={styles.subPickerItem}>
                <RNPickerSelect
                  placeholder={{}}
                  onValueChange={(itemValue, itemIndex) => setEndRoute(itemValue)}
                  items={[
                    {label: '地鐵 - 屯馬線', value: 'TML'},
                    {label: '地鐵 - 東涌線', value: 'TCL'},
                    {label: '輕鐵', value: 'LRT'}
                  ]}
                  style={pickerSelectStyles}
                  value={endRoute}
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
                  onValueChange={(itemValue, itemIndex) => setEndStation(itemValue)}
                  items={genStationArray(endStationList)}
                  style={pickerSelectStyles}
                  value={endStation}
                />
              </View>
            </View>
          </View>
        </View>

        <View style={styles.picker}>
          <View style={styles.subPicker1}>
            <Text style={styles.textHeader}>路線偏好</Text>
          </View>

          <View style={styles.subPicker2}>
            <View style={styles.subPicker3}>
              <View style={styles.subPickerTitle}>
                <Text style={styles.textBody}>模式</Text>
              </View>

              <View style={styles.subPickerItem}>
                <RNPickerSelect
                  placeholder={{}}
                  onValueChange={(itemValue, itemIndex) => setMode(itemValue)}
                  items={[
                    {label: "最快", value: "1"},
                    {label: "最少轉乘", value: "2"},
                    {label: "最少步行", value: "3"},
                  ]}
                  style={pickerSelectStyles}
                  value={mode}
                />
              </View>
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
    marginVertical: 13,

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
    paddingTop: 13,
    paddingVertical: 15,
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