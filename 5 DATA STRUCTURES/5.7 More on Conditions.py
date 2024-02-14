# This chapter focuses on operator precedence
# More info on operator precedence: https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/

# The expression is evaluated as follows:
# 2 ** 2 -> 4
# 4 == 4 -> True
# True and 3 < 2 -> True and False -> False
# False or True -> True
print(2 ** 2 == 4 and 3 < 2 or True)

# Using the walrus operator (:=), it is possible to assign values to variables inside expressions
if (n := 1) and n == 1:
    print("N is in fact equal to one since we assigned the value one to it in the if statement.")
print(n)
if (n := 0) and n == 1:
    print("N is not equal to one, so this block won't be reached, since we reassigned its value to 0.")
print(n)
