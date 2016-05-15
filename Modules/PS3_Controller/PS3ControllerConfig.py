#!/usr/bin/python

import pygame

print "Pair your PS3 Controller now"

# print "... wait 5 sec"

# for x in range(0, 6):
#     print x
#     sleep(1)


# Init the PS3 Controller

try:

    pygame.init()
    j = pygame.joystick.Joystick(0)
    pygame.joystick.Joystick(0).init()

    if pygame.joystick.get_init():

        print "PS3 Controller connected"

    else:

        print "No Controller Connected. Please pair your PS3 Controller and restart the script."

except StandardError:

    print "No Controller Connected. Please pair your PS3 Controller and restart the script."

# #### SET UP THE CONTROLLER #### #

# set buttons

button_select = 0
button_thumb_left = 1
button_thumb_right = 2
button_start = 3
button_up = 4
button_right = 5
button_down = 6
button_left = 7
button_trigger_left = 8
button_trigger_right = 9
button_shoulder_left = 10
button_shoulder_right = 11
button_triangle = 12
button_circle = 13
button_cross = 14
button_rectangle = 15

# set triggers

trigger_right_axis = 13

# set axis

axis_left_updown = 1
axis_right_updown = 3
axis_left_leftright = 0
axis_right_leftright = 2

# ## naming buttons ## #

# system buttons

BUTTON_SELECT = j.get_button(button_select)
BUTTON_START = j.get_button(button_start)

# d-pad

BUTTON_UP = j.get_button(button_up)
BUTTON_DOWN = j.get_button(button_down)
BUTTON_LEFT = j.get_button(button_left)
BUTTON_RIGHT = j.get_button(button_right)

# action buttons

BUTTON_TRIANGLE = j.get_button(button_triangle)
BUTTON_CROSS = j.get_button(button_cross)
BUTTON_RECTANGLE = j.get_button(button_rectangle)
BUTTON_CIRCLE = j.get_button(button_circle)

# thumbstick buttons

BUTTON_THUMBSTICK_LEFT = j.get_button(button_thumb_left)
BUTTON_THUMBSTICK_RIGHT = j.get_button(button_thumb_right)

# shoulder buttons

BUTTON_SHOULDER_LEFT = j.get_button(button_shoulder_left)
BUTTON_SHOULDER_RIGHT = j.get_button(button_shoulder_right)

# trigger buttons

BUTTON_TRIGGER_LEFT = j.get_button(button_trigger_left)
BUTTON_TRIGGER_RIGHT = j.get_button(button_trigger_right)

# ## naming axis ## #

AXIS_LEFT_UPDOWN = j.get_axis(axis_left_updown)
AXIS_LEFT_LEFTRIGHT = j.get_axis(axis_left_leftright)
AXIS_RIGHT_UPDOWN = j.get_axis(axis_right_updown)
AXIS_RIGHT_LEFTRIGHT = j.get_axis(axis_right_leftright)
