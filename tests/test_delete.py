import os
import json
import pytest
from Operations.delete_record import delete_person

@pytest.fixture
def setup_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'Operations', 'data.json') #file path to json
    
    #Load initial data from data.json
    with open(file_path, 'r') as file:
        initial_data = json.load(file)
    
    yield file_path, initial_data  #sets up any necessary resources before yield and removes after yeild
    

    with open(file_path, 'w') as file:
        json.dump(initial_data, file, indent=2)

def test_delete_person(setup_data):
    file_path, initial_data = setup_data
    
    #Delete Sita from file
    delete_person(file_path, "Ram")
    
    #Read from file
    with open(file_path, 'r') as file:
        updated_data = json.load(file)
    
    # Asserting Sita is deleted from data.json
    assert len(updated_data) == len(initial_data) - 1
    assert not any(person["name"] == "Sita" for person in updated_data)
