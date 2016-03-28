#!/usr/bin/python

from time import sleep

from Modules.Adafruit_Python_Code.Adafruit_MotorHAT.Adafruit_MotorHAT import Adafruit_MotorHAT

# create an object for the MotorHAT

mh = Adafruit_MotorHAT(addr=0x60)

# define time frame

tf = 0.1

# name the motors

leftMotor_rear = mh.getMotor(1)
rightMotor_rear = mh.getMotor(2)
gun_motor = mh.getMotor(3)


# #### SET UP THE MOTORS #### #

# auto-disabling motors on shutdown

def turn_off_motors():
    leftMotor_rear.run(Adafruit_MotorHAT.RELEASE)
    rightMotor_rear.run(Adafruit_MotorHAT.RELEASE)


# stop the gun

def stop_gun():
    gun_motor.run(Adafruit_MotorHAT.RELEASE)


# fire the gun

def fire():
    gun_motor.setSpeed(35)
    gun_motor.run(Adafruit_MotorHAT.FORWARD)
    sleep(tf)
    print "Fire in the hole !!!"
    gun_motor.run(Adafruit_MotorHAT.RELEASE)
    sleep(tf)


# left motor forward with speed parameter

def left_motor_forward(v_max_left):
    leftMotor_rear.setSpeed(v_max_left)
    leftMotor_rear.run(Adafruit_MotorHAT.FORWARD)


# right motor forward with speed parameter

def right_motor_forward(v_max_right):
    rightMotor_rear.setSpeed(v_max_right)
    rightMotor_rear.run(Adafruit_MotorHAT.FORWARD)


# left motor backward with speed parameter

def left_motor_backward(v_max_left):
    leftMotor_rear.setSpeed(v_max_left)
    leftMotor_rear.run(Adafruit_MotorHAT.BACKWARD)


# right motor forward with speed parameter

def right_motor_backward(v_max_right):
    rightMotor_rear.setSpeed(v_max_right)
    rightMotor_rear.run(Adafruit_MotorHAT.BACKWARD)


# some movement functions for the thumb sticks

# drive forward with speed parameter

def thumb_forward(v_max_left, v_max_right):
    print "Vorwaerts mit Speed L", v_max_left, "R", v_max_right
    left_motor_forward(v_max_left)
    right_motor_forward(v_max_right)
    sleep(tf)


# drive backward with speed parameter

def thumb_backward(v_max_left, v_max_right):
    print "Rueckwaerts mit Speed L", v_max_left, "R", v_max_right
    left_motor_backward(v_max_left)
    right_motor_backward(v_max_right)
    sleep(tf)


# pivot counterclockwise with speed parameter

def thumb_turn_counterclockwise(v_max_left, v_max_right):
    print "Links rum mit Speed L", v_max_left, "R", v_max_right
    left_motor_backward(v_max_left)
    right_motor_forward(v_max_right)
    sleep(tf)


# pivot clockwise with speed parameter

def thumb_turn_clockwise(v_max_left, v_max_right):
    print "Rechts rum mit Speed L", v_max_left, "R", v_max_right
    left_motor_forward(v_max_left)
    right_motor_backward(v_max_right)
    sleep(tf)


# left motor forward with speed parameter

def thumb_left_forward(v_max_left):
    print "L Vorwaerts mit Speed", v_max_left
    left_motor_forward(v_max_left)
    sleep(tf)


# left motor backward with speed parameter

def thumb_left_backward(v_max_left):
    print "L Rueckwaerts mit Speed", v_max_left
    left_motor_backward(v_max_left)
    sleep(tf)


# right motor forward with speed parameter

def thumb_right_forward(v_max_right):
    print "R Vorwaerts mit Speed", v_max_right
    right_motor_forward(v_max_right)
    sleep(tf)


# right motor backward with speed parameter

def thumb_right_backward(v_max_right):
    print "R Rueckwaerts mit Speed", v_max_right
    right_motor_backward(v_max_right)
    sleep(tf)

    # set the speed with the right shoulder trigger

    # def speed():
    #     # if v_max is greater than 70 the motors will start, let's use them
    #     # they can't start with less power (adjust this to your own motors)
    #
    #     if v_max > 70:
    #
    #         leftMotor_rear.setSpeed(v_max)
    #         rightMotor_rear.setSpeed(v_max)
    #
    #     # if v_max is smaller than 70 the motors won't even start, so let's don't use them
    #
    #     else:
    #
    #         turn_off_motors()

    # some movement functions for the direction keys

    # drive forward

    # def forward():
    #     speed()
    #     leftMotor_rear.run(Adafruit_MotorHAT.FORWARD)
    #     rightMotor_rear.run(Adafruit_MotorHAT.FORWARD)
    #     print "Vor mit Speed", v_max
    #     sleep(tf)
    #
    #
    # # drive backward
    #
    # def backward():
    #     speed()
    #     leftMotor_rear.run(Adafruit_MotorHAT.BACKWARD)
    #     rightMotor_rear.run(Adafruit_MotorHAT.BACKWARD)
    #     print "Zurueck mit Speed", v_max
    #     sleep(tf)
    #
    #
    # # pivot counterclockwise
    #
    # def turn_left():
    #     speed()
    #     leftMotor_rear.run(Adafruit_MotorHAT.BACKWARD)
    #     rightMotor_rear.run(Adafruit_MotorHAT.FORWARD)
    #     print "Links mit Speed", v_max
    #     sleep(tf)
    #
    #
    # # pivot clockwise
    #
    # def turn_right():
    #     speed()
    #     leftMotor_rear.run(Adafruit_MotorHAT.FORWARD)
    #     rightMotor_rear.run(Adafruit_MotorHAT.BACKWARD)
    #     print "Rechts mit Speed", v_max
    #     sleep(tf)
