import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_delimiter import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):
    def test_node_delimiter_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #print(new_nodes)

    def test_node_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(new_nodes)

    def test_node_delimiter_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        #print(new_nodes)
        
    def test_node_delimiter_no_delimiter(self):
        node = TextNode("This is text with an _italic word", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "_", TextType.ITALIC))

if __name__ == "__main__":
    unittest.main()