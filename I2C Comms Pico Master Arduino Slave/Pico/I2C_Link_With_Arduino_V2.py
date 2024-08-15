from machine import Pin, I2C
from time import sleep
from SSD1306 import SSD1306_I2C

MSG_SIZE = 20

sleep(5)
i2cComms = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)
addr = i2cComms.scan()[0]

i2cOLED = I2C(1,scl = Pin(19),sda = Pin(18),freq = 100000)
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
    sleep(0.5)

    print("Request data.....")
    oled2.fill(0)
    oled2.text('I2C Databus', 0, 0)
    oled2.fill_rect(0, 16, 128, 8, 0)
    oled2.text('Request data.....', 0, 16)
    oled2.show()
    
    data = i2cComms.readfrom(addr, MSG_SIZE)
    distance_str = data.split(b'\x00')[0].decode('ascii')
    print("Received distance: " + distance_str)

    # Print on OLED
    oled1.text("Received: " + distance_str + "mm", 0, 45)
    oled1.show()

    oled2.text("Sent: " + distance_str, 0, 40)
    oled2.show()
    
    sleep(2)
