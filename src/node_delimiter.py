from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_strings = node.text.split(delimiter, -1)
            if len(split_strings) <= 2:
                pass
                #raise Exception("Matching Delimiter Not Found")
                #new_nodes.append(node)
            text_string = True
            for string in split_strings:
                if text_string == True:
                    new_nodes.append(TextNode(string, TextType(node.text_type)))
                    text_string = False
                else:
                    new_nodes.append(TextNode(string, TextType(text_type)))
                    text_string = True
        else:
            new_nodes.append(node)
    return new_nodes