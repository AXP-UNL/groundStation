

import time
import board
import busio
import adafruit_bno055
import adafruit_lps2x

import math 

file_name = "output.txt"

# Use these lines for I2C
i2c = busio.I2C(board.SCL, board.SDA)

bno = adafruit_bno055.BNO055_I2C(i2c)
lps = adafruit_lps2x.LPS22(i2c)

 
last_val = 0xFFFF
 
 
def temperature():
    global last_val  # pylint: disable=global-statement
    result = bno.temperature
    if abs(result - last_val) == 128:
        result = bno.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result

def magnetic_to_heading(magnetic_data):
    x = magnetic_data[0]
    y = magnetic_data[1]

    heading = math.atan2(y, x) * 180 / math.pi

    return heading

def write_values(data, filePath):
    file = None
    try:
        file = open(filePath, 'w') 
    except IOError:
        file.close()
        return
    finally:
        file.write(data)
        file.close()

#file = open(file_name, 'w') 

while True:

    file = open(file_name, 'w')
    #print("Temperature: {} degrees C".format(sensor.temperature))
    #print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    #print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    degrees = magnetic_to_heading(bno.magnetic)
    pressure = lps.pressure
    temperature = lps.temperature
    
    file.write(str(degrees))
    file.write(',')
    file.write(str(pressure))
    file.write(',')
    file.write(str(temperature))
    file.write('\n')
    #print("Pressure: %.2f" % lps.pressure)
    #print("Temperature: %.2f" % lps.temperature)

    #print("Heading: %.2f" % degrees)

    #print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    #print("Euler angle: {}".format(sensor.euler))
    #print("Quaternion: {}".format(sensor.quaternion))
    #print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    #print("Gravity (m/s^2): {}".format(sensor.gravity))
    #print()
    file.close()
    time.sleep(1)
