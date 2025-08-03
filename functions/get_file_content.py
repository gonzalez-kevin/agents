import os
from config import MAX_CHARS

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