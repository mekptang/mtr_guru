import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

const CollectionsListScreen = ({navigation}) => {
    return (
      <View style={styles.container}>
        <Text>Collections List Screen</Text>
        <Button title='Go to Collection' onPress={() => navigation.navigate("Collection")}/>
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

export default CollectionsListScreen