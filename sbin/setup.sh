#!/bin/bash

# this script is meant to be run on the raspberry pi 4

# echo on
set -x

# stop on errors
set -e

# install dependencies


# web and web socket server - https://gitlab.com/pgjones/quart
sudo pip3 install \
quart \
websockets \
flask \
flask-cors \
argparse

# Blinka needed by motorkit :/
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

# motorkit
sudo pip3 install adafruit-circuitpython-motorkit

# proximity sensor
sudo pip3 install adafruit-circuitpython-vcnl4040
