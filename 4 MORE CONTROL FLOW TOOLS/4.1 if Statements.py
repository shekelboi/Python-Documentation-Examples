# Checking conditions using if, elif (else if) and else

x = int(input("Enter a number: "))

# Checking if it is an even or odd number
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Checking whether the number is less than 10, between 10 and 100 or greater than 100

if x < 10:
    print("Less than 10.")
elif 10 <= x <= 100:
    print("Between 10 and 100.")
else:
    print("Greater than 100.")
