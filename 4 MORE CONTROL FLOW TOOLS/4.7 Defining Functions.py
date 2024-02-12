# Using global we can load and modify global variables
def modify_global():
    global x
    x = 5


# Nonlocal will load the variable from the nearest enclosing scope
def nonlocal_test():
    # Note that y here is a local variable, thus it will not affect the value of y within nonlocal_test
    def modify_nonlocal():
        nonlocal x
        x = 10
        y = 10

    x, y = 0, 0

    modify_nonlocal()
    print(x, y)


x = 100
print(x)
modify_global()
print(x)

nonlocal_test()
# All functions without a return statement implicitly return None
print(modify_global())
