input_path = 'files/input.txt'
enc = 'utf-8'

# The read method has an optional size argument, in which
# the number of characters/bytes (in binary mode) to read can be specified
with open(input_path, encoding=enc) as file:
    print(file.read())
    # Once the end of the file has been reached, the read method return an empty string
    print(repr(file.read()))

# The readline methods only reads one line at a time and also keeps the \n at the end of the lines
with open(input_path, encoding=enc) as file:
    # Assigning the returned value of the readline method to line
    # and checking if it has some value (not an empty string)
    while line := file.readline():
        print(line, end='')
    print()

# A more convenient way of iterating through a file line by line is using a for loop
with open(input_path, encoding=enc) as file:
    # Iterating through the file line by line and also outputting the number of the current line
    for i, line in enumerate(file, start=1):
        print(f'{i}. {line}', end='')
    print()

# All the lines of a file can be stored in a list using either the readlines method
# or by converting the file object to a list
with open(input_path, encoding=enc) as file:
    # Alternatively list(file)
    lines = file.readlines()
    print(lines)

# With the write method, it is possible to write text into a file, given that the file is opened in writable mode.
# The method return the number of characters written.
with open('files/output.txt', mode='w', encoding=enc) as file:
    written = file.write('Just an example')
    print(written, 'characters written')
    # The tell method returns the current position in the file (characters in text mode, bytes in binary mode)
    position = file.tell()
    print('Currently at character', position)

with open(input_path, encoding=enc) as file:
    print(file.readline(), end='')
    # Using the seek method, we can return to the beginning of the file
    file.seek(0)
    print(file.readline(), end='')
    # The position can be set relatively too, using the second (whence) argument of the method
    # 0 = beginning of the file, 1 = current position, 2 = end of the file

    # Unfortunately the position cannot be changed relative to the current one (and relative to the end) in text mode
    # This however can be achieved with the help of the tell method
    # It is important to note that even though this does work, the Python documentation warns against using an offset
    # value other than the current position or 0, stating that any other value may result in undefined behavior.

    # 30 chars back from the current position
    file.seek(file.tell() - 30)
    print(file.readline(), end='')
    # Consequently setting the position back by 30 chars again would result in printing the exact same line
    file.seek(file.tell() - 30)
    print(file.readline(), end='')

    # The same functionality can be extended to the end too, albeit in a bit more cumbersome way
    # Seeking the end of the file
    file.seek(0, 2)
    # Seeking to 30 chars before the end of the file
    file.seek(file.tell() - 30)
    print(file.readline())
