import React, { useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import MainTabScreen from './components/screens/MainTabScreen'
import CollectionScreen from './components/screens/CollectionScreen'
import AboutScreen from './components/screens/AboutScreen'
import SettingScreen from './components/screens/SettingScreen'
import {LogBox} from "react-native";

LogBox.ignoreLogs(["exported from 'deprecated-react-native-prop-types'.", ])
const Drawer = createDrawerNavigator();

export default function App() {

  return (
      <NavigationContainer>
        <Drawer.Navigator initialRouteName='Home' screenOptions={{headerShown: false}}>
          <Drawer.Screen name="Home" component={MainTabScreen} />
          <Drawer.Screen name="Setting" component={SettingScreen} />
          <Drawer.Screen name="About" component={AboutScreen} />
        </Drawer.Navigator>
      </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
