import os
from config import MAX_CHARS

def get_files_info(working_directory, directory = "."):
    full_path = os.path.join(working_directory, directory)
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(full_path)
    
    # check to ensure the target directory follows the same path as the working directory
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for filename in os.listdir(abs_target_dir):
            filepath = os.path.join(abs_target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: Error listing files: {e}"
    
    
def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(full_path)
    
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read()) > 10000:
                file_content_string = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
                
            return file_content_string
    except Exception as e:
        return f"Error: Error reading file: {e}"