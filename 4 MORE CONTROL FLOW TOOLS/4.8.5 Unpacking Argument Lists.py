# To unpack argument lists you may use the * operator
# Typical arguments for a range (start, end, step)
args = [2, 30, 5]
# To pass it to the range function it must be unpacked first
print(list(range(*args)))

# The same thing can be done with dictionaries
args = {
    'sep': ', ',
    'end': '!!!'
}
print("just", "an", "example", **args)
