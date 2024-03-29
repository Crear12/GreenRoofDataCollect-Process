# GreenRoofDataCollect-Process
It's a class project related to Green Roof Project in Rutgers. The project includes collecting data using Arduino&amp;sensors(C), visualization and modeling(python).
# Data Collection
## Hardware
### 1. Adafruit METRO
Adafruit METRO 328 was used for data collection and writing. (Adruino IDE is required)
### 2. Capacitive Soil Moisture Sensor V1.2 
This moisture sensor was used to read and collect moisture data. A pre-calibration is required. The detailed operation is 1.Put it in dry air and record the voltage for 0%; 2. Put it into water and record the voltage for 100%. 3. Divide the difference between two voltage into 100.
### 3. TMP36 temperature sensor
TMP36 was used to collect temperature data and the equation was provided: Celsius = (voltage - 0.5) * 100.0.
### 4. A power bank
A power bank was used to power the whole data collection system.
### 5. An 8GB SD card
An 8GB SD card was used to store the collected data.

## Procedures
### Real-time Data Collection System
Sensors to MCU:
1. Connect the MCU and the Sensors

Use A0-A4 for data receiving. For example, 2 sensors were used in this project. So use A0 to read data from moisture sensor and use A1 to read temperature sensor.

2. Make the MCU Read the Signal(Voltage) from Sensors

Initiate the MCU and data receiving pin to read the signal from sensors. 

3. Calibrate the Sensors by Calculating the Real Data and the Signal

The moisture sensor requires calibration. Firstly, read and record the voltage from dry air as 0% humidity. Secondly, read and record the voltage from water as 100% humidity. After getting both boundaries, more accurate levels can be divided.

4. Transform the Signal into Information(Temperature(Celsius) and Humidity(Percentage))

Use equation to automatically calculate the temperature and moisture based on the voltages.

5. Output the Information

MCU to PC:
1. Connect the MCU and PC

Use a micro-USB to USB cable to connect the MCU to any PC USB port. Use Arduino IDE to check the connected port ID.

2. Make the PC Read the Output of MCU

Use pip install pyserial or conda install pyserial to install the serial module for python. Use serial.Serial(‘{Port_ID}’,9600).readline().decode(‘utf-8’) to read the data from MCU through python.

3. Store the Data & Process

Use csv module to write the data into Comma-separated values(csv) file, set up sharing folder for data transferring between different computers.

4. Visualization&Processing

Use matplotlib to visualize the data. Use sklearn to do some basic processing.

### Offline Collection System
Sensors to MCU:
1. Connect the MCU and the Sensors

Use A0-A4 for data receiving. For example, 2 sensors were used in this project. So use A0 to read data from moisture sensor and use A1 to read temperature sensor.

2. Make the MCU Read the Signal(Voltage) from Sensors

Initiate the MCU and data receiving pin to read the signal from sensors. 

3. Calibrate the Sensors by Calculating the Real Data and the Signal

The moisture sensor requires calibration. Firstly, read and record the voltage from dry air as 0% humidity. Secondly, read and record the voltage from water as 100% humidity. After getting both boundaries, more accurate levels can be divided.

4. Transform the Signal into Information(Temperature(Celsius) and Humidity(Percentage))

Use equation to automatically calculate the temperature and moisture based on the voltages.

5. Output the Information

Same as Real-time Data Collection ⬆️

Newer Ones ⬇️

MCU to SD Card:
1. Connect the MCU and SD card writer
2. Format the SD card into FAT32
3. Insert the SD card
4. Make the MCU write the data into SD card with SensorOutput.ino.
5. Read the SD card and extract the data

## Codes
Data collection includes two parts: 
### 1. Real-time data collection(PC-based)
The initial idea is collecting data from sensors to PC directly. OutputTemp.ino works on Adafruit METRO to output the temperture based on the eqution: Celsius = (voltage - 0.5) * 100.0, dataAccess_Save.py works on PC to read the output from METRO and write the result into a csv file with current time.

### 2. Offline data collection(SD card based)
Considering that we are collecting outdoor data and we cannot put our laptop outside all the time, we developped another code to do all the things on Adafruit METRO without a PC. SensorOutput.ino was designed to collect moisture data and temperature data of soil surface consistantly and write the collected data into a txt file and store the file on a SD card.

# Data Visualization
## Data Filtering
Data Filtering.py used lowpass filter, highpass filter and Fast Fourier transform to filter the data.
## Data Regression
Gaussian was used in Data regression.py for data regression.
## Data Visualization
Visualization.py is the script for data visualization.

# Numerical Model
dM/dt = -0.000002(T-Taverage)

Model.py was used to realize the proposed numerical model. The data used was collected on Nov.,28,2019(Mois_Temp_Nov28-Dec1.csv).

# One more thing
During our data collection, our devices were mis-detected as bomb and the police came > <, which disabled us to collect enough data to develop a better model.
