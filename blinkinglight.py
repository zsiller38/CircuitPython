import board
import neopixel
import time
import math

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 255, 0)) #tuuns light a color then turn it off and changes to a new color.
    time.sleep(.5)
    dot.fill((0, 0, 0))
    time.sleep(.5)
    dot.fill((255, 0, 0))
    time.sleep(.5)
    dot.fill((0, 0, 0))
    time.sleep(.5)