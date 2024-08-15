# I2C-communication-between-Processors
I2C data transfer in a readable text format between Pico as Master and Arduino as Slave and Two Picos one as Master and other as Slave.

I2C protocol in principal can have two masters on the same bus, but this is not a practical or a good practice as the master creates the clock on the databus (SCL) which the data (SDA) is transferred and practically you can't have two clocks synchronised on the same bus and switching between different masters would be a software headache.
I need the Pico to act as the slave to another Pico which runs the clock as master, however this seems to be an issue as Pico runs micropython and not all the I2C_Slave libraries are available. This means that it is very difficult to provide an address to Pico and use it as a slave device.

Pico as Master - Arduino as Slave
First step was to replicate what already is available on internet which is Pico as Master and Arduino as Slave.  There are a number of examples and I combined a few of them to make a working model of an Arduino connected to an Ultrasound transducer - MaxSonar which I had available to send distance data to a Pico that acts as the master. 
![20240815_102602](https://github.com/user-attachments/assets/637acf68-a19b-4d72-8f0e-42d427dc8a9c)

![Image1](https://github.com/user-attachments/assets/2541d0f0-5e62-4c5b-8786-70a40f26dd52)

![Image2](https://github.com/user-attachments/assets/9137b7f4-f248-4419-bb27-b9e32e466110)



