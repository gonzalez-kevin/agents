import os

def get_files_info(working_directory, directory = "."):
    full_path = os.path.join(working_directory, directory)
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(full_path)
    
    # check to ensure the target directory follows the same path as the working directory
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    directory_items = os.listdir(directory)
    for item in directory_items:
        return f"- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(file)}\n"