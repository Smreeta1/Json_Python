import pytest
import json
import os
from Operations.add_record import add_person


def test_add_person():
    previous_data = [
        {"name": "Ram", "age": 20, "city": "ktm"},
        {"name": "Sita", "age": 22, "city": "Ktm"},
        {"name": "Abc", "age": 32, "city": "Bkt"}
    ]

    new_person = {"name": "Hari", "age": 24, "city": "BRT"}


    file_path = "temp_data.json"
    with open(file_path, 'w') as json_file:
        json.dump(previous_data, json_file, indent=2)

    add_person(file_path, new_person)       # Add the new person
    
    with open(file_path, 'r') as file:     #load file and read
        data = json.load(file)

    assert data == previous_data + [new_person], "The new person was not added correctly."
    os.remove(file_path)  #Removing the temp Json file after test compl
    
if __name__ == "__main__":
    pytest.main()
