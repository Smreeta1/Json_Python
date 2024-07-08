import json

#list of dictionaries definition
data = [
    {"name": "Ram", "age": 20, "city": "ktm"},
    {"name": "Sita", "age": 22, "city": "Ktm"},
    {"name": "Abc", "age": 32, "city": "Bkt"}
]
file_path = "./data.json"

with open(file_path, "w") as json_file:  #to serialize data and write to file
    json.dump(data, json_file)

print(f"Data has been written to {file_path}")
