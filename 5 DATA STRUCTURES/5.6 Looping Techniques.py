# It is possible to loop through a dictionary using the items method and unpacking the returned key value pairs
d = {
    "Barack Obama": 2008,
    "Donald Trump": 2016,
    "Joe Biden": 2020
}

for key, value in d.items():
    print(key, value)

# Using enumerate we can retrieve the corresponding index alongside the elements
l = [3, 19, 32, 48, 10]
for i, n in enumerate(l):
    print(i, n)

# The zip function creates a sequence of tuples from the input lists
l2 = [328, 3829, 483, 21, 93]
# Note that after zipping the lists, the zipped sequence will take the length of the shortest list,
# thus the values of a l3 will not be included after 321
l3 = [20, 80, 21, 890, 321, 3289, 13, 0]
print(list(zip(l, l2, l3)))

# Looping over a sequence in reverse is possible multiple ways
# The most common way to achieve that is using the reversed function
for n in reversed(range(10)):
    print(n)

print("====")
# We can use the sorted function to loop over a sorted list
l = [10, 10, 3, 2, 3, -4, -9, 21]
for n in sorted(l):
    print(n)

print("====")
# To eliminate duplicates we can initialize a set with the value of hte list
for n in set(l):
    print(n)

print("====")
# We can combine set an sorted to loop through the sorted unique elements
for n in sorted(set(l)):
    print(n)
