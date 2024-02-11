# A simple example to a while loop could be to find the first n divisors of a given number
# Suppose we are looking for the first 6 divisors of the number 1024

# The number we are looking for
number = 1024
# The number of divisors we are looking for
number_of_divisors = 6

# Storing the divisors
divisors = []

# Initiating a counter from where we will look for divisors (this should be started from 1,
# since division by 0 would result in an exception).
counter = 1

# While we have less than 6 divisors, we will keep searching for them
while len(divisors) <= number_of_divisors:
    # If the selected number is divisible by the current number (the counter) we will add that to the divisors
    if number % counter == 0:
        divisors.append(counter)
        # Optionally print the found divisor
        # The divisors will only be separated by a space instead of a newline
        print(counter, end=" ")
    # Increment the counter
    counter += 1

# Add a newline using print, so when the list is printed, it is not printed on the same line as the divisors previously
print()

# Print the list of the first 6 divisors found
print(divisors)
