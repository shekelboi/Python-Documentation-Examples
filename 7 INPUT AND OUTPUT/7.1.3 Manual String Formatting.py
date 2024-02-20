# With the rjust function we can add padding to the value just like in case
# E.g. the powers of 10 with rjust
for i in range(10):
    print(str(10 ** i).rjust(10))

# The same thing with an f-string
# From the two code snippets, it is clear that achieving the same results using an f-string is more convenient
for i in range(10):
    print(f'{10 ** i:10}')

# Zfill can be used to pad typically numeric values with zeros, it understands the minus sign too
num = '-1.95'
print(num.zfill(2))
print(num.zfill(6))
