import sys
import time

from pymata4 import pymata4

"""
Setup a pin for PWM (aka analog) output and output
some different values.
"""

PINS = (5, 6, 9, 10)

def setup_pins(board, pins):
    for pin in pins:
        board.set_pin_mode_pwm_output(pin)

def set_pwm(board, pin, width):
    board.pwm_write(pin, width)

def test_pwm(board, pins, width):
    for pin in pins:
        print('Set pin')
        set_pwm(board, pin, width)
        time.sleep(1)
        print('Unset pin')
        set_pwm(board, pin, 0)
        time.sleep(1)


board = pymata4.Pymata4()
setup_pins(board, PINS)
# test_pwm(board, PINS, 128)


# here we clean up after the program completes.
board.shutdown()
sys.exit(0)

# def set_intensity(my_board, pin):
#     """
#     This function will set an LED and set it to
#     several PWM intensities.
#     :param my_board: an PymataExpress instance
#     :param pin: pin to be controlled
#     """

#     # set the pin mode
#     print('pwm_analog_output example')
#     my_board.set_pin_mode_pwm_output(pin)

#     # set the intensities with analog_write
#     print('Maximum Intensity')
#     my_board.pwm_write(pin, 255)
#     time.sleep(.5)
#     print('Mid Range Intensity')
#     my_board.pwm_write(pin, 128)
#     time.sleep(.5)
#     print('Off')
#     my_board.pwm_write(pin, 0)


