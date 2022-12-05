import board
import time 
import math
import pwmio 
from adafruit_motor import servo 

pwm = pwmio.PWMOut(board.D3, duty_cycle=2 **15, frequency=50)
myServo = servo.Servo(pwm)

while True:
    myServo.angle = 90 
    time.sleep(1)
    myServo.angle = 0
    time.sleep(1)