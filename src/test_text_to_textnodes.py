import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_nodes(self):
       new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
       self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT, None),
                TextNode("text", TextType.BOLD, None),
                TextNode(" with an ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" word and a ", TextType.TEXT, None),
                TextNode("code block", TextType.CODE, None),
                TextNode(" and an ", TextType.TEXT, None),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT, None),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()