import React, {useState} from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import SinglePtRouteSearchScreen from './SinglePtRouteSearchScreen';
import SinglePtRouteInfoScreen from './SinglePtRouteInfoScreen'
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import { RouteProvider } from '../RouteProvider';

const RouteSearchStack = createStackNavigator();

const RouteSearchStackScreen = ({navigation}) => {
    return (
        <RouteProvider>
            <RouteSearchStack.Navigator screenOptions={{
                headerStyle:{
                    backgroundColor: '#2E5266FF',
                },
                headerTintColor: '#D3D0CBFF',
            }}>
                <RouteSearchStack.Screen name="SinglePtRouteSearch" component={SinglePtRouteSearchScreen} options={{
                    title: '搜尋目錄',
                    headerLeft: () => (
                        <MaterialCommunityIcons name="menu-open" size={25} color='#D3D0CBFF' onPress={() => navigation.openDrawer()}/>
                    )
                }}/>
                <RouteSearchStack.Screen name="SinglePtRouteInfo" component={SinglePtRouteInfoScreen} options={{title: '過往紀錄'}}/>
            </RouteSearchStack.Navigator>

        </RouteProvider>
    )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
});

export default RouteSearchStackScreen;