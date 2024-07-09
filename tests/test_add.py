import pytest
import json
import os
from Operations.add_record import add_person

@pytest.fixture
def setup_file_path():
    return os.path.join(os.path.dirname(__file__), '../Operations/data.json')

def test_add_person(setup_file_path):
    file_path = setup_file_path
    new_person = {"name": "final", "age": 20, "city": "Pkr"}  # test case: Adding a new person

    result = add_person(file_path, new_person)  # Calling add_person function to add new person
    print(result)  # print either "Added" or "Duplicate"

    with open(file_path, 'r') as file:  # Verifying result
        data = json.load(file)

    # Check if the new person is already in the data
    assert new_person in data, f"{new_person} was not found in the data after adding."
    assert result == "Added", "The new person was not added correctly."

    # Try adding the same person again
    result_duplicate = add_person(file_path, new_person)

    # Verify that the duplicate was not added
    with open(file_path, 'r') as file:
        data_after_duplicate = json.load(file)

    assert result_duplicate == "Duplicate", "Duplicate entry was not detected."

