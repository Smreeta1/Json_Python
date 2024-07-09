import json


def add_person(file_path, new_person):
    with open(file_path, 'r') as file:  # Read file
        data = json.load(file)

    print(f"Current data: {data}")
    print(f"New person to add: {new_person}")

    # Check for duplicates
    for person in data:
        if person == new_person:
            print("Duplicate entry found.")
            return "Duplicate"

    data.append(new_person)  # Append new person data

    with open(file_path, 'w') as file:  # Write to file
        json.dump(data, file, indent=2)
        
    return "Added"
