import collections
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from random import randrange
from typing import Optional
from fastapi import FastAPI
import time

colorama_init()

## For testing
loop_count = 0
MAX_ITER = 10
## End for testing

NUM_LEDS = 10

output = collections.deque([0 for i in range(NUM_LEDS)])

output_colors = [
    Fore.RED,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.MAGENTA,
    Fore.RESET,  # Regular text color, to allow "dark mode"
    Fore.YELLOW,
]


   
def display_output(value: int):
     # function to display the output based on the input value
    output_string = ""
    for l in output:
        c = l % len(output_colors)
        output_string += output_colors[c]
        output_string += "%d, " % l
        output_string += Style.RESET_ALL

    print(output_string)


def check_input():
    i = randrange(10)
    return normalize_input(i)

# to-do
def normalize_input(input):
    return input


running = True
while running:
    i = check_input()
    output[0] = i

    display_output(output)

    output.rotate(1)
    time.sleep(1)
    # loop_count += 1
    # if loop_count > MAX_ITER:
    #     running = False


app = FastAPI()

@app.get("/api/display_value/")
def get_value(value: int):
    # function to handle the GET request and call display_output function
    if 0 <= value <= 256:
        result = display_output(value)
        return {"result": result}
    else:
        return {"error": "The value entered must be between 0 and 256."}
