# Name: Jayed Rafi
# For Raspberry Pi Pico
# Sensor: PMSA003I
# References: https://www.adafruit.com/product/4632

import time
import machine
from pmsa003i import PMSA003I
import sdcard # for sdcard
import uos  #for sdcard
time.sleep(2)  # wait 2 seconds after boot

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=100000) # initialize I2C pins
sensor = PMSA003I(i2c) # Initialize PMSA003I sensor
cs = machine.Pin(15, machine.Pin.OUT)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))
sd = sdcard.SDCard(spi, cs)
led = machine.Pin('LED', machine.Pin.OUT)
# Mount filesystem: This allows us to access the SD card
# as if it was a separate storage drive attached to the pico
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

#change the file name below, else will override previous.
with open("/sd/pmsa003i_data.txt", "w") as file:
    while True:
        data = sensor.read()
        led.value(1)
        #  Data format and information:
        # Units: Mass Concentration Values (µg/m³), Particle Count (/0.1L air)
        # Format: timestamp, PM1.0 ATM, PM2.5 ATM, PM10 ATM, particles>0.3µm, particles>0.5µm, particles>1.0µm, particles>2.5µm, particles>5.0µmm, particles>10µm
        file.write(str(time.time())+","+str(data["PM1.0_ATM"])+","+str(data["PM2.5_ATM"])+","+str(data["PM10_ATM"])+","+str(data["particles_0.3µm"])+","+str(data["particles_0.5µm"])+","+str(data["particles_1.0µm"])+","+str(data["particles_2.5µm"])+","+str(data["particles_5.0µm"])+","+str(data["particles_10µm"])+"\r\n")
        print(str(time.time())+","+str(data["PM1.0_ATM"])+","+str(data["PM2.5_ATM"])+","+str(data["PM10_ATM"])+","+str(data["particles_0.3µm"])+","+str(data["particles_0.5µm"])+","+str(data["particles_1.0µm"])+","+str(data["particles_2.5µm"])+","+str(data["particles_5.0µm"])+","+str(data["particles_10µm"]))
        file.flush()
        time.sleep(1) # Interval between readings (seconds)
    led.value(0)