import locale

# The open function returns a file object
# The first argument is the file name, the second is the mode
# ('w' for writing, 'a' for appending, 'r' for reading, r+ for reading and writing, etc.)
# The encoding of the file can be specified using the encoding keyword argument

# This is the default encoding that is used if encoding is left unspecified
print(locale.getencoding())

# Opening the input.txt file in the files folder with utf-8 encoding
# The default mode is reading ('r')
# Platform specific line endings, such as \r\n on Windows, are converted to \n automatically while reading text.
# The opposite applies to writing to text files, the platform specific line endings are restored by default.
file = open('files/input.txt', encoding='utf-8')
# We can read the entire file using the read method.
print(file.read())
file.close()
# In some situations changes written into the file will be lost when the filestream is closed manually.
# Further info: https://github.com/python/cpython/issues/62052

# The close method must be called on the file if we want to close the filestream.
# Using the with keyword the file can be closed automatically once we leave the block

with open('files/input.txt', encoding='utf-8') as file:
    print(file.read())
