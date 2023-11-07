import os
import json

current_os = os.name

DATA_PATH = "Apple Music Activity/"
files = os.listdir(DATA_PATH)

json_files = []
csv_files = []

for file in files:
    if file.endswith(".json"):
        json_files.append(file)
    elif file.endswith(".csv"):
        csv_files.append(file)

json_data = []

for json_file in json_files:
    with open(os.path.join(DATA_PATH, json_file), "r") as f:
        data = json.load(f)
        json_data.append(data)

def print_json_structure(d, indent=0):
    for key, value in d.items():
        print(' ' * indent + str(key), end=' ')
        if isinstance(value, dict):
            print("(dict)")
            print_json_structure(value, indent+4)
        elif isinstance(value, list):
            print("(list)")
            print_list_structure(value, indent+4)
        else:
            print("(" + type(value).__name__ + ")")

def print_list_structure(l, indent=0):
    print(' ' * indent + "List contains:")
    # We assume that a list contains homogenous elements, as per JSON standard practice
    if l:  # Check if the list is not empty
        if isinstance(l[0], dict):
            print_json_structure(l[0], indent+4)
        elif isinstance(l[0], list):
            print_list_structure(l[0], indent+4)
        else:
            print(' ' * (indent+4) + "(" + type(l[0]).__name__ + ")")
    else:
        print(' ' * (indent+4) + "(Empty List)")

# Assuming `data` is your top-level list
def analyze_list(data):
    if data:  # Ensure the list is not empty
        if isinstance(data[0], dict):
            # It's a list of dictionaries
            print_list_structure(data)
        elif isinstance(data[0], list):
            # It's a list of lists
            for sub_list in data:
                print_list_structure(sub_list, indent=4)
        else:
            # It's a list of some other data type
            print("List of " + str(type(data[0]).__name__))
    else:
        print("Empty list")

analyze_list(json_files[0])
