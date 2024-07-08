import json
 
         
def add_person(file_path, new_person):
    with open(file_path, 'r') as file:      #Read file
        data = json.load(file)

    data.append(new_person)                 #Append new person data

    with open(file_path, 'w') as file:     #Write to file
        json.dump(data, file,indent=2)

new_person = {"name": "new2", "age": 24, "city": "BRT"}  #new person record
file_path = "./data.json" 
