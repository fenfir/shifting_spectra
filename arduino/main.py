import collections
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from random import randrange
from typing import Optional
from fastapi import FastAPI
import asyncio

colorama_init()

## For testing
loop_count = 0
MAX_ITER = 10
## End for testing

NUM_LEDS = 10
running = False

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

def update_light(value: int):
    output[0] = value

def check_input():
    i = randrange(10)
    return normalize_input(i)

# TODO
def normalize_input(input):
    return input


async def update_lights():
    while running:
        display_output(output)

        output.rotate(1)
        await asyncio.sleep(1)

app = FastAPI()

@app.get("/api/display_value/")
def get_value(value: int):
    # function to handle the GET request and call display_output function
    if 0 <= value <= 256:
        result = update_light(value)
        return {"result": result}
    else:
        return {"error": "The value entered must be between 0 and 256."}

@app.on_event("startup")
async def startup_event():
    print("Starting display loop...")
    global running
    running = True
    asyncio.create_task(update_lights())

@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down...")
    global running
    running = False