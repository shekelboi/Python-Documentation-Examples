# A dictionary is a key-value pair map

# Empty curly braces initialize an empty dictionary
d = {}

print(d)

# Keys can be added using subscription
d["key"] = "value"

# The value can be recalled from the key once added to the dictionary
print(d["key"])

# Similarly, the value of associated with the key can also be modified
d["key"] = "something else"
print(d["key"])

# Attempting to access a key that does not exist in a dictionary leads to an exception
# print(d["not in the dict"])

# Keys (and their associated value) can be deleted using the del keyword
del d["key"]
print(d)

# Dictionaries can be initialized with key-value pairs
d = {
    "like": "this",
    "or": "this"
}
print(d)

# Dict comprehensions are also possible
# Here is an example where the capitalized version of the words are mapped onto the original
words = ["Guangdong", "Hubei", "Hainan", "Fujian", "Sichuan"]
d = {province: province.upper() for province in words}
print(d)
