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
#
# this creates a unsorted test.json file with the configuration
# rename test.json to button_configuration.json to make it work with the buttons_control_pi.py program

import json

button_configuration = {

    'button_1': {

        'name': 'brightness',
        'pin': 21,
        'pin_name': '21',
        'description': 'scroll trough brightness settings',
        'callback': 'set_display_brightness'

    },
    'button_2': {

        'name': 'display',
        'pin': 20,
        'pin_name': '20',
        'description': 'turn display on / off',
        'callback': 'set_display_state'

    },
    'button_3': {

        'name': 'shutdown',
        'pin': 13,
        'pin_name': '13',
        'description': 'shutdown the pi',
        'callback': 'shutdown_action'

    },
    'button_4': {

        'name': 'reboot',
        'pin': 16,
        'pin_name': '16',
        'description': 'reboot the pi',
        'callback': 'reboot_action'

    },
    'button_5': {

        'name': 'wifi',
        'pin': 5,
        'pin_name': '05',
        'description': 'turn wifi on / off',
        'callback': 'wifi_action'

    },
    'button_6': {

        'name': 'bluetooth',
        'pin': 6,
        'pin_name': '06',
        'description': 'turn bluetooth on / off',
        'callback': 'bluetooth_action'

    },

}

# for debugging

# data = open('test.json').read()
# test_configuration = json.loads(data)

# for button in button_configuration:

for button in button_configuration:
    print 'Button #{} - {}: {} - callback: {}'.format(
        button_configuration[button]['pin_name'],
        button_configuration[button]['name'],
        button_configuration[button]['description'],
        button_configuration[button]['callback']
    )

print '\n'

output_file = open('test.json', 'w')
json.dump(button_configuration, output_file, indent=2)
output_file.close()
