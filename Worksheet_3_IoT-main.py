# Imports go at the top
from microbit import *


isOn=False

# Code in a 'while True:' loop repeats forever
while True:

    if button_a.was_pressed():

        if isOn == True:
            pin0.write_digital(0)
            isOn = False
        else:
            pin0.write_digital(1)
            isOn = True

       

