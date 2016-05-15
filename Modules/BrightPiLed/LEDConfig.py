#!/usr/bin/python

from Modules.BrightPiLed.BrightPILed import BrightPI

# create a default object, no changes to I2C address or frequency

ledlight = BrightPI(1)


# #### control the lights #### #

# white LED'S on


def lights_led():
    print "Turn white LED's ON"
    ledlight.reset()
    ledlight.led_all_on()
    # os.system("sudo i2cset -y 1 0x70 0x00 0x5a")


# infrared LED'S on

def lights_ir():
    print "Turn IR LED ON"
    ledlight.reset()
    ledlight.ir_all_on()
    # os.system("sudo i2cset -y 1 0x70 0x00 0xa5")


# all LED'S off

def lights_off():
    print "Turn all the LED's OFF"
    ledlight.reset()
    # os.system("sudo i2cset -y 1 0x70 0x00 0x00")
