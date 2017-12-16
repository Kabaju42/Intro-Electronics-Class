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

# Run a while loop that lasts forever
# (or until the power gets cut.)
while True:
   # Note that everything in the loop is indented 
   
   # led.value tells the led to be ether on (1) or off (2)
   led.value = 1
   # time.sleep tells the computer to wait 
   time.sleep(.5)

   led.value = 0
   time.sleep(.5)


