import machine, neopixel

class AbstractBoothAvailibilityIndicator:

    def showAvailable(self):
        pass

    def showInUse(self):
        pass

class NeoPixelBoothAvailibilityIndicator(AbstractBoothAvailibilityIndicator):

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
