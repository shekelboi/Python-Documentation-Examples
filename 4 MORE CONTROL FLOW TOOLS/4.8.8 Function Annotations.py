def custom_uppercase(string: str) -> str:
    return "".join([s.upper() if i % 2 == 0 else s for i, s in enumerate(string)])


# Using the __annotations__ attribute of a function, we can find the parameter and return types of that function
print(custom_uppercase.__annotations__)
