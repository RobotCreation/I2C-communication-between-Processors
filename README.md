# I2C-communication-between-Processors
I2C data transfer in a readable text format between Pico as Master and Arduino as Slave and Two Picos one as Master and other as Slave.

I2C protocol in principal can have two masters on the same bus, but this is not a practical or a good practice as the master creates the clock on the databus (SCL) which the data (SDA) is transferred and practically you can't have two clocks synchronised on the same bus and switching between different masters would be a software headache.
I need the Pico to act as the slave to another Pico which runs the clock as master, however this seems to be an issue as Pico runs micropython and not all the I2C_Slave libraries are available. This means that it is very difficult to provide an address to Pico and use it as a slave device.

Pico as Master - Arduino as Slave
First step was to replicate what already is available on internet which is Pico as Master and Arduino as Slave.  There are a number of examples and I combined a few of them to make a working model of an Arduino connected to an Ultrasound transducer - MaxSonar which I had available to send distance data to a Pico that acts as the master. 

![20240815_102602](https://github.com/user-attachments/assets/1b0e9583-226e-419a-a9e9-cb47b47ef424)

![Image1](https://github.com/user-attachments/assets/e6ec01bc-53f9-495d-a87c-e3d81cdc774c)
![Image2](https://github.com/user-attachments/assets/2cf411a6-a8f2-44cc-9e6d-16a48410232f)

In this setup, The pico is the Master using I2C0 on Pins GP16-SDA and GP17-SCL to communicate with the Arduino.  The databus is connected to the Arduino which is configured as slave at address 10 (0xA Hex) and also to an OLED display at address 60 (0x3C Hex).
The Pico can write to the OLED via databus and also I connected another OLED connected to I2C1, however it is not possible for the Arduino to communicate with the OLED on the databus and I had to disable the initiation as it would create conflict in the Arduino interrupt commands.



