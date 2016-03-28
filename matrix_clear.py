#!/usr/bin/python

from Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid_left = EightByEight(address=0x70)
grid_right = EightByEight(address=0x71)

print "Clear the 8x8 Display"

grid_left.clear()
grid_right.clear()
