#!/usr/bin/python3
import os

def set_all_permissions(directory_path):
    # Check if the specified directory exists
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if it's a regular file
        if os.path.isfile(file_path):
            try:
                # Set read, write, and execute permissions for owner, group, and others
                os.chmod(file_path, 0o777)  # 7 = read, write, and execute permission

                print(f"Permissions updated for {filename}")
            except Exception as e:
                print(f"Error updating permissions for {filename}: {e}")

if __name__ == "__main__":
    # Specify the correct directory path within the Docker container
    directory_path = "/alx-higher_level_programming/0x0F-python-object_relational_mapping"

    set_all_permissions(directory_path)
