# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)

---

## Hello_CircuitPython

### Description & Code
I made the serial monitor say hello world using the print function in circuit python
```python
#zachary siller
#9/13/2022
#goal print hello world on serial monitor
from time import sleep

while True:
    print("Hello world!") #prints hello world
    sleep(4)
```

### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
No wiring required

### Reflection
This projects hardest component was linking my github repository and vs code. Once that was completed it was very easy to use VS code and upload changes to github. I already enjoy circuit python far more than c++. Learning the new language should not be hard because it is way for intuitive that c++.


## CircuitPython_Servo

### Description & Code
I encorperated principles from my button servo from c++ into circuit python to make a servo turn 2 different directions when buttons were pressed. This was done using a basic else if statement and reading buttons states.
```python
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
```

### Evidence

![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/giphy%20(1).gif?raw=true)

### Wiring
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/servocircuitpythonwiring.png?raw=true)

### Reflection
This project was relativly easy because I had already done the same project in arduino, so the code was very easy. The first time I did the project I did not have the buttons but intergrating the buttons was very easy all it required was some new wiring some help from a friend and a few extra lines of code.

## Rainbow distance sensor

### Description and Code
Goal to change the color of a RBG light using and Ultrasonic sensor. This is done by mapping the distance values onto RBG value spectrum. As the distance changes the map function will change the values of the RBG accordingly. 
  
```python
#Zachary Siller
#10/20/2022
#change a RBG light based on sensor data
import digitalio
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel                       
from board import *

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
led.brightness = 0.1
1  #setting the brightness of the light, from 0-1 brightness
ledOutput = 0
Red = 0
Green = 0
Blue = 0

while True:

    try:
        cm = sonar.distance
        print((sonar.distance, Red, Green, Blue))
        time.sleep(0.01)
        if cm < 5:
            led.fill((255, 0, 0))#turns the light red if distance less than 5
        elif cm > 5 and cm < 10:
            Green = 0
            Red = simpleio.map_range(cm, 5.1, 10, 255, 0) #from distance 5 to 10 red and blue values based on distance from ultrasonic sensor
            Blue = simpleio.map_range(Red, 0, 255, 255, 0)
            led.fill((Red, Green, Blue))
        else:
            Blue = simpleio.map_range(cm, 10.1, 20, 255, 0)
            Green = simpleio.map_range(Blue, 0, 255, 255, 0)
            led.fill((0, Green, Blue))#setting the color with RGB values
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)
```
### Evidence
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/giphy.gif?raw=true)

### Wiring
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/Screenshot%202022-10-11%20153206.png?raw=true)



### Reflection
This project was very hard because I had trouble understanding the mapping function used. I needed to get some help from classmates to complete the code but now I understand how and why the code works. WHile coding there were problems with the if statements to based on the distance the sensor was reading. We did'nt use an elif statement and instead just used if statements. This created an issue were the code would jump statements and do the wrong thing. We did not need elif statements in c++ so it was important to learn about them.


## CircuitPython_LCD

### Description & Code
Create a code that counts the number of times a button is pressed and uses another button to toggle counting up and down. This is done by first downloading some extra code from someone elses github repository to make the LCD code work correctly with the metro board. Followed by some else if statements checking the button state of one button and the checking the other one based on the first button state.
```python
#Zachary Siller
#10/20/2022
#Connect a button and lcd to count the number of button presses.
import board
import math
import time
from lcd.lcd import LCD                                     #connects buttons and LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface   #input pins to board
from digitalio import DigitalInOut, Direction, Pull
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP
num = 0                         #Display Variable
Redo = True                     
lcd.print("Starting")
while True:                                 
    if btn.value == True and Redo == True:  
        if btn2.value == True:                    #counts down
            num = num - 1
        else:
            num = num + 1                                   
        lcd.clear()                             #counts down
        lcd.print(str(num))
        Redo = False
        time.sleep(.1)
    elif btn.value == False and Redo == False:
        Redo = True

```

### Evidence

![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/ezgif-2.gif?raw=true)

Image credit goes to [Kaz](https://github.com/kshinoz98/CircuitPython)

### Wiring
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/lcdwiring.png?raw=true)
### Reflection
This project was relativly hard because you had to make sure you did not skip numbers while counting. Getting the ability to toggle between counting up and down was also intresting. When using an LCD it is important to have the right LCD format and configuration, there is also a pontentiometer on the back of the LCD that can be used to adjust the btightness and visibility. The wiring for the LCD was much easier than the first time I used an LCD display.





