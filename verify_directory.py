import os
import pickle
from functools import reduce

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir_structure = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir_structure)
        parent[folders[-1]] = subdir
    return dir_structure

if __name__ == "__main__":

    # Load directory_structure from a file named directory_structure.pkl
    with open('directory_structure.pkl', 'rb') as f:
        directory_structure = pickle.load(f)

    curr_directory_structure = get_directory_structure("Apple Music Activity/")

    # Find the difference between the two directory structures
    diff = {}
    for key in directory_structure:
        if key not in curr_directory_structure:
            diff[key] = ('directory_structure', None)
        else:
            for subkey in directory_structure[key]:
                if subkey not in curr_directory_structure[key]:
                    diff[subkey] = ('directory_structure', key)

    for key in curr_directory_structure:
        if key not in directory_structure:
            diff[key] = (None, 'curr_directory_structure')
        else:
            for subkey in curr_directory_structure[key]:
                if subkey not in directory_structure[key]:
                    diff[subkey] = ('curr_directory_structure', key)

    # Print the differences
    if len(diff) == 0:
        print("No differences found.")
    for key in diff:
        print(f"{key} is present in {diff[key][0]} but not in {diff[key][1]}")
