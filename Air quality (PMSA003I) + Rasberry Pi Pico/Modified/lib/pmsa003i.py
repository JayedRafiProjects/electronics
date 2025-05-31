# Note: Library file.
# For Raspberry Pi Pico
# Sensor: PMSA003I
# References: https://www.adafruit.com/product/4632import time
import struct
import machine

class PMSA003I:
    def __init__(self, i2c, address=0x12):
        self.i2c = i2c
        self.address = address

    def read(self):
        try:
            data = self.i2c.readfrom(self.address, 32)
            if len(data) == 32:
                value = struct.unpack('>HHHHHHHHHHHHHHHxx', data)
                return {
                    "PM1.0_CF1": value[0],
                    "PM2.5_CF1": value[1],
                    "PM10_CF1": value[2],
                    "PM1.0_ATM": value[3],
                    "PM2.5_ATM": value[4],
                    "PM10_ATM": value[5],
                    "particles_0.3µm": value[6],
                    "particles_0.5µm": value[7],
                    "particles_1.0µm": value[8],
                    "particles_2.5µm": value[9],
                    "particles_5.0µm": value[10],
                    "particles_10µm": value[11]
                }
        except OSError:
            print("Error!")
            return None

