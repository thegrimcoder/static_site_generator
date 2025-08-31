import os
import shutil

from textnode import TextNode

def main():
    copy_dir_recursively("static/", "public/")

def copy_dir_recursively(source_path, destination_path):
    print(f"Deleting all contents of '{destination_path}'...")
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    print(f"Recreating destination directory: '{destination_path}'")
    os.mkdir(destination_path)

    print("Starting recursive copy...")
    _copy_recursive(source_path, destination_path)
    print("Copy complete!")

def _copy_recursive(source, destination):
    for item in os.listdir(source):
        source_item_path = os.path.join(source, item)
        destination_item_path = os.path.join(destination, item)

        # Check if the item is a file
        if os.path.isfile(source_item_path):
            print(f"Copying file from '{source_item_path}' to '{destination_item_path}'")
            # Copy the file to the destination
            shutil.copy(source_item_path, destination_item_path)
        # Check if the item is a directory
        elif os.path.isdir(source_item_path):
            print(f"Entering directory: '{source_item_path}'")
            # Create the corresponding directory in the destination
            os.mkdir(destination_item_path)
            # Recursively call the function for the new directory
            _copy_recursive(source_item_path, destination_item_path)

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        line = line.strip()
        print(f"Line: {line}")
        if line.startswith("#"):
            if line.startswith("# "):
                return line.lstrip("# ").strip()
    
    raise Exception("No title header found")


if __name__ == "__main__":
    main()

