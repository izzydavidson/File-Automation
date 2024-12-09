#Sorting File Types
import os
import shutil

def organize_and_rename_files(source_folder):
    # Define file type groups and corresponding folder names
    file_groups = {
        '.docx': 'word',
        '.xlsx': 'excel',
        '.csv': 'csv',
        '.pod5': 'pod5',
        '.fastq': 'fastq',
        '.fast5': 'fast5',
        '.pdf': 'pdf' 
    }
    
    # Create subfolders and organize files
    for file_type, folder_name in file_groups.items():
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Process files in the source folder
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify file extension
        file_extension = os.path.splitext(file_name)[1].lower()

        # Check if the file type is in our defined groups
        if file_extension in file_groups:
            # Move and rename the file
            folder_name = file_groups[file_extension]
            folder_path = os.path.join(source_folder, folder_name)

            # Generate new file name
            new_file_name = f"{folder_name}_{len(os.listdir(folder_path)) + 1}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)

            # Move the file to its respective folder
            shutil.move(file_path, new_file_path)

            print(f"Moved and renamed: {file_name} -> {new_file_name}")

# Example usage
source_folder = "/Users/izzydavidson/Desktop/mixed_files"  # Replace with your folder path
organize_and_rename_files(source_folder)
