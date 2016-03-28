#!/usr/bin/python
import random

from robot_ps3_controller import *

mh = Adafruit_MotorHAT(addr=0x60)
sh = PWM(0x40)

min_dist = 70


def autonomy():
    no_problem = True
    while no_problem:
        sh.setPWM(servoFront, 0, servoFrontZero)
        dist = us_dist(15)
        if dist > min_dist:
            print "Forward is fine !!"
            forward()
        else:
            print "Stuff is in the way !!"
            turn_off_motors()
            sh.setPWM(servoFront, 0, servoFrontMin)
            left_dir = us_dist(15)
            sh.setPWM(servoFront, 0, servoFrontMax)
            right_dir = us_dist(15)

            if left_dir > right_dir and left_dir > min_dist:
                print "Choose left"
                turn_left()
            elif left_dir < right_dir and right_dir > min_dist:
                print "Choose right"
                turn_right()
            else:
                print "No good option... REVERSE !!"
                backward()

                rot_choices = [turn_right(), turn_left()]
                rotation = rot_choices[random.randrange(0, 2)]
                rotation()

        turn_off_motors()

turn_off_motors()

sh.setPWM(servoFront, 0, servoFrontZero)
move(3)

autonomy()

