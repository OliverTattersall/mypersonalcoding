import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableWithoutFeedback,TouchableOpacity, Image, SafeAreaView } from 'react-native';

export default function App() {
  console.log('app executed');
  let x = 1;

  const handlePress = (text) =>{console.log(text)}

  return (
    
    <>
    <SafeAreaView style={styles.container}>
      <View style={{
        backgroundColor: 'dodgerblue',
        width: 150,
        height: 70

        }}>

      </View>
    </SafeAreaView>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: Platform.OS === 'android' ? 35 : 0,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
