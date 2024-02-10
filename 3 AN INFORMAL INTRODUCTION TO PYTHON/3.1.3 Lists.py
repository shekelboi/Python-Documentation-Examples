# Lists can contain multiple data types
l = ["example", 2, 2.4, True]
print(l)

# Lists can be sliced
l = [20, 3, 4, 1, 5]
print(l[-1])  # Last index
print(l[2:5])  # From 2 to 4 (5 but excluding 5)
print(l[::2])  # Only every second element
print(l[::-1])  # Reversing the list

# List can be concatenated
l = [2, 4] + [6, 8]
print(l)

# Lists are subscriptable and mutable (their content can be changed)
l[0] = -9999
print(l)

# New elements can be added to the list using append
l.append(444)
print(l)

# Slices can be replaced
l[2:4] = [0, 0]
print(l)

# Slices can also be removed using del
del l[2:4]
print(l)

# Or by assigning an empty string to the slice
l[0:2] = []
print(l)

# We can use the len function to get the length of the list, just like with a string
print(len(l))
