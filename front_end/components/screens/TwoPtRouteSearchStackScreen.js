import React, {useState} from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import RouteSearchScreen from './TwoPtRouteSearchScreen';
import TwoPtRouteInfoScreen from './TwoPtRouteInfoScreen'
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
                <RouteSearchStack.Screen name="RouteSearch" component={RouteSearchScreen} options={{
                    title: '搜尋目錄',
                    headerLeft: () => (
                        <MaterialCommunityIcons name="menu-open" size={25} color='#D3D0CBFF' onPress={() => navigation.openDrawer()}/>
                    )
                }}/>
                <RouteSearchStack.Screen name="RouteInfo" component={TwoPtRouteInfoScreen} options={{
                    title: '旅程資料',
                }}/>
            </RouteSearchStack.Navigator>

        </RouteProvider>

    )
}

const styles = StyleSheet.create({
    container: {
    width: 370,
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
});

export default RouteSearchStackScreen;