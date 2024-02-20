from datetime import datetime

# Padding helps with the alignment of multiple columns
# E.g. the first 11 powers of 2 (including the 0th)
for i in range(11):
    print(2 ** i, 2 ** i)
# Since the last power (2 ** 10) is 4 digits long, we can make the field at least 4 characters wild.
# This way the columns will line up.
for i in range(11):
    print(f'{2 ** i:4} {2 ** i:4}')

# We could make the columns even wilder, however this would leave a lot of empty space
for i in range(11):
    print(f'{2 ** i:10} {2 ** i:10}')

# A really useful tool in debugging is using the equal sign to display both the name of the variable and its value
now = datetime.now()
# Prints the name of the variable and its value using repr
print(f'{now=}')
