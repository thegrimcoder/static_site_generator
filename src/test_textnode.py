import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2, "Not Equal")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not equal", TextType.BOLD)
        self.assertNotEqual(node, node2, "Equal")

    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is not equal", TextType.BOLD)
        print(node.text_type)
        self.assertNotEqual(node, node2, "Equal")

if __name__ == "__main__":
    unittest.main()