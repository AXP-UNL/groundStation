from gpiozero import Motor
from time import sleep

basePivot = Motor(17,18,pwm=True)
upperPivot = Motor(27,22,pwm=True)
basePivot.forward(1)
