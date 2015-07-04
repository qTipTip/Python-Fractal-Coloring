"""
This file contains various color_functions for use in the fractal visualizer.
Each color function returns a real number, which is passed to a color_index function
that returns an index 0 <= i <= 1.
Currently the input_line is on the form:
    x_index, y_index, iterations, complex_number
this is subject to change.
"""
from numpy import clip

class ColorFunctions:
    """ A class containing various color functions, as well as a color index
    function and a function that composes these two """

    def __init__(self, max_iterations):
        self.max_iterations = max_iterations
        
    def iteration_count_coloring(self, input_line):
        return int(input_line[2]) / float(self.max_iterations)

    def color_index(self, u, k=2.5, u_0 = 0):
        return u
    
    def get_color(self, index):
        return (int(index*255), int(index*255) ,int(index*255))