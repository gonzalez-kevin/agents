import os
import subprocess

def run_python_file(working_directory, file_path, args = []):
    full_path = os.path.join(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(full_path)
    
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target_file.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'
        
    try:
        completed_process = subprocess.run(timeout=30, capture_output = True, check = True, text = True, args = ["python", abs_target_file] + args, cwd = abs_working_dir)
        if completed_process.returncode == 0:
            return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        elif completed_process.returncode != 0:
            return f"Process exited with code {completed_process.returncode}"
        elif not completed_process.returncode:
            return "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"