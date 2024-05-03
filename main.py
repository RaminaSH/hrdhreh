import os
import shutil

# Set the directory where you want to delete photos
directory = '/path/to/directory'

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Function to delete files with specified extensions
def delete_files(dir_path, extensions):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1].lower()
            if file_ext in extensions:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# Call the delete_files function with the desired directory and extensions
delete_files(directory, image_extensions)