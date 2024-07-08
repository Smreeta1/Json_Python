import json

#Steps:Reading, Appending, and Writing
 #Direct dump() will overwrite existing dtaa
        #new_person = {"name": "Hari", "age": 24, "city": "BRT"}
        #with open(file_path, 'w') as file:
        #json.dump([new_person], file, indent=2)  
         
def add_person(file_path, new_person):
    with open(file_path, 'r') as file:      #Read file
        data = json.load(file)

    data.append(new_person)                 #Append new person data

    with open(file_path, 'w') as file:     #Write to file
        json.dump(data, file,indent=2)

new_person = {"name": "Hari", "age": 24, "city": "BRT"}  #new person record

file_path = "./data.json" 

add_person(file_path, new_person) # Adding the new person record
