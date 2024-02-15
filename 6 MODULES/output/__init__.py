"""
This is a package specializes in handling outputs (stdout or file output).
"""

# Relative import of the content of the modules in the current folder
from .display import *
from .file import *

# The path variable shows the directories used by the package.
# This list can be extended, thus also extending the modules in the package.
print("The path to the", __name__, "package is", __path__)
