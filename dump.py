import json

# Define a list of dictionaries
data = [
    {"name": "Ram", "age": 20, "city": "ktm"},
    {"name": "Sita", "age": 22, "city": "Ktm"},
    {"name": "Abc", "age": 32, "city": "Bkt"}
]

# Specify the file path where you want to save the JSON data
file_path = "./data.json"

# Open the file in write mode and use json.dump() to serialize data and write to file
with open(file_path, "w") as json_file:
    json.dump(data, json_file)

print(f"Data has been written to {file_path}")
