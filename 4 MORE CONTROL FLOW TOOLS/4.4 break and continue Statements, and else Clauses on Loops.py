# Loops can also have an else clause, which is only executed when the original condition evaluates to false or
# the final iteration is reached (in case of for loops)

# Compare the following loops

l = [43, 132, 421, 32, 76]

# Suppose we are looking for an element that does not exist in the list
for n in l:
    if n == 5:
        print("Found")
else:
    print("Not in the list")

# If we break out of the loop before it finishes all iterations, it will not enter the else clause
for n in l:
    print("Breaking out of the loop")
    break
else:
    print("Not in the list")

# We can use continue to skip to the next iteration
for n in l:
    # Continue if the number is odd
    if n % 2 == 1:
        continue
    print(n)
