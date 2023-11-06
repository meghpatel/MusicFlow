import os
import pickle
import zipfile
from verify_directory import get_directory_structure

current_os = os.name

DATA_PATH = "Apple Music Activity/"
files = os.listdir(DATA_PATH)

zip_files = []

for file in files:
    if file.endswith(".zip"):
        zip_files.append(file)

print ("ZIP Files: ", zip_files)

for zip_file in zip_files:
    with zipfile.ZipFile(DATA_PATH + zip_file, 'r') as zip_ref:
        zip_ref.extractall(DATA_PATH)
        os.remove(DATA_PATH + zip_file)

exclude_dirs = [".stfolder"]
for root, dirs, files in os.walk(DATA_PATH):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for dir in dirs:
        for file in os.listdir(os.path.join(root, dir)):
            os.rename(os.path.join(root, dir, file), os.path.join(DATA_PATH, file))

# Remove empty directories
for root, dirs, files in os.walk(DATA_PATH, topdown=False):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))

print("All zip files have been extracted and removed, and files have been moved outside of directories.")

current_directory_structure = get_directory_structure(DATA_PATH)

# Save directory_structure to a file named directory_structure.pkl
with open('current_directory_structure.pkl', 'wb') as f:
    pickle.dump(current_directory_structure, f)