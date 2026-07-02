import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files = os.listdir(source_folder)

for file in files:
    source = os.path.join(source_folder, file)
    destination = os.path.join(destination_folder, file)

    if os.path.isfile(source):
        shutil.copy(source, destination)

print("All files copied successfully!")