import os

def rename_files(directory_path, base_name):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Iterate through all files in the directory
    for count, filename in enumerate(os.listdir(directory_path), start = 5):
        old_file_path = os.path.join(directory_path, filename)

        if os.path.isfile(old_file_path):
            # Extract the original file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Construct the new filename with an incrementing number
            new_filename = f"{base_name}_{count}{file_extension}"
            new_file_path = os.path.join(directory_path, new_filename)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
            except Exception as e:
                print(f"Failed to rename '{filename}': {e}")

target_directory = "./mahayahay/" 
desired_name = "mahayahay"

rename_files(target_directory, desired_name)