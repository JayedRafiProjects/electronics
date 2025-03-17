import time
import machine
from pmsa003i import PMSA003I

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=100000) # initialize I2C pins
DATA_INTERVAL = 5 # Interval between readings
sensor = PMSA003I(i2c) # Initialize PMSA003I sensor

while True:
    data = sensor.read()
    print("Mass Concentration Values (µg/m³)")
    print("PM1.0 (CF=1):", data["PM1.0_CF1"])
    print("PM2.5 (CF=1):", data["PM2.5_CF1"])
    print("PM10 (CF=1):", data["PM10_CF1"])
    print("PM1.0 (ATM):", data["PM1.0_ATM"])
    print("PM2.5 (ATM):", data["PM2.5_ATM"])
    print("PM10 (ATM):", data["PM10_ATM"])
    print("Particle Count (/0.1L air)")
    print("Particles > 0.3µm: ",data["particles_0.3µm"])
    print("Particles > 0.5µm: ",data["particles_0.5µm"])
    print("Particles > 1.0µm " , data["particles_1.0µm"])
    print("Particles > 2.5µm: ",data["particles_2.5µm"])
    print("Particles > 5µm: ",data["particles_5.0µm"])
    print("Particles > 10µm: ",data["particles_10µm"])
    print("========================================")
    time.sleep(DATA_INTERVAL)