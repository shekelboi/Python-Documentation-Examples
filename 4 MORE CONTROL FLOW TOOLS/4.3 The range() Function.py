# Iterating through a range
# The range takes the start, end (exclusive) and step as its parameters

# For example, a step of 2 can be used with a starting point of 50 and an ending point of 101 to
# print all the even numbers between 50 and 100
for i in range(50, 101, 2):
    print(i)

print("====")

# Negative step is also possible
# The inverse of the previous loop would be
for i in range(100, 49, -2):
    print(i)

print("====")

# It is possible to use range to iterate through a list of elements (by passing the length of the list to the range)
# This is particularly useful we need to reassign the values inside the list
# Suppose we want to set all even numbers to zero, it could be achieved using this
l = [10, 7382, 812, 8291, 132]
for i in range(len(l)):
    if l[i] % 2 == 0:
        l[i] = 0
print(l)

# The same thing can be achieved with enumerate too
l = [10, 7382, 812, 8291, 132]
for index, num in enumerate(l):
    if num % 2 == 0:
        l[i] = 0
print(l)
