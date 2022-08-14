import React, { useState } from 'react'
import { StyleSheet, Button, Pressable, Text, View } from 'react-native'
import DatePicker from 'react-native-date-picker'
import moment from 'moment';

export default ({date, setDate, title}) => {
//   const [date, setDate] = useState(new Date())
  const [open, setOpen] = useState(false)

  return (
    <>
        <View style={styles.container}>
            <Pressable style={styles.datePicker} onPress={() => setOpen(true)}>
                <Text style={styles.dateText}> {moment(date).format('YYYY-MM-DD  hh:mm A')} </Text>
            </Pressable>
            <DatePicker
                modal
                open={open}
                date={date}
                onConfirm={(date) => {
                    setOpen(false)
                    setDate(date)
                }}
                onCancel={() => {
                    setOpen(false)
                }}
            />
        </View>
    </>
  )
}


const styles = StyleSheet.create({

    datePicker: {
        textAlign: 'center',
        justifyContent: 'center',
        height: 40,
        borderColor: '#e6e6fa',

        borderWidth: 1,
        borderRadius: 8,
        borderColor: '#e6e6fa',
        marginLeft: 10,
        marginRight: 10
    },

    dateText: {
        color: '#2f7cf6',
        fontSize: 17,
        textAlign: 'center',
        fontWeight: 'bold'
    },
});
