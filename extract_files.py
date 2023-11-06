import os
import zipfile

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
        
print("All zip files have been extracted.")