#!/usr/bin/python

from time import sleep

from Modules.PS3_Controller.PS3ControllerConfig import *


# #### PLAY THE GAME #### #

# Define timeframe

tf = 0.1

try:

    # this will run until you press the START Button (3)

    while j.get_button(button_start) == 0:

        # process event handlers

        pygame.event.pump()

        # directions D-Pad

        # up (4)

        if j.get_button(button_up) != 0:

            print "UP"
            sleep(tf)

        # down (6)

        elif j.get_button(button_down) != 0:

            print "DOWN"
            sleep(tf)

        # left (7)

        elif j.get_button(button_left) != 0:

            print "LEFT"
            sleep(tf)

        # right (5)

        elif j.get_button(button_right) != 0:

            print "RIGHT"
            sleep(tf)

        # SystemButtons

        # Select (0)

        elif j.get_button(button_select) != 0:

            print "SELECT"
            sleep(tf)

        # MainButtons

        # rectangle-button (12)

        elif j.get_button(button_rectangle) != 0:

            print "RECTANGLE"
            sleep(tf)

        # X-button (14)

        elif j.get_button(button_cross) != 0:

            print "CROSS"
            sleep(tf)

        # square-button (15)

        elif j.get_button(button_triangle) != 0:

            print "TRIANGLE"
            sleep(tf)

        # O-button (13)

        elif j.get_button(button_circle) != 0:

            print "CIRCLE"
            sleep(tf)

        # shoulder-button

        # right shoulder (11)

        elif j.get_button(button_shoulder_right) != 0:

            print "RIGHT SHOULDER"
            sleep(tf)

        # left shoulder (10)

        elif j.get_button(button_shoulder_left) != 0:

            print "LEFT SHOULDER"
            sleep(tf)

        # right trigger (9)

        elif j.get_button(button_trigger_right) != 0:

            print "RIGHT TRIGGER"
            sleep(tf)

        # left trigger (8)

        elif j.get_button(button_trigger_left) != 0:

            print "LEFT TRIGGER"
            sleep(tf)

        # thumbstick buttons

        # right thumbstick (2)

        elif j.get_button(button_thumb_right) != 0:

            print "RIGHT THUMBSTICK"
            sleep(tf)

        # left thumbstick (1)

        elif j.get_button(button_thumb_left) != 0:

            print "LEFT THUMBSTICK"
            sleep(tf)

            # thumbsticks direction sleepment

            # STOP

        # elif AXIS_LEFT_UPDOWN == 0.00 and AXIS_RIGHT_UPDOWN == 0.00:

            # print "CENTER"
            # sleep(tf)

        # left thumbstick directions

        # left thumbstick up

        elif j.get_axis(axis_left_updown) < 0:

            print "LEFT THUMBSTICK UP"
            sleep(tf)

        # left thumbstick down

        elif j.get_axis(axis_left_updown) > 0:

            print "LEFT THUMBSTICK DOWN"
            sleep(tf)

        # left thumbstick left

        elif j.get_axis(axis_left_leftright) < 0:

            print "LEFT THUMBSTICK LEFT"
            sleep(tf)

        # left thumbstick right

        elif j.get_axis(axis_left_leftright) > 0:

            print "LEFT THUMBSTICK RIGHT"
            sleep(tf)

        # right thumbstick directions

        # right thumbstick up

        elif j.get_axis(axis_right_updown) < 0:

            print "RIGHT THUMBSTICK UP"
            sleep(tf)

        # right thumbstick down

        elif j.get_axis(axis_right_updown) > 0:

            print "RIGHT THUMBSTICK DOWN"
            sleep(tf)

        # right thumbstick left

        elif j.get_axis(axis_right_leftright) < 0:

            print "RIGHT THUMBSTICK LEFT"
            sleep(tf)

        # right thumbstick right

        elif j.get_axis(axis_right_leftright) > 0:

            print "RIGHT THUMBSTICK RIGHT"
            sleep(tf)

    else:
        j.quit()

# #### THAT'S ALL FOLKS #### #

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    j.quit()
