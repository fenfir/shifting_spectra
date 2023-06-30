from nest2D import Point, Box, Item, nest, SVGWriter

def add_item_from_file(file, n, items):
    with open(file) as f:
        read_data = f.readline()

        item = Item([])

        items.append(item) 

    f.closed

def main():
    box = Box(150000000, 150000000)
    input = []
    add_item_from_file("test.asc", 6, input)

    pgrp = nest(input, box)

    sw = SVGWriter()
    sw.write_packgroup(pgrp)
    sw.save()