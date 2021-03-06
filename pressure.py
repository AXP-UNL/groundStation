import time
import board
import busio
import adafruit_lps2x

i2c = busio.I2C(board.SCL, board.SDA)

lps = adafruit_lps2x.LPS22(i2c)

while True:
    print("Pressure: %.2f hPa" % lps.pressure)
    print("Temperature: %.2f" % lps.temperature)
    time.sleep(1)
