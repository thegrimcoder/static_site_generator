from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes import split_nodes_link, split_nodes_image
from node_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    text_nodes = []
    node = TextNode(text, TextType.TEXT, )

    text_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #print(text_nodes)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    #print(text_nodes)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    #print(text_nodes)
    text_nodes = split_nodes_image(text_nodes)
    #print(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    #print(text_nodes)

    return text_nodes
    
    

    
