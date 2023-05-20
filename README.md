# CircuitPython

## Table of Contents

* [Table of Contents](#Table_Of_Contents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython RainbowSensor](#Rainbow_Distance_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython Photointerupter](#Photointerupter)
* [CircuitPython RotaryEncoder](#Rotary_Encoder)
* [CircuitPython TempratureSensor](#Temp_Sensor)

---

## Hello CircuitPython

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


## CircuitPython Servo

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

## Rainbow Distance Sensor

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


## CircuitPython LCD

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

## Photointerupter

### Description and Code
The goal of this code was to utilize a photointerupter to count the number of times something passes in between the photointerupter. Then using print the counter number using the serial monitor.
```Python
# Zachary Siller
# Engineering 3 3/28/2023
# Count using a photointerupter
import time
import digitalio
import board

photoI = digitalio.DigitalInOut(board.D7) #sets photointerupter pin
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

last_photoI = True
last_update = -4

photoICrosses = 0

while True:
    if time.monotonic()-last_update > 4:
        print("The number of crosses is {photoICrosses}")
        last_update = time.monotonic()

    if last_photoI != photoI.value and not photoI.value: #checks the previous photo state and if they are different it adds one
        photoICrosses += 1
    last_photoI = photoI.value

```

### Evidence
![ezgif-3-097eb97f2f](https://user-images.githubusercontent.com/71402927/228946056-1d1356f9-8fd0-410c-a610-d5ec2c489edc.gif)


### Wiring
![Screenshot (2)](https://github.com/zsiller38/CircuitPython/blob/master/Images/Screenshot%202023-03-31%202.05.06%20PM.png?raw=true)

### Reflection
This code was easy to get working mainly because it was the only one that did not involve a serial monitor. I used code from [River](https://github.com/rivques/) as a baseline to understand what was going on. I initially did not know what time.monotonic meant but now I know it is simply a clock that cannot move backwards. This assignment was cool and satisfying when it was working.

## Rotary Encoder

### Description and Code
This code is using a rotary encoder to change states. The states determine what LEDs are one. A green red and yellow LEDs are used to mimick a traffic stop. Then a push button on the rotary encoder turns the light on and off once the encoder selects the state. The rotary encoder uses 5 pins. A power, ground, buton, and two others which are used to determine which way the encoder was turned and how fast. Finally an LCD is used to display prompts based on what the encoder is selecting. 
```Python
# Zachary Siller
# Rotary encoder
# 3/30/2023
import time
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

encoder = rotaryio.IncrementalEncoder(board.D3, board.D2) # Sets up the encoder pins and button
last_position = 0
btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Buttonyep = 1

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

ledGreen = DigitalInOut(board.D8)     # assigns led pins 
ledYellow = DigitalInOut(board.D9)
ledRed = DigitalInOut(board.D10)
ledGreen.direction = Direction.OUTPUT
ledYellow.direction = Direction.OUTPUT
ledRed.direction = Direction.OUTPUT

while True:
    position = encoder.position    # checks if the encoder has turned and checks which direction it has turned
    if position != last_position:
        if position > last_position:
            state = state + 1
        elif position < last_position:
            state = state - 1
        if state > 2:
            state = 2
        if state < 0:
            state = 0
        print(state)
        if state == 0:      # prints based on state
            lcd.set_cursor_pos(0, 0)
            lcd.print("GOOOOO")
        elif state == 1:
            lcd.set_cursor_pos(0, 0)
            lcd.print("yellow")
        elif state == 2:
            lcd.set_cursor_pos(0, 0)
            lcd.print("STOPPP")
    if btn.value == 0 and Buttonyep == 1:
        print("buttion")
        if state == 0:  # changes LED color
                ledGreen.value = True
                ledRed.value = False
                ledYellow.value = False
        elif state == 1:
                ledYellow.value = True
                ledRed.value = False
                ledGreen.value = False
        elif state == 2:
                ledRed.value = True
                ledGreen.value = False
                ledYellow.value = False
        Buttonyep = 0
    if btn.value == 1:
        time.sleep(.1)
        Buttonyep = 1
    last_position = position
    
```
### Evidence
![ezgif-3-097eb97f2f](https://user-images.githubusercontent.com/91289762/226446966-8a585aef-7c21-480a-8ca3-219ae95f4cef.gif)

Image Credit goes to [Kaz](https://github.com/kshinoz98/CircuitPython)
### Wiring
![ezgif-3-097eb97f2f](https://github.com/zsiller38/CircuitPython/blob/master/Images/Screenshot%202023-03-31%202.11.26%20PM.png)
### Reflection
This project was extremely frustrating. VS code had not been working for the previous few days so I was using Mu. Mu was actually easy to use although it is less versatile and complex than VS code. The primarly issue was with the LCD. Sometimes the LCD sucks to much power from the metro board and when this happens the board shuts of and refuses to connect. I had to implement a simple switch which would allow the board to connect to the computer before the LCD was connectd. Later on I switched to connecting the LCD after the board was already connected which was far easier. I used code from [Kaz](https://github.com/kshinoz98/CircuitPython) to help get the project started. The code is not that complex. It consists of some code assigning states based on how the encoder has moved and then if statements to turn of the LEDs. This project was cool and I enjoyed it.

## Temp Sensor

### Description and Code
The goal of this code was to use a temp sensor and convert its output into celcius. Then using an LCD display the temp in celcius and farenhiet and print some phrases based on the temprature. 
``` Python
#Zachary Siller
#Temp Sensor
#3/20/2023
import board   #[Lines 1-8] Importing all Neccessary libraries to communicate with LCD
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import board
import analogio


# get and i2c object
i2c = board.I2C()
tmp36 = analogio.AnalogIn(board.A0)
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
def tmp36_temperature_C(analogin):              #Convert millivolts to temperature
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value 
    lcd.set_cursor_pos(0, 0)           #print reactions to tempratures
    if temp_F > 75:
        lcd.print("it's too hot!")
    elif temp_F < 70:
        lcd.print("it's too cold")
    else:
        lcd.print("It's just right")
    lcd.set_cursor_pos(1, 0)
    lcd.print("Temp: {}F".format(temp_F))
    time.sleep(.5)

```

### Evidence
![ezgif-3-097eb97f2f](https://github.com/zsiller38/CircuitPython/blob/master/Images/ezgif.com-crop.gif)

Image Credit goes to [Vincent](https://github.com/vmanka25/CircuitPython)
### Wiring
![ezgif-3-097eb97f2f](https://github.com/zsiller38/CircuitPython/blob/master/Images/Screenshot%202023-03-31%202.02.34%20PM.png)
### Reflection
This code was probably the easiest of them all. The code is very simple. The one thing I learned about was how a temprature sensor detects temprature. It converts the surrounding temprature into millivolts which we can ten convert into celcius and farenhiet. This assignment was very cool because now I know a lot more about temprature and how it is mesured. 



