import { StyleSheet, Text, View, Button, ScrollView, SafeAreaView, Image } from 'react-native';
import Dash from 'react-native-dash';
import React, { useState } from 'react';


const etaListTranspose = (etaList) => {
    if (etaList){
        if (etaList.length > 0){
            const path_data = Object.assign(...Object.keys(etaList[0]).map( key =>
                ({ [key]: etaList.map( o => o[key] ) })
            ));
            return path_data
        }
    }
}

// <MaterialCommunityIcons name="arrow-down" size={50} />

const ETACard = ({start_station, start_station_type, end_station, end_station_type, transit_time, wait_time, eta_delay_time, route, eta_list, description, path_id, path_length}) => {

    let newEta = etaListTranspose(eta_list)

    return (
      <View style={styles.journeyCard}>
        {
          (!description || path_id == '1') ? 
            <View style={[styles.startStation, path_id == '1' ? styles.stationBorder : null]}>
              { start_station_type == 'hr' ? <Image style={styles.trainLogo} source={require('../../assets/mtr.jpg')} /> : <Image style={styles.trainLogo} source={require('../../assets/railway.jpeg')} /> }
              <View style={styles.startStationFontWrapper1}>
              </View>
              <View style={[styles.startStationFontWrapper2, path_id == '1' ? styles.StationFontWrapper3 : null]}>
                <Text style={styles.startStationFont}>{start_station}</Text>
              </View>
            </View>
          :
            null
        }

        {
          description ? 
            <View style={[styles.tripInfo, {height: 90}]}>
              <View style={styles.direction}>
                <Dash dashGap={5} dashLength={10} dashThickness={7} dashColor={'#D8D8D8'} style={styles.dashLine}></Dash>
              </View>

              <View style={styles.etaWalk}>
                <View style={styles.tripTime}>
                  <View style={styles.tripTimeItem}>
                    <Text style={styles.tripTimeText}>步行:   </Text> 
                  </View>
                  <View style={styles.tripTimeItem}>
                    <Text style={styles.tripTimeText}>{transit_time} 分</Text>
                  </View>
                </View>
                <View style={styles.description}>
                  <Text style={styles.descriptionText}>{description}</Text> 
                </View>
              </View>
            </View>
          
          :

            <View style={styles.tripInfo}>
              <View style={styles.direction} >
                <View style={[styles.leftDirection, route == 'TML' ? {borderColor: 'brown'} : route == 'TCL' ? {borderColor: 'orange'} : {borderColor: 'goldenrod'}]}></View>
                <View style={styles.rightDirection}></View>
              </View>

              <View style={styles.etaTrain}>
                <View style={styles.tripTime}>
                  <View style={styles.tripTimeItem}>
                    <Text style={styles.tripTimeText}>車程:   </Text>
                    <Text style={styles.tripTimeText}>侯車時間:   </Text> 
                    <Text style={[styles.tripTimeText, {paddingBottom: 20}]}>過往延誤:   </Text> 
                  </View>
                  <View style={styles.tripTimeItem}>
                    <Text style={styles.tripTimeText}>{transit_time} 分</Text> 
                    <Text style={styles.tripTimeText}>{wait_time} 分</Text>
                    <Text style={[styles.tripTimeText, {paddingBottom: 20}]}>{eta_delay_time} 分</Text>
                  </View>
                </View>
                  
                {
                  !eta_list ? null: (eta_list.length == 0) ? null :   

                    <View style={styles.etaList}>
                      <View style={styles.etaListRoute}>
                        <View style={styles.etaTitle}>
                          <Text style={styles.etaTitleText}>路線</Text>
                        </View>
                        {newEta.route_no.map((route_no, index) => {
                          return <Text style={styles.etaText} key={index} >{route_no}</Text>
                        })}
                      </View>

                      <View style={styles.etaListDirection}>
                        <View style={styles.etaTitle}>
                          <Text style={styles.etaTitleText}>方向</Text>
                        </View>
                        {newEta.dest_station.map((dest_station, index) => {
                          return <Text style={styles.etaText} key={index} >{dest_station}</Text>
                        })}
                      </View>
                                    
                      <View style={styles.etaListPlatform}>
                        <View style={styles.etaTitle}>
                          <Text style={styles.etaTitleText}>月台</Text>
                        </View>
                        {newEta.platform_id.map((platform_id, index) => {
                          return <Text style={styles.etaText} key={index} >{platform_id}</Text>
                        })}
                      </View>
                                        
                      <View style={styles.etaListTime}>
                        <View style={styles.etaTitle}>
                          <Text style={styles.etaTitleText}>到站時間</Text>
                        </View>
                        {newEta.ttnt_eta.map((ttnt_eta, index) => {
                          return <Text style={styles.etaText} key={index} >{ttnt_eta} 分</Text>
                        })}
                      </View>
                    </View>
                }
              </View>
            </View>
        }

        {
          (!description || path_id == path_length) ? 
            <View style={[styles.endStation, path_id == path_length ? styles.stationBorder : null]}>
              { end_station_type == 'hr' ? <Image style={styles.trainLogo} source={require('../../assets/mtr.jpg')} /> : <Image style={styles.trainLogo} source={require('../../assets/railway.jpeg')} /> }
              <View style={styles.endStationFontWrapper1}></View>
              <View style={styles.endStationFontWrapper2}>
                <Text style={styles.endStationFont}>{end_station}</Text>
              </View>
            </View>
          :
            null
        }  
      </View>
    )
}

