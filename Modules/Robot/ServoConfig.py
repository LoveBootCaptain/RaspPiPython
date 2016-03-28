#!/usr/bin/python

from Modules.Adafruit_Python_Code.Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM

# create an object for servo HAT

sh = PWM(0x40)

# Set the Servo Frequency

sh.setPWMFreq(60)  # Set frequency to 60 Hz

# #### SET THE SERVOS #### #

# name the servos

servoCamPan = 0
servoCamTilt = 1
servoGunPan = 2
servoGunTilt = 3
servoFront = 8
servoRear = 9

# # set the servo values

# Sensor Front

servoFrontMin = 330
servoFrontMax = 530

# Sensor Rear

servoRearMin = 330
servoRearMax = 530

# Cam Pan Left Right

servoCamPanMin = 155  # Right
servoCamPanMax = 570  # Left

# Cam Tilt Up Down

servoCamTiltMin = 170  # Up
servoCamTiltMax = 450  # Down

# Gun Pan Left Right

servoGunPanMin = 140  # Right
servoGunPanMax = 570  # Left

# Gun Tilt Up Down

servoGunTiltMin = 240  # Up
servoGunTiltMax = 480  # Down

# Zero = Middle

servoCamPanZero = servoCamPanMid = ((servoCamPanMax - servoCamPanMin) / 2) + servoCamPanMin
servoCamTiltZero = servoCamTiltMid = ((servoCamTiltMax - servoCamTiltMin) / 2) + servoCamTiltMin
servoGunPanZero = servoGunPanMid = ((servoCamPanMax - servoCamPanMin) / 2) + servoCamPanMin
servoGunTiltZero = servoGunTiltMid = ((servoCamTiltMax - servoCamTiltMin) / 2) + servoCamTiltMin
servoFrontZero = servoFrontMid = ((servoFrontMax - servoFrontMin) / 2) + servoFrontMin
servoRearZero = servoRearMid = ((servoRearMax - servoRearMin) / 2) + servoRearMin


# define zero the servos

def zero_servos():
    sh.setPWM(servoCamPan, 0, servoCamPanZero)
    sh.setPWM(servoCamTilt, 0, servoCamTiltZero)
    sh.setPWM(servoGunPan, 0, servoGunPanZero)
    sh.setPWM(servoGunTilt, 0, servoGunTiltZero)
    sh.setPWM(servoFront, 0, servoFrontZero)
    sh.setPWM(servoRear, 0, servoRearZero)
