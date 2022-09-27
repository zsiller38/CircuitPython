#zachary siller
# 9/27/2022
#turn on a rbg light and make it turn red
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255)) #turns rbg red