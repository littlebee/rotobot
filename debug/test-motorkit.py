#!/usr/bin/env python3

# from :
# https://github.com/adafruit/Adafruit_CircuitPython_MotorKit/blob/main/README.rst#usage-example

import time
from adafruit_motorkit import MotorKit

MOTOR_I2C_ADDRESS = 0x60

kit = MotorKit(MOTOR_I2C_ADDRESS)

motor = kit.motor4

print("testing motor for 10 seconds")
# the motor is not strong enough to start at 0.4, but once
# it's moving, it can keep going at that speed
motor.throttle = 0.5
time.sleep(0.25)
motor.throttle = 0.4
time.sleep(10)
motor.throttle = 0
