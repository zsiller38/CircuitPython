# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

dot=neopixel.NeoPixel(board.NEOPIXEL,1)
dot.brightness = .01
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:

    try:
        print((sonar.distance,))
        cm=sonar.distance
        if cm < 5:
            dot.fill((255,0,0))
        elif 20 > cm > 5:
            dot.fill((0,0,255))
        else:
            dot.fill((0,255,0))
        

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)