import json

# py dictionaries definition
data = [
    {"name": "Ram", "age": 20, "city": "ktm"},
    {"name": "Sita", "age": 22, "city": "Ktm"},
    {"name": "Abc", "age": 32, "city": "Bkt"}
]


json_string = json.dumps(data) # Serializes the list to a JSON formatted string

# Print the JSON string
print(json_string)
