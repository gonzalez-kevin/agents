import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(full_path)
    
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        target_dir = os.path.dirname(abs_target_file)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        with open(abs_target_file, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Could not write to file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to python file in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to write the python file to, relative to the working directory.",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "The content to write to the file."
            )
        },
    ),
)