const styles = StyleSheet.create({

      // Whole card
      journeyCard: {
        backgroundColor: 'white',
        width: 360,
        paddingLeft: 15,
        paddingRight: 15,
        paddingTop: 5,
      },
      

      // 1st + 3rd part of the Card
      startStation: {
        flexDirection: 'row',
        alignItems: 'flex-end',
        justifyContent: 'center',
        width: '100%',
        
        paddingVertical: 5,
        borderTopWidth: 1,
        borderColor: '#b4b4b4',
      },

      startStationFontWrapper1: {

      },

      startStationFontWrapper2: {
        marginLeft: 15,
        width: '80%',
        height: 60,
      },

      stationBorder: {
        borderColor: 'white',
      },

      startStationFont: {
        fontWeight: "bold",
        fontSize: 18,
        paddingVertical: 25,
      },

      endStation: {
        flexDirection: 'row',
        alignItems: 'stretch',
        justifyContent: 'center',
        width: '100%',
        
        paddingVertical: 5,
        borderBottomWidth: 1,
        borderColor: '#b4b4b4',
      },

      endStationFontWrapper1: {

      },

      endStationFontWrapper2: {
        marginLeft: 15,
        width: '80%',
        height: 60,
      },

      endStationFont: {
        fontWeight: "bold",
        fontSize: 18,
        marginVertical: 15,
      },

      trainLogo: {
        width: 50,
        height: 50,
      },

      // 2nd Part of the card
      tripInfo: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        width: '100%',

        marginVertical: 7,
      },

      direction: {
        width: '18%',
        flexDirection: 'row',
      },

      leftDirection: {
        width: '50%',
        borderRightWidth: 7,
      },

      rightDirection: {
        width: '50%',
      },

      dashLine: {
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        flex: 1,
        marginRight: 8,
      },

      etaTrain:{
        flexDirection: 'column',
        width: '81%',
        paddingHorizontal: 5,
        paddingVertical: 5,
        backgroundColor: 'lavender',
        borderRadius: 8,
      },

      etaWalk:{
        flexDirection: 'column',
        width: '81%',
        paddingHorizontal: 5,
        paddingVertical: 5,
        backgroundColor: '#e3e3e3',
        borderRadius: 8,

      },

      tripTime:{
        flexDirection: 'row',
        justifyContent: 'flex-end',
        alignItems: 'stretch',
      },

      tripTimeItem:{
        alignItems: 'flex-end',
      },

      tripTimeText:{
        fontSize: 15,
        marginVertical: 3,
      },

      etaList:{
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'stretch',
        marginVertical: 0,
      },

      etaListRoute:{
        marginVertical: 3,
        borderColor: 'black',
        flexDirection: 'column',
        justifyContent: 'space-between',

        width: '25%',
      },

      etaListDirection:{
        marginVertical: 3,
        borderColor: 'black',
        flexDirection: 'column',
        justifyContent: 'space-between',
        
        width: '27%',
      },

      etaListPlatform:{
        marginVertical: 3,
        borderColor: 'black',
        flexDirection: 'column',
        justifyContent: 'space-between',
        
        width: '20%',
      },

      etaListTime:{
        marginVertical: 3,
        borderColor: 'black',
        flexDirection: 'column',
        justifyContent: 'space-between',
        
        width: '28%',
      },

      etaTitle: {
        borderBottomWidth: 2,
      },

      etaTitleText:{
        fontWeight: 'bold',
        textAlign: 'center',
        fontSize: 15,
        marginVertical: 5,
      },

      etaContent:{

      },

      etaText:{
        textAlign: 'center',
        marginVertical: 5,
        fontSize: 15,
      },

      description: {
        marginVertical: 20,
        alignItems: 'center',
        justifyContent: 'center',
      },

      descriptionText:{
        fontSize: 15,
      },

});

export default ETACard;
