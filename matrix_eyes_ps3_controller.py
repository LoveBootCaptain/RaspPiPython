import pygame

from Modules.Matrix_8x8.Animations import *
from Modules.PS3_Controller.ControllerConfig import *

backpack_left.setBrightness(1)
backpack_right.setBrightness(1)

grid_left.clear()
grid_right.clear()


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

# Define sleep as movement

tf = 0.1
move = sleep

try:

    # this will run until you press the START Button (3)

    while j.get_button(button_start) == 0:

        # process event handlers

        pygame.event.pump()

        # directions D-Pad

        # up (4)

        if j.get_button(button_up) == 0 and j.get_button(button_down) == 0 and j.get_button(
                button_left) == 0 and j.get_button(button_right) == 0 and j.get_button(button_rectangle) == 0\
                and j.get_button(button_cross) == 0:

            print "MITTE"
            animation(blink_animation)

        if j.get_button(button_up) != 0:

            print "UP"
            animation(look_up)

        # down (6)

        elif j.get_button(button_down) != 0:

            print "DOWN"
            animation(look_down)

        # left (7)

        elif j.get_button(button_left) != 0:

            print "LEFT"
            animation(look_left)

        # right (5)

        elif j.get_button(button_right) != 0:

            print "RIGHT"
            animation(look_right)

        # SystemButtons

        # Select (0)

        elif j.get_button(button_select) != 0:

            print "SELECT"
            move(tf)

        # MainButtons

        # rectangle-button (12)

        elif j.get_button(button_rectangle) != 0:

            print "RECTANGLE"
            mood_left(look_angry_left)
            mood_right(look_angry_right)

        # X-button (14)

        elif j.get_button(button_cross) != 0:

            print "CROSS"
            mood_left(look_angry_right)
            mood_right(look_angry_left)

        # square-button (15)

        elif j.get_button(button_square) != 0:

            print "SQUARE"
            move(tf)

        # O-button (13)

        elif j.get_button(button_circle) != 0:

            print "CIRCLE"
            mood_left(look_stoned)
            mood_right(look_stoned)

        # shoulder-button

        # right shoulder (11)

        elif j.get_button(button_shoulder_right) != 0:

            print "RIGHT SHOULDER"
            move(tf)

        # left shoulder (10)

        elif j.get_button(button_shoulder_left) != 0:

            print "LEFT SHOULDER"
            move(tf)

        # right trigger (9)

        elif j.get_button(button_trigger_right) != 0:

            print "RIGHT TRIGGER"
            move(tf)

        # left trigger (8)

        elif j.get_button(button_trigger_left) != 0:

            print "LEFT TRIGGER"
            move(tf)

        # thumbstick buttons

        # right thumbstick (2)

        elif j.get_button(button_thumb_right) != 0:

            print "RIGHT THUMBSTICK"
            move(tf)

        # left thumbstick (1)

        elif j.get_button(button_thumb_left) != 0:

            print "LEFT THUMBSTICK"
            move(tf)

        # thumbsticks direction movement

        # STOP

        elif j.get_axis(axis_left_updown) == 0.00 and j.get_axis(axis_right) == 0.00:

            print "CENTER"
            move(tf)

        # left thumbstick directions

        # left thumbstick up

        elif j.get_axis(axis_left_updown) < 0:

            print "LEFT THUMBSTICK UP"
            move(tf)

        # left thumbstick down

        elif j.get_axis(axis_left_updown) > 0:

            print "LEFT THUMBSTICK DOWN"
            move(tf)

        # left thumbstick left

        elif j.get_axis(axis_left_leftright) < 0:

            print "LEFT THUMBSTICK LEFT"
            move(tf)

        # left thumbstick right

        elif j.get_axis(axis_left_leftright) > 0:

            print "LEFT THUMBSTICK RIGHT"
            move(tf)

        # right thumbstick directions

        # right thumbstick up

        elif j.get_axis(axis_right) < 0:

            print "RIGHT THUMBSTICK UP"
            move(tf)

        # right thumbstick down

        elif j.get_axis(axis_right) > 0:

            print "RIGHT THUMBSTICK DOWN"
            move(tf)

        # right thumbstick left

        elif j.get_axis(2) < 0:

            print "RIGHT THUMBSTICK LEFT"
            move(tf)

        # right thumbstick right

        elif j.get_axis(2) > 0:

            print "RIGHT THUMBSTICK RIGHT"
            move(tf)

    else:
        j.quit()
        grid_left.clear()
        grid_right.clear()

# #### THAT'S ALL FOLKS #### #

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    j.quit()
    grid_left.clear()
    grid_right.clear()
