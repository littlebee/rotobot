#!/usr/bin/env python3

# see, https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/#Interrupts_with_RPiGPIO_wait_for_edge

import time
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

MOTOR_I2C_ADDRESS = 0x60
SWITCH_PIN = 24
SWITCH_TIMEOUT = 300

kit = MotorKit(MOTOR_I2C_ADDRESS)
motor = kit.motor4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print(f"pin {SWITCH_PIN} value: {GPIO.input(SWITCH_PIN)}")
    time.sleep(0.1)
