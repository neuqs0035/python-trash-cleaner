import os
import winshell
import shutil

folder_path = os.path.abspath(os.path.dirname(__file__))
exception_file = "main.py"

all_files = os.listdir(folder_path)

for file_name in all_files:
    file_path = os.path.join(folder_path, file_name)

    # Skip main.py
    if file_name == exception_file:
        continue

    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Removed file: {file_name}")
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
        print(f"Removed directory: {file_name}")

# Empty the recycle bin
winshell.recycle_bin().empty()
