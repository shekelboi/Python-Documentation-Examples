l = [25, 30, 30, 10]
print(l)

# Adding an item to a list
l.append(5)
print(l)
# Extending the list by another one
l.extend([18, 22])
print(l)
# Inserting an element at a certain index
l.insert(0, 999)
print(l)
# Remove an element
l.remove(999)
print(l)
# Remove and return the specified element by index (the last one by default)
print(l.pop())
print(l.pop(4))
# Get the index of the first occurrence of a value in the list
print(l)
print(l.index(25))
# Same but only within the specified slice
print(l.index(25, 0, 1))

# Count the number of occurrences of an element
print(l.count(30))

# Reverse the list
l.reverse()
print(l)

# Shallow copy of a list
l2 = l.copy()
l[1] = 1000
print(f"{l} != {l2}")

# Sort the list
l.sort()
print(l)

# Delete all the elements
l.clear()
print(l)
