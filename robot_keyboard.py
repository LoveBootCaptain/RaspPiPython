#!/usr/bin/python

import atexit
import sys
from time import sleep

from Modules.Adafruit_Python_Code.Adafruit_MotorHAT.Adafruit_MotorHAT import Adafruit_MotorHAT
from Modules.Adafruit_Python_Code.Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

# create a default object, no changes to I2C address or frequency

mh = Adafruit_MotorHAT(addr=0x60)
sh = PWM(0x40)


# recommended for auto-disabling motors on shutdown!

def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turn_off_motors)

# Set up the motors

leftMotor = mh.getMotor(1)
rightMotor = mh.getMotor(2)

# Define sleep as movement

tf = 0.1
move = sleep


# set the speed to start, from 0 (off) to 255 (max speed)

def speed():
    v_max = 150
    leftMotor.setSpeed(v_max)
    rightMotor.setSpeed(v_max)


# some movement functions for the direction keys

# drive forward

def forward():
    speed()
    leftMotor.run(Adafruit_MotorHAT.FORWARD)
    rightMotor.run(Adafruit_MotorHAT.FORWARD)
    print "Vor"
    move(tf)


# drive backward

def backward():
    speed()
    leftMotor.run(Adafruit_MotorHAT.BACKWARD)
    rightMotor.run(Adafruit_MotorHAT.BACKWARD)
    print "Zurueck"
    move(tf)


# pivot counterclockwise

def turn_left():
    speed()
    leftMotor.run(Adafruit_MotorHAT.BACKWARD)
    rightMotor.run(Adafruit_MotorHAT.FORWARD)
    print "Links"
    move(tf)


# pivot clockwise

def turn_right():
    speed()
    leftMotor.run(Adafruit_MotorHAT.FORWARD)
    rightMotor.run(Adafruit_MotorHAT.BACKWARD)
    print "Rechts"
    move(tf)


# better don't try this at home

try:

    while True:
        print "Enter the Command:",
        a = raw_input()  # Fetch the input from the terminal
        if a == 'w':
            forward()  # Move forward
        elif a == 'a':
            turn_left()  # Turn left
        elif a == 'd':
            turn_right()  # Turn Right
        elif a == 's':
            backward()  # Move back
        elif a == 'x':
            turn_off_motors()  # Stop
        elif a == 'z':
            print "Exiting"  # Exit
            sys.exit()
        else:
            print "Wrong Command, Please Enter Again"
        move(tf)

# When Start or CTRL+C is pressed clean this up

except KeyboardInterrupt:
    sys.exit()
