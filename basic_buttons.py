#!/usr/bin/python

import os
from time import sleep
import sys

import RPi.GPIO as GPIO

# it will work on any GPIO channel

wifi = 22       # GPIO channel 22 for WiFi
reboot = 27     # GPIO channel 27 for Reboot/Shutdown
button = 23     # GPIO channel 23 for debug short/long
script = 17     # GPIO channel 17 # for Script starts

# setup the channel as input with a 50K Ohm pull up. A push button will ground the pin,

GPIO.setmode(GPIO.BCM)
GPIO.setup(wifi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reboot, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(script, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# print a little help

print "SYSTEM READY"
print "Button #17 - start script"
print "Button #22 - start wifi (short)"
print "Button #22 - stop wifi (long)"
print "Button #23 - debug button (short)"
print "Button #23 - debug button (long)"
print "Button #27 - reboot RoboPi (short)"
print "Button #27 - shutdown RoboPi (long)"


# creating a falling edge for the wifi button

def wifi_action(wifi):

    # print a message when the button is pressed

    print('Button press = negative edge detected on channel %s' % wifi)

    # set the button counter

    button_press_timer = 0

    # start the loop

    while True:

        # while button is still pressed down

        if not GPIO.input(wifi):

            # keep counting until button is released

            button_press_timer += 1

            # print the button timer

            print button_press_timer

        # button is released, figure out for how long

        else:

            # pressed for > 5 seconds

            if button_press_timer > 5:

                print "long press > 5 : ", button_press_timer

                # do what you need to do before the action

                print "Shutting Wifi down"

                # this will turn off the wifi

                os.system("sudo ifdown wlan0")

                sleep(3)
                print "wifi offline"
                return

            # press for > 2 < 5 seconds

            elif button_press_timer > 2:

                print "short press > 2 < 5 : ", button_press_timer

                # do what you need to do before a reboot

                print "Turning Wifi back on"

                # this will turn the wifi on

                os.system("sudo ifup wlan0")

                sleep(3)
                print "wifi online"
                return

            # reset the timer

            button_press_timer = 0

        # return to while

        sleep(1)


# creating a falling edge for the reboot/shutdown button

def system_action(reboot):

    # print a message when the button is pressed

    print('Button press = negative edge detected on channel %s' % reboot)

    # set the button counter

    button_press_timer = 0

    # start the loop

    while True:

        # while button is still pressed down

        if not GPIO.input(reboot):

            # keep counting until button is released

            button_press_timer += 1
            print button_press_timer

        # button is released, figure out for how long

        else:

            # pressed for > 5 seconds

            if button_press_timer > 5:

                print "long press > 5 : ", button_press_timer

                # do what you need to do before the action

                print "Shutting RoboPi down"

                # this will shutdown your pi

                os.system("sudo shutdown now")
                return

            # press for > 2 < 5 seconds

            elif button_press_timer > 2:

                print "short press > 2 < 5 : ", button_press_timer

                # do what you need to do before a reboot

                print "Reboot RoboPi"

                # this will reboot your pi

                os.system("sudo reboot")
                return

            # reset the timer

            button_press_timer = 0

        # return to while

        sleep(1)


# a simple custom script starter... press the button to start a python script

def script_action(script):

    # print a message when the button is pressed

    print('Button press = negative edge detected on channel %s' % script)

    # start the script

    print "starting your script now..."
    sleep(1)
    os.system("sudo python /home/pi/robot/robot.py")


# creating a falling edge for the quit button

def button_action(button):

    # print a message when the button is pressed

    print('Button press = negative edge detected on channel %s' % script)

    # quit this program

    print "quit this program...", button
    sleep(1)
    GPIO.cleanup()
    sys.exit()


# setup the thread, detect a falling edge for GPIO's and debounce them with 2000mSec

GPIO.add_event_detect(wifi, GPIO.FALLING, callback=wifi_action, bouncetime=2000)
GPIO.add_event_detect(reboot, GPIO.FALLING, callback=system_action, bouncetime=2000)
GPIO.add_event_detect(script, GPIO.FALLING, callback=script_action, bouncetime=2000)
GPIO.add_event_detect(button, GPIO.FALLING, callback=button_action, bouncetime=2000)


# assume this is the main code...

try:

    while True:

        # do whatever
        # while "waiting" for falling edge on port 23

        sleep(2)

except KeyboardInterrupt:

    # clean up GPIO on CTRL+C exit

    GPIO.cleanup()
    sys.exit()
GPIO.cleanup()
sys.exit()
