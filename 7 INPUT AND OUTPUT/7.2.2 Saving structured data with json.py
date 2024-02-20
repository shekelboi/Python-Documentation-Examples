import json

file_path = 'files/speakers.json'

# Complex data types can be stored in a json
speakers = {'Indonesian': 199, 'Korean': 82, 'Hindi': 602}
print(json.dumps(speakers))
# Alternatively written to a file
# First we need to create a file stream then use the dump method of the json module
# This process is called serialization, where an object is turned into string representation
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(speakers, file)

# We can load the json file using the load method
# This process is called deserialization, where the JSON input is turned into an object
with open(file_path, encoding='utf-8') as file:
    data = json.load(file)
    print(data)
