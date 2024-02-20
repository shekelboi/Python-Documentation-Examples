# Importing datetime for later usage
import string
from datetime import datetime

# F-strings (formatted string literals) are prefixed by an 'f', this gives us the ability to
# reference variables or evaluate expressions in curly braces.
# Formatting options can also be specified,
# e.g. :.2f displays the result as a floating point value with 2 decimal places.
x = 20
divisor = 7
print(f'x = {x}, {x} / {divisor} = {x / divisor:.2f}')

# The same thing can be achieved with the format function.
# In this case the curly braces acts as placeholders where formatting options can be specified
# and the expressions/variables are passed to the format function.
print('x = {}, {} / {} = {:.10f}'.format(x, x, divisor, x / divisor))

# Padding can be specified after a colon which helps with the arrangement of the values in the output
# Here is an example of the first 10 powers of 10 (starting from the 0th power) without padding
for i in range(10):
    print(10 ** i)

# And with a padding of 10
# The end of the number will always be at the 10th column (unless it overflows it, e.g. has more digits than 10)
for i in range(10):
    print(f'{10 ** i:10}')

# Repr and str are both ways we can convert objects to a printable form
# The difference lies between their usability, str is meant to return a human-readable representation of the object
# whereas repr is meant to be used for debugging/logging, often giving providing more details about the objects.
# Here is an example of the difference between the two using datetime objects
now = datetime.now()
print(str(now))
print(repr(now))

# Another example would be the difference between printing strings
string = "Example\nstring"
print(string)
# Note that repr surrounds the output string by quotes to emphasize its string nature.
# It also shows the
print(repr(string))
