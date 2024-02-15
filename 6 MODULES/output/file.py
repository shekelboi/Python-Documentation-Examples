def write(file_name: str, content: str):
    with open(file_name) as file:
        file.write(content)
