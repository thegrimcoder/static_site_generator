from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_strings = node.split(delimiter, -1)
            for string in split_strings:
                print(string)
        else:
            new_nodes.extend(node)
    return new_nodes