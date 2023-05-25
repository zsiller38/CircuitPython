#Vincent and Zachary 5/15/2023
#Wheel code no PID

import board
import time
from analogio import AnalogOut, AnalogIn
import simpleio
from lcd import LCD
from lcd import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
last_photoI = False #lines 11-13 start states for variables
current_photoI=True
lasttime=None
pot = AnalogIn(board.A0) #lines 14-18 setup for components
motor = AnalogOut(board.A1)
photoI= AnalogIn(board.A2)
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
lcd.print("Motor Starting")
rpm_list=[] #creates a list for all rpm values
while True:
    print(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) #maps the motor value to the pot value
    motor.value = int(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) 
    current_photoI=photoI.value #reads photo interupter value
    if(last_photoI != current_photoI):
        time1=time.monotonic() #reads out time in fractional seconds
        print(time1)
        if(lasttime != None): #checks to see if this is the first state change of the photointerupter
            deltaT=time1-lasttime
            current_rpm=8*deltaT/60 #calculates rpm
            rpm_list.append(current_rpm) #adds the rpm value to the list
            if(len(rpm_list)>0): #checks if the list length is greater than 0 to avoid dividing by 0
                average_rpm=sum(rpm_list)/len(rpm_list) #calculates average rpm
            else:
                average_rpm=current_rpm
            lcd.set_cursor_pos(0, 0) #lines 36-41 print average and current rpm on the LCD
            lcd.print(current_rpm)
            print(current_rpm)
            lcd.set_cursor_pos(1, 0)
            lcd.print(average_rpm)
            print(average_rpm)
            lasttime=time1 #makes the time1 the new lasttime
    last_photoI=current_photoI #makes current_photoI the new last_photoI