from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 15
camera.rotation = 180

camera.start_preview()
#camera.start_preview(alpha=128)
camera.capture('../Desktop/image.png')
camera.stop_preview()
