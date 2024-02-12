# Lambda is an anonymous function
to_int = lambda s: int(s)
print(to_int("10") + 5)

# It is especially useful in function calls
l = [10, 5, 2, 3]
# Mapping the elements to themselves + 100 using lambda
print(list(map(lambda x: x + 100, l)))
