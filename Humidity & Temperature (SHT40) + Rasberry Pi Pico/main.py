import time
from machine import Pin, I2C
import sht4x

# Alternatives could be: 0,0,1 / 1,2,3 / 1,6,7
i2c = I2C(0, sda=Pin(4), scl=Pin(5))
sht = sht4x.SHT4X(i2c)
DATA_INTERVAL  = 1 # Interval between readings

print("Temperature, Relative Humidity")
while True:
    temperature, relative_humidity = sht.measurements
    print(f"{temperature:.3f}(°C), " + f"{relative_humidity:.3%}")
    time.sleep(DATA_INTERVAL)
