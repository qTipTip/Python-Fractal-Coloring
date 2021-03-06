"""
This script reads one of the .dat files generated by the fractal generator,
iterates over each point in the complex grid and assigns each complex point a
color based on a color_function and a color_palette.
"""

from PIL import Image
import sys
sys.path.append('../color_functions/')
from color_func import ColorFunctions
# We first start by reading in the .dat file
INPUT_FILE = '../fractal_generator/generated_fractal.dat'

with open(INPUT_FILE, 'r') as data_in:
    # We read the first four lines first, telling us what properties the fractals has
    RESOLUTION_X = int(next(data_in).split(' ')[-1])
    RESOLUTION_Y = int(next(data_in).split(' ')[-1])
    NUMBER_OF_ITERATIONS = int(next(data_in).split(' ')[-1])
    COMPLEX_SEED = complex((next(data_in).split(' ')[-1]))
    BAILOUT_VALUE = float((next(data_in).split(' ')[-1]))
    COLOR_FUNCTION = ColorFunctions(NUMBER_OF_ITERATIONS, 2, BAILOUT_VALUE)
    indx = COLOR_FUNCTION.color_index
    colr = COLOR_FUNCTION.get_color
    # We now initialize an empty bitmap
    IMAGE = Image.new('RGB', (RESOLUTION_X, RESOLUTION_Y), 'black')
    PIXELS = IMAGE.load()

    # Iterate over the complex numbers, given by their indices in the complex grid
    for line in list(data_in):
        INPUT_LINE = line.split(',')
        X = int(INPUT_LINE[0])
        Y = int(INPUT_LINE[1])
        ITERATIONS = int(INPUT_LINE[2])
        if ITERATIONS < NUMBER_OF_ITERATIONS:
            PIXELS[X, Y] = colr(indx(COLOR_FUNCTION.continuous_iteration_count(INPUT_LINE)))
    IMAGE.show()
