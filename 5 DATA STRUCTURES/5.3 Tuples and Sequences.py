# The tuple is an immutable sequence data type

# A practical example of tuples would be x, y coordinates
coordinates = (43, 21)
print(coordinates)
# They can also be declared without parentheses
coordinates = 10, 3
print(coordinates)

# Tuples can be unpacked to variables
x, y = coordinates
print(x, y)

# Tuples can be nested
# For example, a line could be represented by two points
p1 = 10, 10
p2 = 20, 20
line = p1, p2
print(line)

# Tuples may contain lists however that would make them unhashable
tuple_with_list = 10, [10]
# This would lead to an error since the list inside the tuple is not hashable
# (same if it was used in a dictionary or set)
# hash(tuple_with_list)
# d = {tuple_with_list: "test"}
# set(tuple_with_list)

# Tuples can also be empty
empty = ()
print(empty)

# Or contain only one element
singleton = 1,
print(singleton)
