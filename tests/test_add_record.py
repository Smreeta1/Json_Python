import unittest
import json
import os
from Operations.add_record import add_person


class TestAddPerson(unittest.TestCase):

    def setUp(self):
        self.file_path = os.path.join(os.path.dirname(__file__), '../Operations/data.json')  # file path setup

    def test_add_person(self):
        new_person = {"name": "final", "age": 20, "city": "Pkr"}  # test case: Adding a new person

        result = add_person(self.file_path, new_person)  # Calling add_person function to add new person
        print(result)  # print either "Added" or "Duplicate"

        with open(self.file_path, 'r') as file:  # Verifying result
            data = json.load(file)

        # Check if the new person is already in the data
        self.assertIn(new_person, data, f"{new_person} was not found in the data after adding.")
        self.assertEqual(result, "Added", "The new person was not added correctly.")

        # Try adding the same person again
        result_duplicate = add_person(self.file_path, new_person)

        # Verify that the duplicate was not added
        with open(self.file_path, 'r') as file:
            data_after_duplicate = json.load(file)

        self.assertEqual(result_duplicate, "Duplicate", "Duplicate entry was not detected.")


if __name__ == "__main__":
    unittest.main()
