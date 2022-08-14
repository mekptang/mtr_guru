import { StyleSheet, Text, View, Button, ScrollView, SafeAreaView, RefreshControl } from 'react-native';
import React, { useState } from 'react';
import AnimatedLoader from 'react-native-animated-loader';
import { useRoute } from '../RouteProvider'
import { data, MTR_APITranslation, LR_APITranslation } from "../data"
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import ETACard from "../elements/ETACard"


const RouteInfoScreen = ({ navigation }) => {
  const routeInfo = useRoute()
  const [ startPoint, setStartPoint ] = useState()
  const [ endPoint, setEndPoint ] = useState()

  const [ rawData, setRawData ] = useState([])

  const [ totalTravelTime, setTotalTravelTime ] = useState()
  const [ totalWalkTime, setTotalWalkTime ] = useState()
  const [ totalWaitTime, setTotalWaitTime ] = useState()
  const [ totalTotalTrainTime, setTotalTrainTime ] = useState()
  const [ interchange, setInterchange ] = useState()
  const [ pathLength, setPathLength ] = useState()
  const [ pathData, setPathData ] = useState([])

  const [visible, setVisible] = useState(false);

  const [refreshing, setRefreshing] = React.useState(false);

  

  const onRefresh = React.useCallback(() => {
    setRefreshing(true)
    const endpoint = "route"
    const body = {
      "start_station_id": "390",
      "dest_station_id": "NAC",
      "mode": "1"
    }
    fetch(`http://3.83.218.157:5000/${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    })
    .then(response => { 
      console.log(response.status); 
      if (response.status == 200){
        return response
      }else{
        return null
      }
    })
    .then(response => {
      if (response){
        return response.json()
      }  
      else{
        return response.text()
      }
    })
    .then(data => {
      // const path_data = Object.assign(...Object.keys(data[0]['path_data'][0]).map( key =>
      //   ({ [key]: data[0]['path_data'].map( o => o[key] ) })
      // ));
      setRawData(data)
      setStartPoint(routeInfo['start_station_id'])
      setEndPoint(routeInfo['dest_station_id'])

      setTotalTravelTime(data[0]["total_travel_time"])
      setTotalWalkTime(data[0]["total_walk_time"])
      setTotalWaitTime(data[0]["total_wait_time"])
      setTotalTrainTime(data[0]["total_train_time"])
      setInterchange(data[0]['interchange'])
      setPathLength(data[0]['path_length'])
      setPathData(data[0]['path_data'])
      console.log(data)
    }).then(() => setRefreshing(false));
  }, [])

  

  React.useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      setVisible(true)
      const endpoint = "route"
      
      // const body = {
      //   "start_station_id": routeInfo['startRouteType'] == "mtr" ? MTR_APITranslation[routeInfo['start_station_id']]:LR_APITranslation[routeInfo['start_station_id']],
      //   "dest_station_id": routeInfo['endRouteType'] == "mtr" ? MTR_APITranslation[routeInfo['dest_station_id']]:LR_APITranslation[routeInfo['dest_station_id']],
      //   "mode": routeInfo['mode']
      // }

      const body = {
        "start_station_id": "390",
        "dest_station_id": "NAC",
        "mode": "1"
      }

      // console.log(body)
      console.log("refreashing")
      // fetch(`http://3.83.218.157:5000/${endpoint}`, {
      fetch(`http://3.83.218.157:5000/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
      })
      .then(response => { 
        console.log(response.status); 
        if (response.status == 200){
          return response
        }else{
          return null
        }
      })
      .then(response => {
        if (response){
          return response.json()
        }  
        else{
          return response.text()
        }
      })
      .then(data => {
        // const path_data = Object.assign(...Object.keys(data[0]['path_data'][0]).map( key =>
        //   ({ [key]: data[0]['path_data'].map( o => o[key] ) })
        // ));
        
        setRawData(data)
        setStartPoint(routeInfo['start_station_id'])
        setEndPoint(routeInfo['dest_station_id'])

        setTotalTravelTime(data[0]["total_travel_time"])
        setTotalWalkTime(data[0]["total_walk_time"])
        setTotalWaitTime(data[0]["total_wait_time"])
        setTotalTrainTime(data[0]["total_train_time"])
        setInterchange(data[0]['interchange'])
        setPathLength(data[0]['path_length'])
        setPathData(data[0]['path_data'])
        
        console.log(data)
      }).then(() => setVisible(false));
    });

    // Return the function to unsubscribe from the event so it gets removed on unmount
    return unsubscribe;
  }, [navigation]);
    return (
      <SafeAreaView style={styles.container}>
        
        <AnimatedLoader
          visible={visible}
          overlayColor="rgba(255,255,255,0.6)"
          source={require("../../assets/9997-infinity-loader.json")}
          animationStyle={styles.lottie}
          speed={1}>
            <Text>Loading...</Text>
        </AnimatedLoader>
        { 
          visible ? null :
            <>
              <View style={styles.headerStyle}>
                <View style={styles.headerContainerStyle}>
                  <Text style={styles.headerTextStyle}>{startPoint}</Text>
                  <MaterialCommunityIcons name="arrow-right" style={styles.arrowStyle} />
                  <Text style={styles.headerTextStyle}>{endPoint}</Text>
                </View>
                <View style={styles.etaAndInterChangeContainerStyle}>
                  <Text style={styles.etaTextStyle}>預計全程時間</Text>
                  <Text style={styles.etaTextStyle}>~{totalTravelTime} 分鐘</Text>
                </View>
                <View style={styles.etaAndInterChangeContainerStyle}>
                  <Text style={styles.interChangeTextStyle}>轉乘次數</Text>
                  <Text style={styles.interChangeTextStyle}>{interchange}</Text>
                </View>
              </View>
              <ScrollView contentContainerStyle={styles.scrollView}
                refreshControl={
                  <RefreshControl
                    refreshing={refreshing}
                    onRefresh={onRefresh}
                  />
              }>
                <View style={styles.containerRoute}>
                  {
                    pathData.map((blk, index) => {
                      return <ETACard 
                        start_station={blk.start_station} 
                        start_station_type={blk.start_station_type} 
                        end_station={blk.end_station}
                        end_station_type={blk.end_station_type}
                        transit_time={blk.transit_time}
                        wait_time={blk.wait_time}
                        eta_delay_time={blk.eta_delay_time}
                        route={blk.route}
                        eta_list={blk.eta_list}
                        description={blk.description}
                        path_id={blk.path_id}
                        path_length={pathLength}
                        key={index}
                      />
                    })
                  }
                </View>
              </ScrollView>
            </>
        }
      </SafeAreaView>
    )
}

const styles = StyleSheet.create({

  container: {
    width: '100%',
    backgroundColor: 'white',
    justifyContent: 'center',
    flex: 1,
  },

  containerRoute: {
    width: '100%',
    flex: 1,
    backgroundColor: 'white',
    borderColor: 'black',
    alignItems: 'stretch',
    justifyContent: 'center',
    alignItems: 'center',
  },

  headerStyle:{
    
  },

  headerTextStyle:{
    fontSize: 22,
    margin: 12,
    fontWeight: "bold",
  },

  arrowStyle:{
    fontSize: 35,
    margin: 5,
  },

  headerContainerStyle:{
    flexDirection: 'row',
    justifyContent: 'space-between',
    backgroundColor: 'lightblue',
    paddingHorizontal: 12,
    paddingVertical: 10,
    borderBottomWidth: 2,
  },

  etaAndInterChangeContainerStyle: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    backgroundColor: 'ghostwhite',
    paddingHorizontal: 23,
    paddingVertical: 8,
  },

  etaTextStyle: {
    fontSize: 18,
    paddingTop: 5,
  },

  interChangeTextStyle: {
    fontSize: 18,
  },

  lottie: {
    width: 100,
    height: 100,
  },

  scrollView: {
    justifyContent: 'center',
    backgroundColor: 'whitesmoke',
  },

});

export default RouteInfoScreen;

// {
//   pathData.map((blk, index) => {
//     return (
//       <Text key={index}>
//         <Text>start_station: {blk.start_station}</Text>{"\n"}
//         <Text>start_station_type: {blk.start_station_type}</Text>{"\n"}
//         <Text>end_station: {blk.end_station}</Text>{"\n"}
//         <Text>end_station_type: {blk.end_station_type}</Text>{"\n"}
//         <Text>transit_time: {blk.transit_time}</Text>{"\n"}
//         <Text>wait_time: {blk.wait_time}</Text>{"\n"}
//         <Text>eta_delay_time: {blk.eta_delay_time}</Text>{"\n"}
//         <Text>route: {blk.route}</Text>{"\n"}
//         {blk.eta_list ? blk.eta_list.map((eta,idx) => {
//           return(
//             <Text key={idx}>
//               <Text>route_no: {eta.route_no}</Text>{"\n"}
//               <Text>dest_station: {eta.dest_station}</Text>{"\n"}
//               <Text>platform_id: {eta.platform_id}</Text>{"\n"}
//               <Text>ttnt_eta: {eta.ttnt_eta}</Text>{"\n"}
//             </Text>
//           )
//         }):null}

//         {
//           blk.description ? blk.description : null
//         }

//       </Text>
//     );
//   })
// }