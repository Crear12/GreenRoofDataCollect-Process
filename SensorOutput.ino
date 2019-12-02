const int temperaturePin = A1;
const int moisturePin = A0;
#include <SPI.h>
#include <SD.h>
File MoisFile;
File TempFile;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  Serial.print("Initializing SD card...");

  if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");
}

void loop() {
  // put your main code here, to run repeatedly:
  float moisvoltage,voltage, degreesC;
  //moisvoltage = getVoltage(moisturePin);
  voltage = getVoltage(temperaturePin);
  degreesC = (voltage - 0.5) * 100.0;
  //Serial.println(moisvoltage+"moisture");
  MoisFile = SD.open("mois.txt", FILE_WRITE);
  if (MoisFile) {
    Serial.print("Writing to Mois.txt...");
    MoisFile.println(String(analogRead(moisturePin))+",");
    // close the file:
    MoisFile.close();
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening Mois.txt");
  }
  TempFile = SD.open("temp.txt", FILE_WRITE);
  if (TempFile) {
    Serial.print("Writing to Temp.txt...");
    TempFile.println(String(degreesC)+",");
    // close the file:
    TempFile.close();
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening Temp.txt");
  }
  delay(10000);//repeat once per 10s (change as you wish!)
}

float getVoltage(int pin)
{
  return (analogRead(pin) * 0.004882814);
}
