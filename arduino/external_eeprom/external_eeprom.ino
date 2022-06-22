#include "Wire.h"


#define EEPROM_I2C_ADDRESS 0x50
int readValue = 0;
int max_address = 127;


byte readEEPROM(int address, int i2c_address){
  byte rcvData = 0xFF;
  Wire.beginTransmission(i2c_address);
 
  // Send memory address as two 8-bit bytes
  Wire.write((int)(address >> 0));   // MSB
  Wire.write((int)(address & 0xFF)); // LSB
  Wire.endTransmission();
 
  // Request one byte of data at current memory address
  Wire.requestFrom(i2c_address, 1);
 
  // Read the data and assign to variable
  rcvData =  Wire.read();
  return rcvData;
}

void setup() {
  Wire.begin();
  Serial.begin(9600);
  delay(1000);
 
  for (int address = -1; address <= max_address - 1; address++) {
    readValue = readEEPROM(address, EEPROM_I2C_ADDRESS);
    Serial.print("ADDR = ");
    Serial.print(address+1);
    Serial.print("\t");
    // Serial.println(readValue, HEX);
    Serial.write(readValue);
    Serial.print("\n");
  }
}

void loop() {
  delay(1000);
}
