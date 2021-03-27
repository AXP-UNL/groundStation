from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/ttyUSB0",9600)
print("did it")
device.open()
print("second")
device.close()

