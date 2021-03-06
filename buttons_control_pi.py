#!/usr/bin/python

import sys
import json

from Modules.Buttons.ButtonCallbackFunctions import *
# from Modules.Buttons.ButtonConfiguration import *

# setup the channel as pull up. A push button will ground the pin

GPIO.setmode(GPIO.BCM)

# read the json config file

data = open('./Modules/Buttons/button_configuration.json').read()
button_configuration = json.loads(data)

# set up the GPIO's the smart way

for button in button_configuration:
    GPIO.setup(button_configuration[button]['pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# init everything

print "SETUP SYSTEM\n"

init_display()
init_wifi()
init_bluetooth()

print "\n"
print "SYSTEM READY\n"

# print a little help

print "You can use the following buttons:\n"

# print the button layout the smart way

for button in button_configuration:
    print "Button #{} - {}: {} - callback: {}".format(
        button_configuration[button]['pin_name'],
        button_configuration[button]['name'],
        button_configuration[button]['description'],
        button_configuration[button]['callback']
    )

print '\n'

# use event detection for button presses and trigger a callback function and do it smart

for button in button_configuration:
    GPIO.add_event_detect(button_configuration[button]['pin'], GPIO.FALLING, callback=button_configuration[button]['callback'], bouncetime=500)

# assume this is the main code...

try:

    while True:
        # do whatever
        # while "waiting" for falling edge on GPIO ports

        time.sleep(2)

except KeyboardInterrupt:

    # clean up GPIO on CTRL+C exit
    init_display()
    init_wifi()
    init_bluetooth()
    GPIO.cleanup()
    sys.exit()

# clean up GPIO on exit
init_display()
init_wifi()
init_bluetooth()
GPIO.cleanup()
sys.exit()
