# Python Trash Cleaner 🗑🧹
 🧹 TRASH Cleaner: Python script to tidy up files and directories in a specified folder, excluding designated exceptions, and empty the recycle bin. 🚀

## Overview

🗑️ TRASH Cleaner: Python script for efficient cleanup in the current directory, sparing exceptions, and ensuring a tidy workspace. 🚀

## Features

- Removes all files and directories from a specified folder, except for an exception file (`main.py` in this case).
- Empties the recycle bin to permanently delete the removed items.

## Requirements

Before running the script, ensure you have the following installed:

- **Python 3:** If not installed, download and install from [python.org](https://www.python.org/downloads/).
- **WinShell:** Install it using the following command:

    ```bash
    pip install winshell
    ```
## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/neuqs0035/python-trash-cleaner.git
   cd python-trash-cleaner
   ```
2. **Run Script:**
   ```bash
   python main.py
   ```

## Schedule Trash Cleaner

1. Configure Task In Task Scheduler

   - Open Windows Task Scheduler (Win + S and type "Task Scheduler").
   - Click on "Create Basic Task."
     
2. Set Task Name And Trigger

   - Name your task and provide an optional description.
   - Choose a trigger that suits your needs (e.g., daily, weekly, or at logon).
     
3. Set Action

   - Select "Start a program" as the action.
   - Browse and select the Python executable (e.g., C:\Python39\python.exe).
   - Set the "Add arguments" field to the path of the main.py script (e.g., C:\path\to\trach-cleaner\main.py).
     
4. Finish
   - Review your settings and click "Finish" to create the scheduled task.

## Notes:

- Ensure that Python is added to your system's PATH to execute the script via Task Scheduler.
- For troubleshooting or detailed logs, consider redirecting the script output to a log file.
