# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
I made the serial monitor say hello world with circuit python
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


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
I made a servo turn with circuit python and an adafruit
```python
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
```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection



## Sonar RGB

### Description & Code
I made a neopixel light change colors when distance changed

```python
```

# Zachary Siller
#Rainbow distance sensor
# Goal to change the color of a RBG light using and Ultrasonic sensor

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
```

### Evidence

### Wiring

### Reflection



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
