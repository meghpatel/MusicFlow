import os

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

print ("JSON Files: ", json_files)
print ("CSV Files: ", csv_files)