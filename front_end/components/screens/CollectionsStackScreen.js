import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { createStackNavigator } from '@react-navigation/stack';
import CollectionsListScreen from './CollectionsListScreen'
import CollectionScreen from './CollectionScreen'
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';

const CollectionStack = createStackNavigator();

const CollectionsStackScreen = ({navigation}) => {
    return (
        <CollectionStack.Navigator screenOptions={{
            headerStyle:{
                backgroundColor: '#2E5266FF',
            },
            headerTintColor: '#D3D0CBFF',
        }}>
            <CollectionStack.Screen name="CollectionsList" component={CollectionsListScreen} options={{
                title:'Collections',
                headerLeft: () => (
                    <MaterialCommunityIcons name="menu-open" size={25} color='#D3D0CBFF' onPress={() => navigation.openDrawer()}/>
                )
            }}/>
            <CollectionStack.Screen name="Collection" component={CollectionScreen} />
        </CollectionStack.Navigator>
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

export default CollectionsStackScreen;