# This script computes a fractal and writes
# all interesting data to a raw file.

from numpy import linspace

out_file = 'generated_fractal.dat'

resolution_x = 1028
resolution_y = 1028
window_of_reference_x = (-2, 1)
window_of_reference_y = (-1, 1)

number_of_iterations = 30
complex_seed = complex(-0.4, 0.6)
complex_function = lambda z, c : z*z + c
bailout_value = 4

complex_grid_x = linspace(window_of_reference_x[0], window_of_reference_x[1], resolution_x)
complex_grid_y = linspace(window_of_reference_y[0], window_of_reference_y[1], resolution_y)

with open(out_file, 'w') as output:
    output.write('#resolution_x = %d\n' % resolution_x) 
    output.write('#resolution_y = %d\n' % resolution_y)
    output.write('#number_of_iterations = %d\n' % number_of_iterations)
    output.write('#complex_seed = %s\n' % str(complex_seed))

    for i, a in enumerate(complex_grid_x):
        for j, b in enumerate(complex_grid_y):
            z = complex(a, b)
            z_new = z
            for n in range(number_of_iterations):
                if abs(z_new) >= bailout_value:
                    output.write('%d, %d, %d, %s\n' % (i, j, n, str(z_new)))
                    break
                else:
                    z_new = complex_function(z_new, complex_seed)
            output.write('%d, %d, %d, %s\n' % (i, j, number_of_iterations, str(z_new)))

