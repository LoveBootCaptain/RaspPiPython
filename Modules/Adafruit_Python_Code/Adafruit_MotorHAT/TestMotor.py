#!/usr/bin/python
import atexit
import time

from Adafruit_MotorHAT import Adafruit_MotorHAT

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)


# recommended for auto-disabling motors on shutdown!
def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turn_off_motors)

myMotor = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)

for i in range(0, 3):

    print "Forward! "
    myMotor.run(Adafruit_MotorHAT.FORWARD)

    print "\tSpeed up..."
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "\tSlow down..."
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "Backward! "
    myMotor.run(Adafruit_MotorHAT.BACKWARD)

    print "\tSpeed up..."
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "\tSlow down..."
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print "Release"
    myMotor.run(Adafruit_MotorHAT.RELEASE)
    time.sleep(1.0)
