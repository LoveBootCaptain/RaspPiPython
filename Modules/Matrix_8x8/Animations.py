#!/usr/bin/python
from time import sleep

from BitMaps import *
from Modules.Adafruit_Python_Code.Adafruit_LEDMatrix.Adafruit_8x8 import EightByEight
from Modules.Adafruit_Python_Code.Adafruit_LEDMatrix.Adafruit_LEDBackpack import LEDBackpack

grid_left = EightByEight(address=0x70)
grid_right = EightByEight(address=0x71)

backpack_left = LEDBackpack(0x70)
backpack_right = LEDBackpack(0x71)

open_eye_animation = [

    eye_center,
    eye_center

]

blink_animation = [

    eye_center,
    eye_blink,
    eye_closed,
    eye_blink,
    eye_center,
    eye_center

]

look_left_animation = [

    eye_left,
    eye_left_2

]

look_left = [

    eye_left_2

]

look_left_back_animation = [

    eye_left

]

look_right_animation = [

    eye_right,
    eye_right_2

]

look_right = [

    eye_right_2

]

look_right_back_animation = [

    eye_right

]

look_up_animation = [

    eye_up,
    eye_up_2

]

look_up = [

    eye_up_2

]

look_up_back_animation = [

    eye_up

]

look_down_animation = [

    eye_down,
    eye_down_2

]

look_down = [

    eye_down_2

]

look_down_back_animation = [

    eye_down

]

look_angry_left = [

    eye_angry_left

]

look_angry_right = [

    eye_angry_right

]

look_stoned = [

    eye_stoned

]


def animation_time():
    sleep(0.125)


def hold_time():
    sleep(1)


def picture_left(bitmap):
    i = 0

    for byte in bitmap:
        left_line = int(byte, 2)
        grid_left.writeRowRaw(i, left_line)
        i += 1


def picture_right(bitmap):
    i = 0

    for byte in bitmap:
        right_line = int(byte, 2)
        grid_left.writeRowRaw(i, right_line)
        i += 1


def mood_left(scene):
    for look in scene:

        i = 0

        for byte in look:
            left_line = int(byte, 2)
            grid_left.writeRowRaw(i, left_line)
            i += 1


def mood_right(scene):
    for look in scene:

        i = 0

        for byte in look:
            right_line = int(byte, 2)
            grid_right.writeRowRaw(i, right_line)
            i += 1


def animation(scene):
    for look in scene:

        i = 0
        animation_time()

        for byte in look:
            line = int(byte, 2)
            print line
            grid_left.writeRowRaw(i, line)
            grid_right.writeRowRaw(i, line)
            i += 1
