# List comprehensions provide a simple way of creating lists while iterating through an iterable

# A list comprehension of the squared values of even numbers between 0 and 10
l = [i ** 2 for i in range(11) if i % 2 == 0]
print(l)
