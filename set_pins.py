import sys
import time
import json
from os import system

from pymata4 import pymata4

PINS = (5, 6, 9, 10)

OPTIONS = '1 Forward \n 2 Reverse \n 3 Turn Right \n 4 Turn Left \n\n'

def setup_pins(board, pins):
    for pin in pins:
        board.set_pin_mode_pwm_output(pin)

board = pymata4.Pymata4()
setup_pins(board, PINS)

mapping = {}

for pin in PINS:
    system('clear')
    print(OPTIONS)
    board.pwm_write(pin, 200)
    mapping[pin] = input('Press number key to select which motor just fired...')

print(mapping)

with open('pin_mapping.json', 'w') as fp:
    json.dump(mapping, fp)

board.shutdown()
sys.exit(0)