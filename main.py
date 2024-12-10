import os

def count_files_and_folders(root_dir):
    total_files = 0
    total_folders = 0
    
    for root, dirs, files in os.walk(root_dir):
        total_files += len(files)
        total_folders += len(dirs)
    
    return total_files, total_folders

def generate_directory_structure(root_dir, level=0, prefix="  "):
    structure = ""
    items = []
    
    try:
        items = sorted(os.listdir(root_dir))
    except PermissionError:
        structure += f"{prefix}|--- [Permission Denied]\n"
        return structure
    except Exception as e:
        structure += f"{prefix}|--- [Error: {e}]\n"
        return structure
    
    item_count = len(items)
    
    for i, item in enumerate(items):
        if item != 'node_modules':
            path = os.path.join(root_dir, item)
            if os.path.isdir(path):
                if i == item_count - 1:
                    structure += f"{prefix}|--- {item}/\n"
                    structure += generate_directory_structure(path, level + 1, prefix + "    ")
                else:
                    structure += f"{prefix}|--- {item}/\n"
                    structure += generate_directory_structure(path, level + 1, prefix + "|   ")
            else:
                if i == item_count - 1:
                    structure += f"{prefix}|--- {item}\n"
                    structure += f"{prefix}\n"  # Add extra newline after the last file
                else:
                    structure += f"{prefix}|--- {item}\n"
    
    return structure

def main():
    root_dir = input("Enter the directory to generate the structure for: ")
    output_file = input("Enter the name of the output file: ")
    output_file = 'output/'+output_file+'.txt'
    
    if not os.path.isdir(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
        return
    
    total_files, total_folders = count_files_and_folders(root_dir)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Count : {total_files} files and {total_folders} folders! \n\n")
            f.write("root\n")
            f.write(generate_directory_structure(root_dir))
        print(f"Directory structure saved to 'output/{output_file}'")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    main()
