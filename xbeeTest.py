from digi.xbee.devices import XBeeDevice

device = DigiMeshDevice("/dev/ttyUSB0",9600)
print("did it")
device.open()
print("message")
device.refresh_device_info()

device.close()


