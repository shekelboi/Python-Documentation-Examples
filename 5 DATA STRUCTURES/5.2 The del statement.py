# Del can delete (unassign) variables or ranges/index within an array

a = 10
print(a)
del a
# Printing a would result in an exception, since it is not declared (it has been deleted)
# print(a)

l = [10, 20, 30, 40, 50]
print(l)
# Deleting the first element
del l[0]
print(l)

# Deleting the last two elements
del l[-2:]
print(l)

# Clearing the array
del l[:]
print(l)
