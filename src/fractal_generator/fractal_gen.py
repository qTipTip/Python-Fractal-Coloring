""" This script computes a fractal and writes
    all interesting data to a raw file."""

import numpy as np

OUT_FILE = 'generated_fractal.dat'

RESOLUTION_X = 512
RESOLUTION_Y = 512
WINDOW_OF_REFERENCE_X = (-2, 1)
WINDOW_OF_REFERENCE_Y = (-1, 1)

NUMBER_OF_ITERATIONS = 30
COMPLEX_SEED = complex(-0.4, 0.6)
COMPLEX_FUNCTION = lambda z, c: z*z + c
BAILOUT_VALUE = 4

# pylint: disable=E1103
COMPLEX_GRID_X = np.linspace(WINDOW_OF_REFERENCE_X[0], WINDOW_OF_REFERENCE_X[1], RESOLUTION_X)
COMPLEX_GRID_Y = np.linspace(WINDOW_OF_REFERENCE_Y[0], WINDOW_OF_REFERENCE_Y[1], RESOLUTION_Y)
# pylint: enable=E1103

with open(OUT_FILE, 'w') as output:
    output.write('#resolution_x = %d\n' % RESOLUTION_X)
    output.write('#resolution_y = %d\n' % RESOLUTION_Y)
    output.write('#number_of_iterations = %d\n' % NUMBER_OF_ITERATIONS)
    output.write('#complex_seed = %s\n' % str(COMPLEX_SEED))

    for i, a in enumerate(COMPLEX_GRID_X):
        for j, b in enumerate(COMPLEX_GRID_Y):
            z = complex(a, b)
            z_new = z
            for n in range(NUMBER_OF_ITERATIONS):
                if abs(z_new) >= BAILOUT_VALUE:
                    output.write('%d, %d, %d, %s\n' % (i, j, n, str(z_new)))
                    break
                else:
                    z_new = COMPLEX_FUNCTION(z_new, COMPLEX_SEED)
            else:
                output.write('%d, %d, %d, %s\n' % (i, j, NUMBER_OF_ITERATIONS, str(z_new)))

