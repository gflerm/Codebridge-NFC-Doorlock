
#include <SoftwareSerial.h>


byte query[8] = {
  0xAA, 0x00, 0x03, 0x25, 0x26, 0x00, 0x00, 0xBB};

byte val;
int i ;

#define door  8
#define duration  250
#define rxPin 9
#define txPin 10

SoftwareSerial rfid( rxPin, txPin );  

void setup()
{
  pinMode(door, OUTPUT);             // Define door output
  digitalWrite(door, LOW);           // Door switch to off 
  Serial.begin(9600);                // Setup serial port for Pc side
  rfid.begin(9600);                  // Setup software serial for reader side
}

void loop()
{
for (i=0 ; i<8 ; i++){              // Send MF_GET_SNR (0x25) command
 rfid.write(query[i]) ;
 }

while(rfid.available()>0){          // Read response from NFC-reader and send to serial port
 val=rfid.read();
 Serial.print(val, HEX);
 Serial.print(" ");
 }
Serial.println();


if (Serial.available()) {          // Get response from serial port, check for D(0x44) to open door.          
 int byte = Serial.read();
 Serial.print(byte,HEX);
 if (byte == 0x44 ){
  digitalWrite(door, HIGH);
  delay(duration);
  digitalWrite(door, LOW);
  }
 }

delay(250);                       // delay for processing on pc side

}
