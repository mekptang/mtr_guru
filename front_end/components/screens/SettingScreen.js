import { StyleSheet, Text, View, Button } from 'react-native';
import React from 'react';

const SettingScreen = ({navigation}) => {
    return (
      <View style={styles.container}>
        <Text>Setting Screen</Text>
      </View>
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

export default SettingScreen