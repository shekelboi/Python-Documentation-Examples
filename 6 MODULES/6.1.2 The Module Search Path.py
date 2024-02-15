import sys

# The list of the built-in modules. These modules are prioritized over local modules
print(sys.builtin_module_names)

# These are the directories in which Python will for the module if it did not find it among the built-in modules
print(sys.path)
