from DIYables_Pico_Keypad import Keypad
import time

NUM_ROWS = 4
NUM_COLS = 3

# Constants for GPIO pins
ROW_PINS = [13, 12, 11, 10]  # GPIO numbers for row pins
COLUMN_PINS = [9, 8, 7]  # GPIO numbers for column pins

# Keymap corresponds to the layout of the keypad 3x4
KEYMAP = ['1', '2', '3',
          '4', '5', '6',
          '7', '8', '9',
          '*', '0', '#']

# Initialize the keypad
keypad = Keypad(KEYMAP, ROW_PINS, COLUMN_PINS, NUM_ROWS, NUM_COLS)
keypad.set_debounce_time(400) # 400ms, addjust it if it detects twice for single press

# Main loop to check for key presses
while True:
    key = keypad.get_key()
    if key:
        print("Key pressed:", key)
