from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180

#camera.start_preview()
camera.start_preview(alpha=200)
sleep(5)
camera.stop_preview()

