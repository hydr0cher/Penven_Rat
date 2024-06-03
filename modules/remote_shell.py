# modules/remote_shell.py

import subprocess
from ..encryption import encrypt_data

# Function to execute shell command
def execute_command(command):
    output = subprocess.getoutput(command)
    return output
