# CPRSmartGlove
I was researching and prototyping a smart glove for CPR training as a final year bachelor's student.
Project architecture:
The system hardware consists of five main parts:
1.	a fabric-based tactile sensor.
2.	an Arduino Nano RP2040 board (BLE peripheral device).
3.	an Arduino Nano 33 BLE board (BLE server device).
4.	a PC where ”Python” code operates.
5.	LiPo battery 3.7 V

A fabric-based pressure sensor is placed on the palm area of the glove as presented in the Figure 2 below. The Arduino Nano 33 BLE board acts as a BLE server device and Arduino Nano RP2040 board acts as a BLE peripheral device and they are connected using BLE technology. The tactile sensor on the glove is connected to the peripheral device and the device sends a sensor value to the server device continuously, 1 byte of data at a time. Then the server device passes the received data to the PC where the data is analyzed using ”Python” programming language.
![image](https://user-images.githubusercontent.com/62512254/144421783-f68b48df-ea16-496b-8883-839c0665e401.png)
