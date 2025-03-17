import time
import machine
import bme280

# Initialize I2C
i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6), freq=100000)

DATA_INTERVAL = 1 # Interval between readings

# Initialize BME280
sensor = bme280.BME280(i2c=i2c)

print("Temperature, Humidity and Pressure")
while True:
    temp, pressure, humidity = sensor.values
    print(f"{temp}",f"{humidity}",f"{pressure}")
    time.sleep(DATA_INTERVAL)