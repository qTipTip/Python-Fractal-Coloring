"""
This file contains various color_functions for use in the fractal visualizer.
Each color function returns a real number, which is passed to a color_index function
that returns an index 0 <= i <= 1.
Currently the input_line is on the form:
    x_index, y_index, iterations, complex_number
this is subject to change.
"""
class ColorFunctions(object):
    """ A class containing various color functions, as well as a color index
    function and a function that composes these two """

    def __init__(self, max_iterations, fractal_power, bailout_value):
        self.max_iterations = max_iterations
        self.fractal_power = fractal_power
        self.bailout_value = bailout_value

    def iteration_count_coloring(self, input_line):
        return int(input_line[2]) / float(self.max_iterations)

    def continuous_iteration_count(self, input_line):
        p = self.fractal_power
        M = self.bailout_value
        N = int(input_line[2])
        mag = float(input_line[3])
        val =  N + (M**p - mag) / float(M**p - M)

    def color_index(self, u, k=2.5, u_0=0):
        """
        Returns a color-index between 0 and 1 based on some metric.
        """
        return u
    def get_color(self, index):
        """
        Given a color index returns an RGB color.  I might implement other
        color spaces as well.
        """
        return (255 - int(index*255), 255 - int(index*255), 255 - int(index*255))
