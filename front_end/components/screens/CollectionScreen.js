import { StyleSheet, Text, View, Button } from 'react-native';
import React from 'react';

const CollectionScreen = ({navigation}) => {
    return (
      <View style={styles.container}>
        <Text>Collection Screen</Text>
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

export default CollectionScreen