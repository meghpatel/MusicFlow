import os
import pickle
import zipfile

current_os = os.name

DATA_PATH = "Apple Music Activity/"
files = os.listdir(DATA_PATH)

zip_files = []

# Create a list of zip files
for file in files:
    if file.endswith(".zip"):
        zip_files.append(file)

print ("ZIP Files: ", zip_files)

# Extract all zip files to the parent folder and delete the zip files
for zip_file in zip_files:
    with zipfile.ZipFile(DATA_PATH + zip_file, 'r') as zip_ref:
        zip_ref.extractall(DATA_PATH)
        os.remove(DATA_PATH + zip_file)

# Move all files outside of directories
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

# current_directory_structure = get_directory_structure(DATA_PATH)

# # Check if .pkl file exists, if it exists, load it
# if os.path.exists('current_directory_structure.pkl'):
#     with open('current_directory_structure.pkl', 'rb') as f:
#         previous_directory_structure = pickle.load(f)
# else:
#     # Save directory_structure to a file named directory_structure.pkl
#     with open('current_directory_structure.pkl', 'wb') as f:
#         pickle.dump(current_directory_structure, f)

# # Compare the current directory structure with the previous directory structure
# if current_directory_structure == previous_directory_structure:
#     print("The directory structure has not changed.")
# else:
#     print("The directory structure has changed.")

