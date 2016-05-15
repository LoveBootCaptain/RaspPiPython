#!/usr/bin/python

import sys
from Modules.Buttons.ButtonConfiguration import *
from Modules.Buttons.ButtonCallbackFunctions import *

# setup the channel as pull up. A push button will ground the pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(brightness, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(display, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(shutdown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reboot, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(escape, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(keyF4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(wifi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bluetooth, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# init everything

print "SETUP SYSTEM\n"

init_display()
init_wifi()
init_bluetooth()

print "\n"
print "SYSTEM READY\n"

# print a little help

print "You can use the following buttons:\n"

print "Button #21 - scroll trough brightness settings"
print "Button #20 - turn display on/off"
print "Button #13 - shutdown the pi"
print "Button #16 - reboot the pi"
print "Button #19 - send ESC Key Command"
print "Button #12 - send F4 Key Command"
print "Button #05 - turn wifi on / off"
print "Button #06 - turn bluetooth on / off\n"

# use event detection for button presses and trigger a callback function from above

GPIO.add_event_detect(display, GPIO.FALLING, callback=set_display_state, bouncetime=500)
GPIO.add_event_detect(brightness, GPIO.FALLING, callback=set_display_brightness, bouncetime=500)
GPIO.add_event_detect(shutdown, GPIO.FALLING, callback=shutdown_action, bouncetime=500)
GPIO.add_event_detect(reboot, GPIO.FALLING, callback=reboot_action, bouncetime=500)
GPIO.add_event_detect(escape, GPIO.FALLING, callback=escape_action, bouncetime=500)
GPIO.add_event_detect(keyF4, GPIO.FALLING, callback=key_f4_action, bouncetime=500)
GPIO.add_event_detect(wifi, GPIO.FALLING, callback=wifi_action, bouncetime=500)
GPIO.add_event_detect(bluetooth, GPIO.FALLING, callback=bluetooth_action, bouncetime=500)

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
