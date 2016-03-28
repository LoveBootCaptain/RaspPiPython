#!/usr/bin/python

import sys

# import RPi.GPIO as GPIO
import pygame

from Modules.Robot.MotorConfig import *
from Modules.Robot.ServoConfig import *
from Modules.BrightPiLed.LEDConfig import *
from Modules.PS3_Controller.ControllerConfig import *

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


# zero the servos on startup

zero_servos()

# auto-disabling motors on startup

turn_off_motors()
stop_gun()

# #### FUNCTIONS #### #

light = 0

# #### PLAY THE GAME #### #

# better don't try this at home

try:

    # this will run until you press the START Button (3)

    while j.get_button(button_start) == 0:

        # process event handlers

        pygame.event.pump()

        # get speed data from thumbsticks Left Axis (1) Right Axis (3)

        v_max_left = int((abs(j.get_axis(axis_left)) * 255))
        v_max_right = int((abs(j.get_axis(axis_right)) * 255))

        # # speed for D-Pad controlling with RightTrigger (13)
        #
        # if j.get_axis(trigger_right) != 0.00:
        #
        #     # get the speed parameter for setting up the motors
        #
        #     v_max = int((abs(j.get_axis(trigger_right)) * 255))
        #
        # elif j.get_axis(trigger_right) == 0.00:
        #
        #     # if the trigger is not pushed set the speed parameter to 0
        #
        #     v_max = 0

        # directions D-Pad

        # up (4)

        if j.get_button(button_up) != 0:

            # forward()

            if servoGunTiltZero > servoGunTiltMin:
                sh.setPWM(servoGunTilt, 0, servoGunTiltZero)
                servoGunTiltZero -= 1
                print "Gun Down", servoGunTiltZero

        # down (6)

        elif j.get_button(button_down) != 0:

            # backward()

            if servoGunTiltZero < servoGunTiltMax:
                sh.setPWM(servoGunTilt, 0, servoGunTiltZero)
                servoGunTiltZero += 1
                print "Gun Up", servoGunTiltZero

        # left (7)

        elif j.get_button(button_left) != 0:

            # turn_left()

            if servoGunPanZero < servoGunPanMax:
                sh.setPWM(servoGunPan, 0, servoGunPanZero)
                servoGunPanZero += 1
                print "Gun Left", servoGunPanZero

        # right (5)

        elif j.get_button(button_right) != 0:

            # turn_right()

            if servoGunPanZero > servoGunPanMin:
                sh.setPWM(servoGunPan, 0, servoGunPanZero)
                servoGunPanZero -= 1
                print "Gun Right", servoGunPanZero

        # SystemButtons

        # Select (0)

        elif j.get_button(button_select) != 0:

            if light == 0:

                print "Licht AN"
                lights_on()
                light = 1
                sleep(0.3)

            elif light == 1:

                print "IR AN"
                lights_ir()
                light = 2
                sleep(0.3)

            else:

                print "Licht AUS"
                lights_off()
                light = 0
                sleep(0.3)

        # MainButtons

        # rectangle-button (12)

        elif j.get_button(button_rectangle) != 0:

            if servoCamTiltZero > servoCamTiltMin:
                sh.setPWM(servoCamTilt, 0, servoCamTiltZero)
                servoCamTiltZero -= 1
                print "Dreieck + Cam Up", servoCamTiltZero

        # X-button (14)

        elif j.get_button(button_cross) != 0:

            if servoCamTiltZero < servoCamTiltMax:
                sh.setPWM(servoCamTilt, 0, servoCamTiltZero)
                servoCamTiltZero += 1
                print "Kreuz + Cam Down", servoCamTiltZero

        # square-button (15)

        elif j.get_button(button_square) != 0:

            if servoCamPanZero < servoCamPanMax:
                sh.setPWM(servoCamPan, 0, servoCamPanZero)
                servoCamPanZero += 1
                print "Viereck + Cam Left", servoCamPanZero

        # O-button (13)

        elif j.get_button(button_circle) != 0:

            if servoCamPanZero > servoCamPanMin:
                sh.setPWM(servoCamPan, 0, servoCamPanZero)
                servoCamPanZero -= 1
                print "Kreis + Cam Right", servoCamPanZero

        # shoulder-button

        # right shoulder (11)

        elif j.get_button(button_shoulder_right) != 0:

            servoCamPanZero = servoCamPanMid
            servoCamTiltZero = servoCamTiltMid
            sh.setPWM(servoCamPan, 0, servoCamPanMid)
            sh.setPWM(servoCamTilt, 0, servoCamTiltMid)
            print "RS + Center the Cam"

        # left shoulder (10)

        elif j.get_button(button_shoulder_left) != 0:

            servoGunPanZero = servoGunPanMid
            servoGunTiltZero = servoGunTiltMin
            sh.setPWM(servoGunPan, 0, servoGunPanMid)
            sh.setPWM(servoGunTilt, 0, servoGunTiltMin)
            print "LS + Center the Gun"

        # right trigger (9)

        elif j.get_button(button_trigger_right) != 0:

            print "RT"
            sleep(tf)

        # left trigger (8)

        elif j.get_button(button_trigger_left) != 0:

            print "LT"
            fire()

        # thumbstick buttons

        # right thumbstick (2)

        elif j.get_button(button_thumb_right) != 0:

            print "RTS"
            sleep(tf)

        # left thumbstick (1)

        elif j.get_button(button_thumb_left) != 0:

            print "LTS"
            sleep(tf)

        # thumbsticks direction movement

        # STOP

        elif j.get_axis(axis_left) == 0.00 and j.get_axis(axis_right) == 0.00:

            turn_off_motors()

        # forward

        elif j.get_axis(axis_left) < 0 and j.get_axis(axis_right) < 0:  # LThumbStickUp and RThumbStickUp

            if v_max_left and v_max_right > 70:

                thumb_forward(v_max_left, v_max_right)

            else:

                turn_off_motors()

        # backward

        elif j.get_axis(axis_left) > 0 and j.get_axis(axis_right) > 0:  # LThumbStickDown and RThumbStickDown

            if v_max_left and v_max_right > 70:

                thumb_backward(v_max_left, v_max_right)

            else:

                turn_off_motors()

        # turn left

        elif j.get_axis(axis_left) < 0 < j.get_axis(axis_right):  # LThumbStickUp and RThumbStickDown

            if v_max_left and v_max_right > 70:

                thumb_turn_clockwise(v_max_left, v_max_right)

            else:

                turn_off_motors()

        # turn right

        elif j.get_axis(axis_left) > 0 > j.get_axis(axis_right):  # LThumbStickDown and RThumbStickUp

            if v_max_left and v_max_right > 70:

                thumb_turn_counterclockwise(v_max_left, v_max_right)

            else:

                turn_off_motors()

        # left thumbstick directions

        # left thumbstick up

        elif j.get_axis(axis_left) < 0:

            if v_max_left > 70:

                thumb_left_forward(v_max_left)

            else:

                turn_off_motors()

        # left thumbstick down

        elif j.get_axis(axis_left) > 0:

            if v_max_left > 70:

                thumb_left_backward(v_max_left)

            else:

                turn_off_motors()

        # left thumbstick left

        elif j.get_axis(0) < 0:

            print "LTSL"
            sleep(tf)

        # left thumbstick right

        elif j.get_axis(0) > 0:

            print "LTSR"
            sleep(tf)

        # right thumbstick directions

        # right thumbstick up

        elif j.get_axis(axis_right) < 0:

            if v_max_right > 70:

                thumb_right_forward(v_max_right)

            else:

                turn_off_motors()

        # right thumbstick down

        elif j.get_axis(axis_right) > 0:

            if v_max_right > 70:

                thumb_right_backward(v_max_right)

            else:

                turn_off_motors()

        # right thumbstick left

        elif j.get_axis(2) < 0:

            print "RTSL"
            sleep(tf)

        # right thumbstick right

        elif j.get_axis(2) > 0:

            print "RTSR"
            sleep(tf)

    else:
        zero_servos()
        turn_off_motors()
        lights_off()
        stop_gun()
        j.quit()
        sys.exit()

# #### THAT'S ALL FOLKS #### #

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    zero_servos()
    turn_off_motors()
    lights_off()
    stop_gun()
    j.quit()
    sys.exit()
