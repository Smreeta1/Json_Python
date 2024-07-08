import unittest
import json

class Test_Json_Serialization(unittest.TestCase):

    def test_json(self):
      
        data = [
            {"name": "Ram", "age": 20, "city": "ktm"},
            {"name": "Sita", "age": 22, "city": "Ktm"},
            {"name": "Abc", "age": 32, "city": "Bkt"}
        ]
        json_string = json.dumps(data)

        self.assertTrue(json_string)  #assert
        
        deserialized_data = json.loads(json_string)
        
        self.assertEqual(deserialized_data, data)
        
        self.assertIsInstance(json_string, str)    # Asserting the types
        self.assertIsInstance(deserialized_data, list)

if __name__ == '__main__':
    unittest.main()
