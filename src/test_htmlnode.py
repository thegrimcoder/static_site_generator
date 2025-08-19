import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1","This is a test",[],{"href": "https://www.google.com", "target": "_blank"})
        #print(node.props_to_html())

    def test_print_node(self):
        node = HTMLNode("h1","This is a test",[],{"href": "https://www.google.com", "target": "_blank"})
        #print(node)

    def test_none_value(self):
        node = HTMLNode("h1", None,[],{"href": "https://www.google.com", "target": "_blank"})
        self.assertIsNone(node.value)

if __name__ == "__main__":
    unittest.main()