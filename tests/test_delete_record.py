# import os
# import json
# import unittest

# from Operations.delete_record import delete_person


# # Function to set up test data
# def setup_data(file_path):
#     # Sample data
#     data = [
#         {"name": "Ram", "age": 20, "city": "ktm"},
#         {"name": "Sita", "age": 22, "city": "Ktm"},
#         {"name": "Abc", "age": 32, "city": "Bkt"}
#     ]
    
#     # Write data to data.json
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=2)

# # Test case for delete_person function

    
#     # Delete "Sita" from data.json
#     delete_person(file_path, "Sita")
    
#     # Read updated data from data.json
#     with open(file_path, 'r') as file:
#         updated_data = json.load(file)
    
#     # Assert that "Sita" is deleted from data.json
#     assert len(updated_data) == 2
#     assert all(person["name"] != "Sita" for person in updated_data)

# if __name__ == '__main__':
#     unittest.main()

import os
import json
import unittest
from Operations.delete_record import delete_person

class TestDeletePerson(unittest.TestCase):
    
    def test_delete_person(self):
        #Define file path to data.json
        file_path = os.path.join(os.path.dirname(__file__), '..', 'Operations', 'data.json')
        
        #Load initial data from data.json
        with open(file_path, 'r') as file:
            initial_data = json.load(file)
        
        #Delete Sita from data.json
        delete_person(file_path, "Sita")
        
        #Read updated data from data.json
        with open(file_path, 'r') as file:
            updated_data = json.load(file)
        
        #Asserting Sita is deleted from data.json
        self.assertEqual(len(updated_data), len(initial_data) - 1)
        self.assertFalse(any(person["name"] == "Sita" for person in updated_data))

if __name__ == '__main__':
    unittest.main()
