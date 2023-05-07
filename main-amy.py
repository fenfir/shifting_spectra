n_leds = 100 # number of LEDs
n_clr_levels = 6 # size of palette

leds_clr_mat = []/
leds_clr_mat = [0 for i in range(n_leds)] 

color_map = []
color_map = [0 for i in range(n_clr_levels)] 


def display_clr():
    pass

def get_input():
    pass

def normalize_input():
    pass

running = True
while running:
    input = get_input()
    norm_input = normalize_input(input)

    leds_clr_mat = color_map[norm_input]

    display_


