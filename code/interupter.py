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