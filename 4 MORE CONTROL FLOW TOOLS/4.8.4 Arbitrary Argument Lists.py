# Arbitrary argument lists can be declared using *, which takes an arbitrary number of arguments in a tuple
def arbitrary(positional, *args):
    print("Positional:", positional)
    print("Optional", args)


arbitrary("Just the required one")
arbitrary("required", "many", "optional", "args")
