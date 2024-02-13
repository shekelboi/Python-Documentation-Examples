# List comprehensions can be nested inside each other

# Generate a matrix with ranges with the following start and end values
ranges = [(0, 10), (5, 20), (110, 115)]
nested = [[i for i in range(start, end)] for start, end in ranges]
print(nested)
