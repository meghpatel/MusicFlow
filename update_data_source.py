"""
This script extracts zip files, updates data directories,
moves files outside of directories, and updates a configuration file.
"""
import os
import shutil
import zipfile
from datetime import datetime
import json

DATA_PATH = "Apple Music Activity/"
NEW_DATA_PATH = "New Data/Apple Music Activity"
BACKUP_FOLDER = "backup/"
CONFIG_FILE = 'config.json'
files = os.listdir(DATA_PATH)

zip_files = []

def get_date_modified(folder):
    """Get the date modified of a folder

    Args:
        folder (string): Path to the folder

    Returns:
        datetime: Date modified of the folder
    """
    return datetime.fromtimestamp(os.path.getmtime(folder))

def is_file_copy_required():
    """Check if the files need to be copied to the new data directory

    Returns:
        boolean: True if the files need to be copied, False otherwise
    """
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        if os.stat(CONFIG_FILE).st_size == 0:
            return True
        else:
            config = json.load(f)
            return config['last_updated'] < get_date_modified(NEW_DATA_PATH).isoformat()

def update_config():
    """ Update the configuration file with the current date and time
    """
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        config = {
            'last_updated': datetime.now().isoformat()
        }
        json.dump(config, f)

def copy_folder(source, destination):
    """Copy the contents of a folder to another folder

    Args:
        source (string): Path to the source folder
        destination (string): Path to the destination folder
    """
    os.makedirs(destination, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(f"Contents of '{source}' copied to '{destination}'")

def delete_folder(data_folder):
    """Delete a folder and its contents

    Args:
        DATA_FOLDER (string): Path to the folder to be deleted
    """
    shutil.rmtree(data_folder)

if is_file_copy_required():

    copy_folder(DATA_PATH, os.path.join(BACKUP_FOLDER, 'OLD_APPLE_MUSIC_ACTIVITY'))
    copy_folder(NEW_DATA_PATH, os.path.join(BACKUP_FOLDER, 'NEW_APPLE_MUSIC_ACTIVITY'))

    delete_folder(DATA_PATH)
    os.makedirs(DATA_PATH, exist_ok=True)
    copy_folder(NEW_DATA_PATH, DATA_PATH)
    update_config()

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
    for directory in dirs:
        for file in os.listdir(os.path.join(root, directory)):
            os.rename(os.path.join(root, directory, file), os.path.join(DATA_PATH, file))

# Remove empty directories
for root, dirs, files in os.walk(DATA_PATH, topdown=False):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for directory in dirs:
        os.rmdir(os.path.join(root, directory))

print ("""All zip files have been extracted and removed, \
    and files have been moved outside of directories.""")
