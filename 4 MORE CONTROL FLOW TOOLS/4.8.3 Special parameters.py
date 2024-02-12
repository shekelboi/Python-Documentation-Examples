# Positional only, positonal/keyword and keyword only arguments can be separated using the following signature:
# Positional only, /, positional/keyword, *, keyword only

def echo(first, /, second="second"):
    print(first, second)


echo("1st")
echo("1st", "2nd")
echo("1st", second="2nd")


# Note that these do not work anymore:
# echo(second="2nd", first="1st")
# echo(first="1st", second="2nd")


def echo(first, /, *, second="2nd"):
    print(first, second)


echo("1st")
echo("1st", second="2nd")
# After re-declaring the echo function, the second argument is only accepted as a keyword argument, thus
# this will not work:
# echo("1st", "2nd")
# Similarly we cannot pass the first argument as a keyword argument
# echo(first="1st", second="2nd")
