import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href:"https://www.google.com" target:"_blank"')

if __name__ == "__main__":
    unittest.main()