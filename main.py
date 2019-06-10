import machine, time
from boothAvailabilityIndicator import NeoPixelBoothAvailibilityIndicator

NUM_PIXELS = 5
NEOPIXEL_PIN = 15

while True:
    indicator = NeoPixelBoothAvailibilityIndicator(NEOPIXEL_PIN, NUM_PIXELS)
    indicator.showInUse()
    time.sleep(1)
    indicator.showAvailable()
    time.sleep(1)
