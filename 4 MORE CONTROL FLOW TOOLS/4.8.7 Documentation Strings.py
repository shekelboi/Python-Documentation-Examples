# Docstrings can be used to document what functions do, what parameters they have, etc.
def custom_uppercase(string: str) -> str:
    """
    Transforms every second character of a string to uppercase.

    It is worth noting that the function does not convert to the input string to lowercase first,
    meaning that it would have no effect on already uppercase string input.
    :param string: Text to transform.
    :return: Transformed text.
    """
    return "".join([s.upper() if i % 2 == 0 else s for i, s in enumerate(string)])


print(custom_uppercase("racecar"))
