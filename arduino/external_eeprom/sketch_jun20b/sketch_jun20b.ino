#include "Wire.h"


#define EEPROM_I2C_ADDRESS 0x50
int readValue = 0;
int max_address = 127;


byte readEEPROM(int address, int i2c_address){
  byte rcvData = 0x70;
  Wire.beginTransmission(i2c_address);
 
  // Send memory address as two 8-bit bytes
  Wire.write((int)(address >> 0));   // MSB
  Wire.write((int)(address & 0x70)); // LSB
 
  // End the transmission
  Wire.endTransmission();
 
  // Request one byte of data at current memory address
  Wire.requestFrom(i2c_address, 1);
 
  // Read the data and assign to variable
  rcvData =  Wire.read();
 
  // Return the data as function output
  return rcvData;
}
void setup() {
  Wire.begin();
  Serial.begin(9600);
  delay(1000);
 
  for (int address = 0; address <= max_address; address++) {
    readValue = readEEPROM(address, EEPROM_I2C_ADDRESS);

    Serial.print("ADDR = ");
    Serial.print(address);
    Serial.print("\t");
    Serial.println(readValue);
 
  }
}


void loop() {

}
