# The import command tells the computer what libraries to use
import digitalio
from analogio import AnalogOut
import board
import neopixel
import time

# 'led' is an object with all the information
# about the red led by the USB port
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Create another object for the multicolor LEDs
# the brand name for these ones is neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .2)
# Start by turning them all off
pixels.fill((0, 0, 0))
pixels.show()

# Run a while loop that lasts forever
# (or until the power gets cut.)
while True:
   # Note that everything in the loop is indented 

   # led.value tells the led to be ether on (1) or off (2)
   led.value = 1
   # time.sleep tells the computer to wait
   time.sleep(.5)

   # make another loop to turn on the multicolor leds one at a time
   for i in range (0, 10, 1):
      pixels[i] = (100, 0, 0)
      time.sleep(.5)
      

   led.value = 0
   pixels.fill((0, 0, 0))
   time.sleep(.5)

