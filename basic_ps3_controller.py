import pygame

from time import sleep
from Modules.PS3_Controller.ControllerConfig import *

# #### PLAY THE GAME #### #

# better don't try this at home

print "Pair your PS3 Controller now"

# print "... wait 5 sec"

# for x in range(0, 6):
#     print x
#     sleep(1)


# Init the PS3 Controller

try:

    pygame.init()

    j = pygame.joystick.Joystick(0)
    j.init()

    print "PS3 Controller connected"

except StandardError:

    print "No Controller Connected. Please pair your PS3 Controller and restart the script."
    sleep(5)

# #### SLEEP #### #

# Define sleep as sleepment

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

        elif j.get_button(button_square) != 0:

            print "SQUARE"
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

        elif j.get_axis(axis_left) == 0.00 and j.get_axis(axis_right) == 0.00:

            print "CENTER"
            sleep(tf)

        # left thumbstick directions

        # left thumbstick up

        elif j.get_axis(axis_left) < 0:

            print "LEFT THUMBSTICK UP"
            sleep(tf)

        # left thumbstick down

        elif j.get_axis(axis_left) > 0:

            print "LEFT THUMBSTICK DOWN"
            sleep(tf)

        # left thumbstick left

        elif j.get_axis(0) < 0:

            print "LEFT THUMBSTICK LEFT"
            sleep(tf)

        # left thumbstick right

        elif j.get_axis(0) > 0:

            print "LEFT THUMBSTICK RIGHT"
            sleep(tf)

        # right thumbstick directions

        # right thumbstick up

        elif j.get_axis(axis_right) < 0:

            print "RIGHT THUMBSTICK UP"
            sleep(tf)

        # right thumbstick down

        elif j.get_axis(axis_right) > 0:

            print "RIGHT THUMBSTICK DOWN"
            sleep(tf)

        # right thumbstick left

        elif j.get_axis(2) < 0:

            print "RIGHT THUMBSTICK LEFT"
            sleep(tf)

        # right thumbstick right

        elif j.get_axis(2) > 0:

            print "RIGHT THUMBSTICK RIGHT"
            sleep(tf)

    else:
        j.quit()

# #### THAT'S ALL FOLKS #### #

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    j.quit()
