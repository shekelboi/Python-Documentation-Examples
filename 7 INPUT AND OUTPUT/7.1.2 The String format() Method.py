# Similarly to f-strings, we can use the format function, in which the braces act as placeholders
who = 'you'
print('This {} how {} format {} string'.format('is', who, 'a'))

# The advantage of the format function is that we can number the arguments and easily change their order without
# having to change the order of the parameters within the function call.
animals = 'fox', 'bear'
print('The {0} chases the {1}'.format(animals[0], animals[1]))
print('The {1} chases the {0}'.format(animals[0], animals[1]))

# Alternatively we can associate keywords with the parameters and use those when we interpolate them
print('The {chaser} chases the {chased}'.format(chased=animals[0], chaser=animals[1]))

# Positional and keywords arguments can be combined
print('The {chaser} chases the {0}'.format(animals[0], chaser=animals[1]))

# Dictionaries can also be passed to the format function, in this case square brackets have to be used within the
# string interpolation to access the values in the dictionary using the keys.
# If we have more than one keys that we want to access from the same dictionary, we must write 0 in front of the key,
# since otherwise the automatic numbering, would add subsequent numbers within the parentheses (2, 3, 4...), however
# these arguments do not exist, so a runtime error occurs. In order to use the dictionary (which in this case is the
# first argument passed to the format function) we must add 0 in front of our key.
# The reason why not adding 0 works if there is only one key that we are trying to access from the dictionary, is
# because the numbering is added implicitly.
capitals = {'Abyssinia': 'Addis Ababa', 'Gold Coast': 'Accra', 'Zaire': 'Kinshasa'}
print('{0[Abyssinia]} and {0[Gold Coast]}'.format(capitals))
# Did we not specify 0, we would have to pass the dictionary the appropriate number of times to the format function
print('{[Abyssinia]} and {[Gold Coast]}'.format(capitals, capitals))

# Alternatively the key-value pairs of the dictionary can be passed
# as keyword arguments to the format function with the ** notation
print('{Abyssinia} and {Gold Coast}'.format(**capitals))
