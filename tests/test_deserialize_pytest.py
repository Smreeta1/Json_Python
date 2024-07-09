import json
import pytest

def test_json():
    test_cases = [
        ([
            {"name": "Ram", "age": 20, "city": "ktm"},
            {"name": "Sita", "age": 22, "city": "Ktm"},
            {"name": "Abc", "age": 32, "city": "Bkt"}
        ]),
        
    ]
    for data in test_cases:
        json_serialization(data)

def json_serialization(data):
    json_string = json.dumps(data)

    assert json_string  # assert truthiness of json_string

    deserialized_data = json.loads(json_string)
    
    assert deserialized_data == data  # assert equality

    assert isinstance(json_string, str)  # asserting types
    assert isinstance(deserialized_data, list)

if __name__ == '__main__':
    pytest.main()
