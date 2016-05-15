#!/usr/bin/python

# setup some buttons
#
# every button has some key/values which are stored in its dictionary
# use them as following:
#
# name          - just for naming the button and it's function
# pin           - the GPIO Pin
# pin_name      - just for printing a fine 2-digits number
# description   - explains the useful thing that button will do
# callback      - set the callback function from /Modules/Buttons/ButtonCallbackFunctions.py
#
# just add more buttons the same way or create new callback functions

button_1 = {

    'name': 'brightness',
    'pin': 21,
    'pin_name': '21',
    'description': 'scroll trough brightness settings',
    'callback': 'set_display_brightness'

}

button_2 = {

    'name': 'display',
    'pin': 20,
    'pin_name': '20',
    'description': 'turn display on / off',
    'callback': 'set_display_state'

}

button_3 = {

    'name': 'shutdown',
    'pin': 13,
    'pin_name': '13',
    'description': 'shutdown the pi',
    'callback': 'shutdown_action'

}

button_4 = {

    'name': 'reboot',
    'pin': 16,
    'pin_name': '16',
    'description': 'reboot the pi',
    'callback': 'reboot_action'

}

button_5 = {

    'name': 'wifi',
    'pin': 5,
    'pin_name': '05',
    'description': 'turn wifi on / off',
    'callback': 'wifi_action'

}

button_6 = {

    'name': 'bluetooth',
    'pin': 6,
    'pin_name': '06',
    'description': 'turn bluetooth on / off',
    'callback': 'bluetooth_action'

}

button_configuration = [

    button_1,
    button_2,
    button_3,
    button_4,
    button_5,
    button_6

]

# for debugging

# for button in button_configuration:
#     print "Button #%s - %s: %s - callback: %s" % (button['pin_name'], button['name'], button['description'], button['callback'])
#     print "Button #{} - {}: {} - callback: {}".format(button['pin_name'], button['name'], button['description'], button['callback'])
# print '\n'
