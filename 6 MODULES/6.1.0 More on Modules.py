# We can import entire modules using import and the name of the module
import math

# Alternatively we can import just a function/variable from a module using from
from math import pi, floor

print(floor(pi))

# Or we may import all the content of the module directly into the current namespace
# This is highly discouraged in most cases since it lacks clarity about what is introduced into the namespace
from math import *

# Here are all the methods and variables of the math module that were imported into the workspace
# (except for the private attributes starting with an underscore
# and the special attributes starting with double underscores)
print(dir(math))

# It is also possible to load a module with an alias
import math as mathematics

print(mathematics.ceil(mathematics.pi))

# From also supports aliases are also supported
from math import ceil as round_up

print(round_up(math.pi))
