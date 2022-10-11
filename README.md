# CircuitPython

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


Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
No wiring required

### Reflection
This projects hardest component was linking my github repository and vs code. Once that was completed it was very easy to use VS code and upload changes to github. I already enjoy circuit python far more than c++. learning the new language should not be hard because it is way for intuitive that c++.


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


## Rainbow distance sensor

### Description and Code
Goal to change the color of a RBG light using and Ultrasonic sensor
  
```python
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
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/giphy%20(1).gif?raw=true)
### Wiring
![spinningMetro_Optimized](https://github.com/zsiller38/CircuitPython/blob/master/Images/Screenshot%202022-10-11%20153206.png?raw=true)



### Reflection
This project was very hard because I had trouble understanding the mapping function used. I needed to get some help from classmates to complete the code but now I understand how and why the code works. WHile coding there were problems with the if statements to based on the distance the sensor was reading. We did'nt use an elif statement and instead just used if statements. This created an issue were the code would jump statements and do the wrong thing. We did not need elif statements in c++ so it was important to learn about them.


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
