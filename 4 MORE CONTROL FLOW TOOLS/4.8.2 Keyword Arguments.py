def echo(first, second="second"):
    print(first, second)


# Functions can be called using keyword arguments
echo("1st")
echo("1st", "2nd")
echo(second="2nd", first="1st")
echo(first="1st", second="2nd")


# Additional arguments can be added using * in the function declaration
# The additional arguments will be stored in a tuple
def additional(required, *others):
    print(required, others)


additional("required")
additional("required", "and", "some", "others")


# Additional keyword arguments can be stored using a dictionary
# This can be achieved by using double asterisk (**) before the last parameter
def additional_keywords(required, **others):
    print(required, others)


additional_keywords("required", test="some test", example="some example")
