import json

def delete_person(file_path, person_name):
   
    with open(file_path, 'r') as file:
        data = json.load(file)

    data = [person for person in data if person["name"] != person_name]

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


