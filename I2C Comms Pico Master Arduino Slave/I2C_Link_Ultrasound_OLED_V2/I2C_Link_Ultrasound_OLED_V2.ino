
// I2C_Link_Ultrasound_OLED_V2
// Using MAxSonar on D11-RX and D12-TX
// I2C on A5-SCL and A4-SDA
//
#include <Wire.h>
#define UNO_ADDR 10
#define RESP_SIZE 20
String OutData = "Data From Arduino                                      ";
String InData = "";

// MaxSonar sensor with OLED display
//RX = D11
//TX = D12

#include <SoftwareSerial.h> // needed for UART interface (RX/TX on Digital pins)

// Display 128 x 32 OLED
// uses SSD1306Ascii library
#include "SSD1306AsciiAvrI2c.h"
#define OLED_I2C_ADDRESS 0x3C    // 0X3C+SA0 - 0x3C or 0x3D
//#define OLED_I2C_ADDRESS 0x3D    // 0X3C+SA0 - 0x3C or 0x3D
SSD1306AsciiAvrI2c oled;  // Initialise OLED display

//  Pin numbers
 SoftwareSerial port1(12, 12); // MaxSonar- RX, TX set at TX on Pin 12 to read data
 int start_pin1=11;            // MaxSonar- RX set at Pin 11 to start the cycle

String inString = ""; // MaxSonar Specific
char inChar;          // MaxSonar Specific

int Range1=0;   // Range from sensor
String OutText;

//-------------------------------------------------------------------------------------------
// Function for obtaining MaxSonar_Range
//----------------------------------------------------------------------------------------------------------

int GetRange1()

{
  //PORT 1
    inString = "";

  port1.listen();
  delay(50);
  while (port1.available()){ // clear out buffer
    port1.read();
  }
  
  digitalWrite(start_pin1,HIGH);
  delay(10);
  digitalWrite(start_pin1,LOW) ;

  while (port1.available() == 0){
    // do nothing - wait for a char
  }

  while (port1.available()){   
    inChar = port1.read();
    //Serial.print(inChar);
    if (isDigit(inChar)) {
      // if 0-9,   add it to the string:
      inString += inChar;
    }
    //Serial.println(inString);
    while (port1.available() == 0){
       if (inChar == '\r') {
        break;
       }
    }
  }  
    Range1 = inString.toInt()*25.4;
    return Range1;
}


// I2C Link
void DataReceive(int numBytes)
{
  int i=0;
  char InData[RESP_SIZE];
  memset(InData,0, RESP_SIZE);
  while(Wire.available()) 
  { 
    InData[i++] = Wire.read();
  }
  
  Serial.print("Recv Event: ");
  Serial.println(String(InData));
}


// I2C Link
void DataRequest()
{
  Serial.println(OutData);
  byte resp[RESP_SIZE];
  for (byte i=0; i<RESP_SIZE; ++i) {
    resp[i] = (byte)OutData.charAt(i);
  }
  Wire.write(resp, sizeof(resp));
  Serial.println("Sent resp.....");
}



void setup()
{
  // OLED setup
  //oled.begin(&Adafruit128x32, OLED_I2C_ADDRESS);
  //oled.setFont(Arial_bold_14);
  //oled.clear();
  //oled.setCursor(0, 2);
  //oled.print("Range:           mm");


  // sonar pin setup
  pinMode(start_pin1, OUTPUT); 
  digitalWrite(start_pin1,LOW);

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // set the data rate for the SoftwareSerial port
  port1.begin(9600);
  Serial.println("Serial Ready");  // Write with the carrage return and line feed
  delay(50);

  // I2C Link
  Wire.begin(UNO_ADDR);

  /*Event Handlers*/
  Wire.onReceive(DataReceive);
  Wire.onRequest(DataRequest);



}

void loop()
{
  Range1 = GetRange1();        // get sonar range
  OutData = String(Range1);
  Serial.println(Range1);  

  oled.setCursor(0, 0);
  oled.print("PI:");   // Clear the range

  oled.setCursor(60, 2);
  oled.print("       ");   // Clear the range
  oled.setCursor(60, 2);
  oled.print(Range1);


 delay(50);
}

