# Python-Fractal-Coloring

I want to create a python library where the user easily can change and
experiment with different so called 'color-functions' when generating fractal
images.

I am hoping to be able to create a set of default color-functions that take
some parameters as input and returns a color-index between 0 and 1. It
essentially assigns each complex number in the grid being examined a
color-index.

This color-index is then passed to a color-pallette function which given a
color space (rgb, rgba, hsv, hls) assigns a color.

In order to avoid having to recompute a fractal every time I test the program,
I am going to generate one fractal and write all the data to a data file that I
can easily re-read.  This also makes it very easy to see the changes between
color functions and palletes.
