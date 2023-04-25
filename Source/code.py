"""
# Original #
# SPDX-FileCopyrightText: 2021 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Modified #
author     : Ethan Herndon
date       : 4/23/23
filename   : code.py
desc       : Macro pad for media capture and game shortcuts
References : 1. https://learn.adafruit.com/neokey-emoji-keyboard/coding-the-neokey-emoji-keyboard
			 2. https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html
			 3. https://docs.circuitpython.org/projects/hid/en/4.1.7/api.html
"""

import time
import board
import busio
from adafruit_neokey.neokey1x4 import NeoKey1x4
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# use STEMMA I2C bus on RP2040 QT Py
i2c_bus = busio.I2C(board.SCL1, board.SDA1)

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x30)

#  create a keyboard object
keyboard = Keyboard(usb_hid.devices)

print("NeoKey Emoji keyboard - Windows")

#  states for key presses
key_0_state = False
key_1_state = False
key_2_state = False
key_3_state = False

while True:
    #  switch debouncing
    #  also turns off NeoPixel on release
    if not neokey[0] and key_0_state:
        key_0_state = False
        neokey.pixels[0] = 0x0
    if not neokey[1] and key_1_state:
        key_1_state = False
        neokey.pixels[1] = 0x0
    if not neokey[2] and key_2_state:
        key_2_state = False
        neokey.pixels[2] = 0x0
    if not neokey[3] and key_3_state:
        key_3_state = False
        neokey.pixels[3] = 0x0

    #  if 1st neokey is pressed...
    if neokey[0] and not key_0_state:
        print("Button A")
        #  turn on NeoPixel
        neokey.pixels[0] = 0xFF0000
        #  open NVIDIAs Performance Overlay
        keyboard.send(Keycode.ALT, Keycode.R)        
        #  update key state
        key_0_state = True

    #  if 2nd neokey is pressed...
    if neokey[1] and not key_1_state:
        print("Button B")
        #  turn on NeoPixel
        neokey.pixels[1] = 0xFFFF00
        #  start NVIDIAs Shadowplay
        keyboard.send(Keycode.ALT, Keycode.F9)
        #  update key state
        key_1_state = True

    #  if 3rd neokey is pressed...
    if neokey[2] and not key_2_state:
        print("Button C")
        #  turn on NeoPixel
        neokey.pixels[2] = 0x00FF00
        #  take Steam screenshot
        keyboard.send(Keycode.KEYPAD_MINUS)
        #  update key state
        key_2_state = True

    #  if 4th neokey is pressed...
    if neokey[3] and not key_3_state:
        print("Button D")
        #  turn on NeoPixel
        neokey.pixels[3] = 0x00FFFF
		# highlight team for Battlezone Combat Commander
        keyboard.send(Keycode.F12)
        #  update key state
        key_3_state = True
