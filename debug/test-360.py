#!/usr/bin/env python3

# see, https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/#Interrupts_with_RPiGPIO_wait_for_edge

import time
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

MOTOR_I2C_ADDRESS = 0x60
SWITCH_PIN = 24
SWITCH_TIMEOUT = 30

kit = MotorKit(MOTOR_I2C_ADDRESS)
motor = kit.motor4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("testing motor")

# the motor is not strong enough to start at 0.4, but once
# it's moving, it can keep going at that speed
motor.throttle = -0.5
time.sleep(0.25)
motor.throttle = -0.75
time.sleep(0.25)
motor.throttle = -1

for i in range(0, 1):
    # wait to read switch pin until we are off the trigger
    time.sleep(1)

    # Not sure why this doesn't work, but it returns after a few seconds
    #  without the switch being triggered
    # GPIO.wait_for_edge(SWITCH_PIN, GPIO.BOTH) # , SWITCH_TIMEOUT)

    while GPIO.input(SWITCH_PIN) == GPIO.LOW:
        time.sleep(0.1)


motor.throttle = 0
