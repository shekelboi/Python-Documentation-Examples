import news
import builtins

# Dir lists all the defined names (variables, modules, functions, etc.) except for built-in functions and variables
print(dir())

# We can use dir on modules too
print(dir(news))

# To list the built-in functions and variables, we can use the builtins module
print(dir(builtins))
