import digitalio
import board
import neopixel
import time
from analogio import AnalogOut
import random

#color arrays
#color[0] = bytearray([255, 0, 0])
#color[1] = bytearray([0, 255, 0])
#color[2] = bytearray([0, 0, 255])
#color[3] = bytearray([100, 25, 0]) # yellow
#color[4] = bytearray([100, 15, 0]) # orange
#color[5] = bytearray([100, 0, 100]) #purple
color[0] = (255, 0, 0)
color[1] = (0, 255, 0)
color[2] = (0, 0, 255)
color[3] = (100, 25, 0) # yellow
color[4] = (100, 15, 0) # orange
color[5] = (100, 0, 100) #purple
                     

#use random numbers
random.seed(0)

# Get the red LED by the USB port
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Turn get the RGB leds
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .2)
pixels.fill((0, 0, 0))
pixels.show()

while True:
   #for i in range (0, 10, 1):
   #   pixels[i] = (100, 30, 0)
   #   led.value = 1
   #   time.sleep(.5)
   
   i = 5
   i = random.randint(0, 9)
   j = random.randint(0, 5)
   pixels[i] = (j)
   time.sleep(.75)

   led.value = 0
   pixels.fill((0, 0, 0))
   time.sleep(.5)

