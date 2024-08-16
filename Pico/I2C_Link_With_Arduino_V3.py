'''
Module: I2C_Link_With_Arduino_V3.py
https://github.com/robotcreation
Firmware: MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico with RP2040
Description:    This module is linking an arduino with a MaxSonar
                to the Pico via an I2C link and displays the Range 

Pins used:

    I2C datalink: I2C0 , SCL = = Pin(17), SDA = Pin(16), freq=400000
    OLED: I2C1 with SCL = Pin(19) and SDA = Pin(18) and freq = 400000 (100000 doesn't work with latest firmware)

'''

from machine import Pin, I2C
from time import sleep
from SSD1306 import SSD1306_I2C

MSG_SIZE = 20
led = Pin("LED", Pin.OUT)
def Blink_LED(): #Blink onboard LED
    led.toggle()
    sleep(0.1)
    led.toggle()
    
Blink_LED()
sleep(0.5)


i2cComms = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
addr = i2cComms.scan()[0]

i2cOLED = I2C(1,scl = Pin(19),sda = Pin(18),freq = 400000)
oled1 = SSD1306_I2C(128, 64, i2cOLED, 0x3C)

#oled = SSD1306_I2C(128, 64, i2c, addr=0x3D)
oled2 = SSD1306_I2C(128, 64, i2cComms, 0x3C)


while True:
    oled1.fill(0)
    oled1.text('Pico I2C databus', 0, 0)
    print("Sending data From PiCO")
    oled1.fill_rect(0, 16, 128, 8, 0)
    oled1.text('Sending Request...', 0, 16)
    oled1.show()
    
    i2cComms.writeto(addr, 'Data from PiCO')
    Blink_LED()
    sleep(0.5)
    
    print("Request data.....")
    oled2.fill(0)
    oled2.text('I2C Databus', 0, 0)
    oled1.fill_rect(0, 16, 128, 8, 0)  # Blank the line
    oled2.text('Request data.....', 0, 16)
    oled2.show()
    
    data = i2cComms.readfrom(addr, MSG_SIZE)
    distance_str = data.split(b'\x00')[0].decode('ascii')
    print("Received distance: " + distance_str)

    # on data received Display on I2C bus that the data was sent
    # the Arduino cannot display on OLED
    oled2.text("Sent: " + distance_str, 0, 40)
    oled2.show()
    
    # Print on OLED
    oled1.fill_rect(0, 16, 128, 8, 0)  # Blank the line
    oled1.text('Data Received', 0, 16)
    oled1.text("Data: " + distance_str + "mm", 0, 45)
    oled1.show()
    
    Blink_LED()
    sleep(0.5)
    #Clear the I2C bus display
    oled2.fill_rect(0, 40, 128, 8, 0)  # Blank the line
    oled2.show()
    
    sleep(0.5)

