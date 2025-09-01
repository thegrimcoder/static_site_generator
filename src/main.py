import os
import shutil
import sys

from markdown_to_html_node import markdown_to_html_node
from textnode import TextNode

def main():
    if sys.argv:
        basepath = sys.argv
    else:
        basepath = "/"
    copy_dir_recursively("static/", "docs/")
    generate_pages_recursive("content/", "./template.html", "docs/", basepath)

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
        #print(f"Line: {line}")
        if line.startswith("#"):
            if line.startswith("# "):
                return line.lstrip("# ").strip()
    
    raise Exception("No title header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path, 'r') as f:
            markdown = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at: {from_path}")
    try:
        with open(template_path, 'r') as f:
            template = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at: {template_path}")
    html_node = markdown_to_html_node(markdown)

    #print(f"HTML Node: {html_node}")

    html_str = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    with open(dest_path, 'w') as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")
    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)) and item.endswith(".md"):
            new_file = item.replace(".md", ".html")
            generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, new_file), basepath)
        elif os.path.isdir(os.path.join(dir_path_content, item)):
            if not os.path.isdir(os.path.join(dest_dir_path, item)):
                os.mkdir(os.path.join(dest_dir_path, item))
                generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)
            else:
                generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)
    

if __name__ == "__main__":
    main()

