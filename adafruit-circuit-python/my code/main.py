from analogio import AnalogOut
import digitalio
import board
import neopixel
import time

#aout = AnalogOut(board.A0)

# get the status LED by the USB port
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#led.value = 0

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .2)
#pixels.fill((100, 0, 100))
pixels.fill((0, 0, 0))
pixels.show()

#purple: equal parts red and blue ie: (50, 0, 50)
#yellow: equal parts red and green (50, 50, 0)
#orange: equal parts full red half green (50, 25, 0)


maxLum = 250
minLum = 50
stepSize = 5

while True:
    intensity = 20
    sleepTime = 0.05

    maxLum = 150
    minLum = 25
    stepSize = 5 
    
    #sleepTime = random()
    #led.value = not led.value
    for intensity in range (minLum, maxLum, stepSize):
        #led.value = not led.value
        #pixels.fill((intensity, 0, 0))
        pixels[0] = pixels[1] = pixels[2] = pixels[3] = pixels[4] = (intensity, 0, 0)
        pixels[6] = pixels[8] = (intensity, 0, 0)
        time.sleep(sleepTime)

        #led.value = not led.value
        #time.sleep(sleepTime)

    #led.value = not led.value
    #intensity = 256

    #maxLum = intensity

    for intensity in range (maxLum, minLum, -1*stepSize):
        #led.value = not led.value
        #pixels.fill((maxLum-intensity, 0,0))
        pixels[0] = pixels[1] = pixels[2] = pixels[3] = pixels[4] = (intensity, 0, 0)
        pixels[6] = pixels[8] = (intensity, 0, 0)
        time.sleep(sleepTime)

        #led.value = not led.value
        #time.sleep(sleepTime)



    #pixels.

    #pixels.fill((0, 0,0))
    #time.sleep(sleepTime)
