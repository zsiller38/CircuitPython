#zachary siller
#9/13/2022
#goal to make a servo turn
import time
import board
import pwmio
from adafruit_motor import servo

#sets pin number
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)


my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5): #moves servo then moves it back
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): 
        time.sleep(0.05)