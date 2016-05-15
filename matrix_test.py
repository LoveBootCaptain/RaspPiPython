#!/usr/bin/python

from Modules.Matrix_8x8.Animations import *

backpack_left.setBrightness(1)
backpack_right.setBrightness(1)

grid_left.clear()
grid_right.clear()

try:

    while True:

        animation(blink_animation)
        hold_time()
        animation(look_left_animation)
        hold_time()
        animation(look_left_back_animation)
        animation(look_right_animation)
        hold_time()
        animation(look_right_back_animation)
        animation(blink_animation)
        sleep(3)
        animation(look_up_animation)
        hold_time()
        animation(look_up_back_animation)
        animation(look_down_animation)
        hold_time()
        animation(look_down_back_animation)
        animation(blink_animation)
        sleep(3)
        animation(blink_animation)
        animation(look_stoned)
        animation(blink_animation)
        mood_left(look_angry_left)
        mood_right(look_angry_right)
        sleep(3)
        animation(blink_animation)
        animation(look_stoned)
        animation(blink_animation)
        mood_left(look_angry_right)
        mood_right(look_angry_left)
        sleep(3)
        animation(blink_animation)
        animation(look_stoned)

    else:

        grid_left.clear()
        grid_right.clear()

# #### THAT'S ALL FOLKS #### #

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    grid_left.clear()
    grid_right.clear()