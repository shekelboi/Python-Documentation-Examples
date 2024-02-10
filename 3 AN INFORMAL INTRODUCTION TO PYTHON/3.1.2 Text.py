# Single and double quotes are both valid
print("Hi")
print('Hi')

# We can escape the quote using the backslash
print("\"like this\"")
print('\'like this\'')

# New lines can be added using \n
print("Ex\nample")

# This behavior can be disabled using a raw string
print(r"Ex\nample")
print(r"\"")

# Multiline strings can be enclosed within triple quotes
print("""
Here
is
an
example
""")

print("====")
# The extra newlines can be suppressed using \
print("""\
Here
is
an
example\
""")
print("====")

# Strings can be concatenated using +
print("Like " + "this")

# They may also be automatically concatenated when they are next to each other (only for string literals)
print("Like " "this")
print("Or "
      "like "
      "this")

# Strings can be repeated using *
print("Example" * 15)

# Strings can be indexed by subscripting them. A single character is still a string.
print("Example"[0])
print(type("Example"[0]))

# Negative indices can be used to index the string from the right
print("Nice"[-1])  # To get the last character

# A technique called slicing can be used to obtain a substring from the original string, with the syntax:
# [start, end, step]
# Note that the end is exclusive.
# The step defaults to 1.

# To get the characters between 2 and 4, you can slice it using [2:5].
print("Amazing"[2:5])

# Omitting the first index defaults to 0, omitting the second index defaults to the size of the string
print("Amazing"[:5])
print("Amazing"[5:])

# Out ot of range indices normally result in an error, however this is not the case for slicing.
print("Short"[1000:])
print("Short"[:1000])

# Python strings are immutable, reassigning parts of them (even a character) will result in an error.

# len() can be used to get the length of the string
print(len("apple"))
