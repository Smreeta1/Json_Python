import json
data = [                                       #dict_data
    {"name": "Ram", "age": 20, "city": "ktm"},
    {"name": "Sita", "age": 22, "city": "Ktm"},
    {"name": "Abc", "age": 32, "city": "Bkt"}
]

json_string = json.dumps(data)         #dict_data is converted to a Json formatted string using json.dumps() 

print(f'JSON string:{json_string}')
print("Type of Json string:", type(json_string))
#OUtput:---Type of Json string: <class 'str'>

file_path = "./data.json"               #file path

json_file = open(file_path, "w")        #writting the Json string to file data.json
json_file.write(json_string)
json_file.close()


json_file = open(file_path, "r")        #reading the Json string back from the file
loaded_json_str = json_file.read()
json_file.close()

#deserialization
deserialized_data = json.loads(loaded_json_str)            # here,.loads() convert data from Json string to Python obj
print(f'Deserialized data:{deserialized_data}')
print("Type of deserialized data:", type(deserialized_data))
#output:--Type of deserialized data: <class 'list'>