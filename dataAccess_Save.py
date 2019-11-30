#!/usr/bin/env python
import serial
import datetime
import csv

def Save2csv(input_data,file):#completed
    with open(file+'.csv', 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(input_data)
    


if __name__ == "__main__":
    
    ArduinoData = serial.Serial('COM3',9600) #https://www.youtube.com/watch?v=mF5cE3DS50s
    try:
        while(1):
            Save2csv([ArduinoData.readline().decode('utf-8')[0:-2],str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))],'Temperature&Moisture_Record')
    except:
        print('Something happened!')