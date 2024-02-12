# Default values can be defined for function parameters
def root(num, degree=2):
    return num ** (1 / degree)


print(root(16))
print(root(16, degree=4))
# In this case, since the arguments are in order, we do not need to specify the name of the parameter
print(root(16, 4))


# Default parameters are only evaluated once. Since lists are passed by reference, this means the
# reference to the default value will be the same in each function call
def f(l=[]):
    print(l)
    l.append(0)
    return l


# l will be appended with every function call
f()
f()
f()
