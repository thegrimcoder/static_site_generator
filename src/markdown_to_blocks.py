from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def markdown_to_blocks(markdown):
    markdown_list = []

    temp_list = markdown.split("\n\n")

    for string in temp_list:
        if string:
            markdown_list.append(string.strip())

    #print(markdown_list)
    return markdown_list