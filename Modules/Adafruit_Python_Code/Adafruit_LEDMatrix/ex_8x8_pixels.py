#!/usr/bin/python

import time

from Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid1 = EightByEight(address=0x70)
grid2 = EightByEight(address=0x71)

print "Press CTRL+Z to exit"

# Continually update the 8x8 display one pixel at a time
while (True):
    for x in range(0, 8):
        for y in range(0, 8):
            grid1.setPixel(x, y)
            grid2.setPixel(x, y)
            time.sleep(0.05)
    time.sleep(0.5)
    grid1.clear()
    grid2.clear()
    time.sleep(0.5)
