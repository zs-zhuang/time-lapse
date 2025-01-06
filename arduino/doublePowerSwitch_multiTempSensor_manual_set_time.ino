
// Basic script that performs the following fucntions:
// Manually set current time
// Allow multiple processes to run on independent timer without using delay(), this is done using millis
// check current time every second
// Print time to serial every 10 seconds
// Print temperature to serial every 10 seconds using millis
// Turn on and off powerswitch at specific time interval

#include <OneWire.h>
#include <DallasTemperature.h>
#include <Time.h>

#define ONE_WIRE_BUS 3                             // Data wire is plugged into digital pin 3 on the Arduino
#define NumberOfDevices 6                          // Set maximum number of devices in order to dimension 
             
int current_minute;
int LEDX = 8;  //red LED for scanner X
int LEDY = 9;  //green LED for scanner Y
int powerX = 10;
int powerY = 12;
long previousMillis = 0;
long interval = 10000;
                                                   // Array holding all Device Address arrays.
OneWire oneWire(ONE_WIRE_BUS);                     // Setup a oneWire instance to communicate with any OneWire devices

DallasTemperature sensors(&oneWire);               // Pass our oneWire reference to Dallas Temperature. 

byte allAddress [NumberOfDevices][8];              // Device Addresses are 8-element byte arrays.
                                                   // we need one for each of our DS18B20 sensors.

byte totalDevices;                                 // Declare variable to store number of One Wire devices
                                                   // that are actually discovered.
void setup() {
  pinMode(powerX, OUTPUT);
  pinMode(powerY, OUTPUT);
  pinMode(LEDX, OUTPUT);
  pinMode(LEDY, OUTPUT);
  
  digitalWrite(powerX, LOW);
  digitalWrite(powerY, LOW);
  digitalWrite(LEDX, LOW);
  digitalWrite(LEDY,LOW);
  
  setTime(18,42,30,25,4,13);
    
  Serial.begin(9600);
  sensors.begin();
  totalDevices = discoverOneWireDevices();         // get addresses of our one wire devices into allAddress array 
  for (byte i=0; i < totalDevices; i++) 
    sensors.setResolution(allAddress[i], 10);      // and set the a to d conversion resolution of each.
}

byte discoverOneWireDevices() {
  byte j=0;                                        // search for one wire devices and
                                                   // copy to device address arrays.
  while ((j < NumberOfDevices) && (oneWire.search(allAddress[j]))) {        
    j++;
  }
  for (byte i=0; i < j; i++) {
    Serial.print("Device ");
    Serial.print(i);  
    Serial.print(": ");                          
    printAddress(allAddress[i]);                  // print address from each device address arry.
  }
  Serial.print("\r\n");
  return j                      ;                 // return total number of devices found.
}

void printAddress(DeviceAddress addr) {
  byte i;
  for( i=0; i < 8; i++) {                         // prefix the printout with 0x
      Serial.print("0x");
      if (addr[i] < 16) {
        Serial.print('0');                        // add a leading '0' if required.
      }
      Serial.print(addr[i], HEX);                 // print the actual value in HEX
      if (i < 7) {
        Serial.print(", ");
      }
    }
  Serial.print("\r\n");
}

void printTemperature(DeviceAddress addr) {
  float tempC = sensors.getTempC(addr);           // read the device at addr.
  if (tempC == -127.00) {
    Serial.print("Error getting temperature");
  } else {
    Serial.print(tempC);                          // and print its value.
    Serial.print(" C (");
    Serial.print(DallasTemperature::toFahrenheit(tempC));
    Serial.print(" F)");
  }
}

void loop() {
  unsigned long currentMillis = millis();
  delay(1000);
  //digitalClockDisplay();
  current_minute = (minute());
  //Serial.print(current_minute);
  //Serial.println();
    
  ///if (current_minute == 58 || current_minute == 59  || current_minute == 0 || current_minute == 1 || current_minute == 28 || current_minute == 29  || current_minute == 30 || current_minute == 31) {
  if (current_minute == 45) {    
      digitalWrite(LEDX, HIGH); // LEDX on
      digitalWrite(powerX, HIGH); // powerswitchX on
  }
  
  ///else if (current_minute == 3 || current_minute == 4  || current_minute == 5 || current_minute == 6 || current_minute == 33 || current_minute == 34  || current_minute == 35 || current_minute == 36) {
  else if (current_minute == 43) {    
      digitalWrite(LEDY, HIGH); // LEDY on
      digitalWrite(powerY, HIGH); // powerswitchY on
  }
  
  else {
      digitalWrite(LEDX, LOW); // LEDX off
      digitalWrite(powerX, LOW); // powerswitchX off
      digitalWrite(LEDY, LOW); // LEDY off
      digitalWrite(powerY, LOW); // powerswitchY off
      
  }    
  
  //sensors.requestTemperatures();  // Initiate  temperature request to all devices
  if(currentMillis - previousMillis > interval) {
      sensors.requestTemperatures();
      //digitalClockDisplay();
      Serial.print(hour());
      Serial.print(" ");
      Serial.print(minute());
      Serial.print(" ");
      Serial.print(second());
      Serial.print("   ");
      previousMillis = currentMillis;
      for (byte i=0; i < totalDevices; i++) {
        //Serial.print("Device ");
        //Serial.print(i);
        //Serial.print(": ");
        printTemperature(allAddress[i]);
        Serial.print("   ");
        //Serial.print("\n\r");
      }
      Serial.print("\n");
      //Serial.print("\n\r\n\r");
  }    
}

void digitalClockDisplay(){
  // digital clock display of the time
  Serial.print(hour());
  Serial.print(" ");
  Serial.print(minute());
  Serial.print(" ");
  Serial.print(second());
  Serial.print(" ");
  Serial.print(day());
  Serial.print(" ");
  Serial.print(month());
  Serial.print(" ");
  Serial.print(year());
  Serial.println();

}
