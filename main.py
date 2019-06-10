import machine, neopixel, time

NUM_PIXELS = 5
NEOPIXEL_PIN = 15

class AbstractBoothAvailibilityIndicator:

    def showAvailable(self):
        pass

    def showInUse(self):
        pass

class NeoPixelBoothAvailibilityIndicator(AbstractBoothAvailibilityIndicator):
    np = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_PIXELS, bpp=4)

    def __init__(self, pin, numPixels):
        self.np = neopixel.NeoPixel(machine.Pin(pin), numPixels, bpp=4)

    def showColor(self, color):
        for i in range(self.np.n):
            self.np[i] = color
        self.np.write()

    def showAvailable(self):
        self.showColor((0,255,0,0))

    def showInUse(self):
        self.showColor((255,0,0,0))

while True:
    indicator = NeoPixelBoothAvailibilityIndicator(NEOPIXEL_PIN, NUM_PIXELS)
    indicator.showInUse()
    time.sleep(1)
    indicator.showAvailable()
    time.sleep(1)
