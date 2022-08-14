import { StyleSheet, Text, View, Button, Dimensions, processColor } from 'react-native';
import React, { useState } from 'react';
import { useRoute } from '../RouteProvider';
// import * as ScreenOrientation from 'expo-screen-orientation';
import { data, MTR_APITranslation, LR_APITranslation } from "../data"
import moment from 'moment'
import { LineChart, BarChart } from 'react-native-charts-wrapper';

// import {
//   LineChart,
//   BarChart,
//   PieChart,
//   ProgressChart,
//   ContributionGraph,
//   StackedBarChart
// } from "react-native-chart-kit";

// body: JSON.stringify({
//   "graph": "p_hr_1c",
//   "start_station": "TML-TKW",
//   "direction": "up",
//   "start_time": "2022-04-22 17:15",
//   "end_time": "2022-04-22 18:15" 
// })


const RouteInfoScreen = ({ navigation }) => {
  const routeInfo = useRoute()
  const [ graphData, setGraphData ] = useState(null)
  const [ xAxis, setXAxis ] = useState()

  React.useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      const endpoint = routeInfo['isMTR'] ? "hr" : "lr"
      const body = routeInfo['isMTR'] ? 
      {
        graph: routeInfo['graphID'],
        start_station_id: routeInfo['singleRoute'].concat('-', MTR_APITranslation[routeInfo['singleStation']]),
        direction: routeInfo['direction'],
        start_time: moment(routeInfo['startDate']).format('YYYY-MM-DD HH:mm:ss'),
        end_time: moment(routeInfo['endDate']).format('YYYY-MM-DD HH:mm:ss')
      }:{
        graph: routeInfo['graphID'],
        start_station_id: LR_APITranslation[routeInfo['singleStation']],
        platform_id: routeInfo['platformID'],
        start_time: moment(routeInfo['startDate']).format('YYYY-MM-DD HH:mm:ss'),
        end_time: moment(routeInfo['endDate']).format('YYYY-MM-DD HH:mm:ss')
      }
      console.log(body)
      
      fetch(`http://3.83.218.157:5000/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
      })
      .then(response => response.json())
      .then(data => {
        if (routeInfo['graphID'] == 'p_hr_1a'){
          for (let i = 0; i < data['dataSets'].length; i++) {
            data['dataSets'][i]['config'] = {
              mode: 'CUBIC_BEZIER',
              drawCubicIntensity: 0.1,
              circleRadius: 3,
              drawValues: false,
              drawFilled: false,
              fillAlpha: 45,
              drawVerticalHighlightIndicator: true,
              drawHorizontalHighlightIndicator: false,
              highlightLineWidth: 1,
              lineWidth: 2,
            }
            for (let j = 0; j < data['dataSets'][i]['values'].length; j++) {
              data['dataSets'][i]['values'][j]['x'] = moment(data['dataSets'][i]['values'][j]['x']).valueOf()
            }
          }
          setXAxis({
            valueFormatter: 'date',
            valueFormatterPattern: 'YYYY-MM-dd HH:mm:ss',
            position: 'BOTTOM',
            labelRotationAngle: 50
          })
          setGraphData(data)
        }
        else if (routeInfo['graphID'] == 'p_hr_1b'){
          for (let i = 0; i < data['dataSets'].length; i++) {
            data['dataSets'][i]['config'] = {
              color: processColor('teal'),
              barShadowColor: processColor('lightgrey'),
              highlightAlpha: 90,
              highlightColor: processColor('red'),
            }
          }
          setXAxis(data['xAxis'])
          setGraphData(data)
        }
        else if (routeInfo['graphID'] == 'p_hr_1c'){
          for (let i = 0; i < data['dataSets'].length; i++) {
            data['dataSets'][i]['config'] = {
              drawCubicIntensity: 0.1,
              circleRadius: 3.5,
              drawValues: false,
              drawFilled: false,
              fillAlpha: 45,
              drawVerticalHighlightIndicator: true,
              drawHorizontalHighlightIndicator: false,
              highlightLineWidth: 1,
              lineWidth: 2,
            }
            for (let j = 0; j < data['dataSets'][i]['values'].length; j++) {
              data['dataSets'][i]['values'][j]['x'] = moment(data['dataSets'][i]['values'][j]['x']).valueOf()
            }
          }
          setXAxis({
            valueFormatter: 'date',
            valueFormatterPattern: 'YYYY-MM-dd HH:mm:ss',
            position: 'BOTTOM',
            labelRotationAngle: 50
          })
          setGraphData(data)
        }
      })

    });

    // Return the function to unsubscribe from the event so it gets removed on unmount
    return unsubscribe
  }, [navigation]);
  console.log(routeInfo['graphID'])
  if (routeInfo['graphID'] == 'p_hr_1a'){
    console.log(graphData)
    return (
      <View style={{flex: 1}}>
        <View style={styles.container}>
          { graphData ? <LineChart style={styles.chart} data={ graphData } xAxis={xAxis}/>:<Text>Loading LineChart</Text> }
        </View>
      </View>
    )
  } 
  else if (routeInfo['graphID'] == 'p_hr_1b'){
    return (
      <View style={{flex: 1}}>
        <View style={styles.container}>
          { graphData? <BarChart style={styles.chart} data={ graphData } xAxis={xAxis}/>:<Text>Loading BarChart</Text> }
        </View>
      </View>
    )
  } 
  else if (routeInfo['graphID'] == 'p_hr_1c'){
    return (
      <View style={{flex: 1}}>
        <View style={styles.container}>
          { graphData ? <LineChart style={styles.chart} data={ graphData } xAxis={xAxis}/>:<Text>Loading LineChart</Text> }
        </View>
      </View>
    )
  }

}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF'
  },
  chart: {
    flex: 1
  },
  font:{
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: 18,
    marginTop: 0,
    width: 200,
    backgroundColor: 'yellow',
  }
});
export default RouteInfoScreen;