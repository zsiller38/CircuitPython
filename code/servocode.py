# Zachary Siller
# 9/29/2022
# hit button to make a servo turn

import board
import time 
import math
import pwmio 
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull ## sets pin numbers and states for buttons
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP

pwm = pwmio.PWMOut(board.D5, duty_cycle=2 **15, frequency=50)
myServo = servo.Servo(pwm)

print("starting")
while True:
    print("re")
    if btn.value == True: ## if button one is pressed turn 180 degrees
        myServo.angle = 180
        time.sleep(1)
        print("Right")
    elif btn2.value == True : ## if button 2 is pressed turn back to start position
        myServo.angle = 0
        time.sleep(1)
        print("Left")