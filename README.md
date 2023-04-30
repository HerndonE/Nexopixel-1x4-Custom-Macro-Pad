
# Nexopixel 1x4 Custom Macro Pad

![GitHub top language](https://img.shields.io/github/languages/top/HerndonE/Nexopixel-1x4-Custom-Macro-Pad)

### Introduction
Using the Adafruit NeoKey 1x4 QT I2C Breakout, I customized specific keycodes for media capture, and game play.

### Keycode Setup
Each neokey has a set keycode to perform a desired function.

This is a basic illustration of the Nexopixel 1x4 and its corresponding neokey values.


![](https://github.com/HerndonE/Nexopixel-1x4-Custom-Macro-Pad/blob/main/Images/keycodeDrawing.png)


1. ```Neokey 0``` has a keycode set for NVIDIAs Performance Overlay.
2. ```Neokey 1``` has a keycode set for NVIDIAs Shadowplay.
3. ```Neokey 2``` has a keycode set for taking a Steam screenshot.
4. ```Neokey 3``` has a keycode set for highlighting all team members in Battlezone Combat Commnder.

### References
1. [Coding the NeoKey Emoji Keyboard](https://learn.adafruit.com/neokey-emoji-keyboard/coding-the-neokey-emoji-keyboard)
2. [Source code for adafruit_hid.keycode](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html)
3. [Adafruit HID Library](https://docs.circuitpython.org/projects/hid/en/4.1.7/api.html)