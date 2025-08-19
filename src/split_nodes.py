from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        print(f"Node: {node}")
        
        markdown = extract_markdown_images(node.text)
        print(f"Markdown: {markdown}")
        original_text = node.text
        for each in markdown:
            image_alt = each[0]
            image_link = each[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            print(f"Sections: {sections}")

def split_nodes_link(old_nodes):
    new_nodes = []