import numpy as np

# Limits for gray scale

limit_down = 0
limit_up = 255

# Dictionaries for white and black level per channel

white_level_per_channel = ({'R': 2000, 'G': 4000, 'B': 2000})

black_level_per_channel = ({'R': 255, 'G': 255, 'B': 255})

# Values for gamma correction

A = 255

gamma = 1./2.2