# Directory Structure Generator

A Python-based tool that generates a visual representation of a directory's structure and saves it to a `.txt` file. The tool also counts the total number of files and folders within the specified directory.

---

## Features

- Recursively generates a directory structure in a visually indented format.
- Ignores the `node_modules` folder for clarity in the output.
- Handles permission errors gracefully and skips restricted folders.
- Outputs the total count of files and folders.
- Saves the output to a `.txt` file for easy sharing or documentation.

---

## How It Works

1. Takes a directory path as input.
2. Recursively scans the directory for subdirectories and files.
3. Generates an indented structure showing all subdirectories and files.
4. Counts the total number of files and folders.
5. Saves the output to a user-specified `.txt` file in the `output/` folder.

---

## Prerequisites

Before using this tool, ensure you have:

- **Python 3.6 or higher** installed.

---

## How to Use

1. **Clone the Repository or Download the Script**

   Save the script file `directory_structure.py` to your local machine.

2. **Run the Tool**

   Open a terminal and run the script:
   ```bash
   python directory_structure.py
