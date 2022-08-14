import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import TwoPtRouteSearchStackScreen from './TwoPtRouteSearchStackScreen'
import SinglePtRouteSearchStackScreen from './SinglePtRouteSearchStackScreen'
import CollectionsStackScreen from './CollectionsStackScreen'

const Tab = createMaterialBottomTabNavigator();

const MainTabSreen = () => {
    return (
        <Tab.Navigator
            initialRouteName="TwoPtRouteSearchStackScreen"
            activeColor="#D3D0CBFF"
            barStyle={{ backgroundColor: '#2E5266FF' }}
        >
            <Tab.Screen
                name="TwoPtRouteSearchStackScreen"
                component={TwoPtRouteSearchStackScreen}
                options={{
                    tabBarLabel: '行程指引',
                    tabBarIcon: ({ color }) => (
                        <MaterialCommunityIcons name="magnify" color={color} size={25} />
                    ),
                }}
            />
            <Tab.Screen
                name="SinglePtRouteSearchStackScreen"
                component={SinglePtRouteSearchStackScreen}
                options={{
                    tabBarLabel: '過往到站時間',
                    tabBarIcon: ({ color }) => (
                        <MaterialCommunityIcons name="history" color={color} size={26} />
                    ),
                }}
            />
            {/* <Tab.Screen
                name="CollectionsStackScreen"
                component={CollectionsStackScreen}
                options={{
                    tabBarLabel: 'Collections',
                    tabBarIcon: ({ color }) => (
                        <MaterialCommunityIcons name="bookmark-box-multiple" color={color} size={26} />
                    ),
                }}
            /> */}
        </Tab.Navigator>
    );
}

export default MainTabSreen;