#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time
import uinput

# global variables for button logic

display_state = 0
display_brightness_toggle = 0  # will start from medium settings to low and than round robbin
wifi_state = 0
bluetooth_state = 0

# setup key commands to send

keyboard_command = uinput.Device([
    uinput.KEY_ESC,
    uinput.KEY_F4,
])


# some init functions

def init_display():

    global display_state
    global display_brightness_toggle

    # turn the display on for sure
    os.system("echo 0 > /sys/class/backlight/rpi_backlight/bl_power")
    display_state = True
    print "display:             enabled"

    # set the displays brightness to medium setting
    os.system("echo 100 > /sys/class/backlight/rpi_backlight/brightness")
    display_brightness_toggle = 3
    print "display brightness:  medium"


def init_wifi():

    global wifi_state

    # disable wifi for sure
    os.system("sudo ifconfig wlan0 down")
    wifi_state = False
    print "wifi:                disabled"


def init_bluetooth():

    global bluetooth_state

    # disable bluetooth for sure
    os.system("echo 'power off' | bluetoothctl")
    time.sleep(3)
    bluetooth_state = False
    print "bluetooth:            disabled"


# this are the main callback functions which will be triggered by buttons events

# turn the display on / off

def set_display_state(display):

    global display_state

    if not GPIO.input(display):

        if not display_state:

            print "Display On", display
            os.system("echo 0 > /sys/class/backlight/rpi_backlight/bl_power")
            display_state = True
            return

        elif display_state:

            print "Display Off", display
            os.system("echo 1 > /sys/class/backlight/rpi_backlight/bl_power")
            display_state = False
            return


# scroll through some brightness settings round robbin starting from medium

def set_display_brightness(brightness):

    global display_brightness_toggle

    if not GPIO.input(brightness):

        if display_brightness_toggle == 0:

            print "SuperBright", brightness
            os.system("echo 255 > /sys/class/backlight/rpi_backlight/brightness")
            display_brightness_toggle = 1
            return

        elif display_brightness_toggle == 1:

            print "Bright", brightness
            os.system("echo 160 > /sys/class/backlight/rpi_backlight/brightness")
            display_brightness_toggle = 2
            return

        elif display_brightness_toggle == 2:

            print "Medium", brightness
            os.system("echo 100 > /sys/class/backlight/rpi_backlight/brightness")
            display_brightness_toggle = 3
            return

        elif display_brightness_toggle == 3:

            print "Low", brightness
            os.system("echo 55 > /sys/class/backlight/rpi_backlight/brightness")
            display_brightness_toggle = 4
            return

        else:

            print "SuperLow", brightness
            os.system("echo 25 > /sys/class/backlight/rpi_backlight/brightness")
            display_brightness_toggle = 0
            return


# shutdown the pi

def shutdown_action(shutdown):

    print "shutdown", shutdown
    os.system("sudo shutdown -P now")


# reboot the pi

def reboot_action(reboot):

    print "reboot", reboot
    os.system("sudo shutdown -r now")


# send ESC Key command

def escape_action(escape):

    print "ESC", escape
    keyboard_command.emit_click(uinput.KEY_ESC)


# send F4 Key command

def key_f4_action(keyF4):

    print "F4", keyF4
    keyboard_command.emit_click(uinput.KEY_F4)


def wifi_action(wifi):

    global wifi_state

    if not GPIO.input(wifi):

        if not wifi_state:

            print "WiFi On", wifi
            os.system("sudo ifconfig wlan0 up")
            wifi_state = True
            return

        elif wifi_state:

            print "WiFi Off", wifi
            os.system("sudo ifconfig wlan0 down")
            wifi_state = False
            return


def bluetooth_action(bluetooth):

    global bluetooth_state

    if not GPIO.input(bluetooth):

        if not bluetooth_state:

            os.system("echo 'power on' | bluetoothctl")
            print "Bluetooth On", bluetooth
            time.sleep(3)
            os.system("echo 'connect 8E:F0:B5:FE:9E:F3' | bluetoothctl")
            print "Connected to Controler"
            bluetooth_state = True
            return

        elif bluetooth_state:

            os.system("echo 'power off' | bluetoothctl")
            time.sleep(3)
            print "Bluetooth Off + Controler disconnected", bluetooth
            bluetooth_state = False
            return
