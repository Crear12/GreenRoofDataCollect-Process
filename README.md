# GreenRoofDataCollect-Process
It's a class project related to Green Roof Project in Rutgers. The project includes collecting data using Arduino&amp;sensors(C), visualization and modeling(python).
# Data Collection
## Hardware
1. Adafruit METRO
2. Capacitive Soil Moisture Sensor V1.2 
3. TMP36 temperature sensor
4. A power bank
5. An 8GB SD card


## Codes
Data collection includes two parts: 
  1. Real-time data collection(PC-based)
  2. Offline data collection(SD card based)
  
1. Real-time data collection
The initial idea is collecting data from sensors to PC directly. OutputTemp.ino works on Arduino to output the temperture based on the eqution: Celsius = (voltage - 0.5) * 100.0, dataAccess_Save.py works on PC to read the output from METRO and write the result into a csv file with current time.

2. Offline data collection
Considering that we are collecting outdoor data and we cannot put our laptop outside all the time, we developped another code to do all the things on Adafruit METRO without a PC. SensorOutput.ino was designed to collect moisture data and temperature data of soil surface consistantly and write the collected data into a txt file and store the file on a SD card.
