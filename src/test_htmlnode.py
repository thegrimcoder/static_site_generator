import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1","This is a test",[],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1","This is a test",[],{"href": "https://www.google.com", "target": "_blank"})
        print(node.props_to_html())

    def test_not_eq(self):
        #node = TextNode("This is a text node", TextType.BOLD)
        #node2 = TextNode("This is not equal", TextType.BOLD)
        #self.assertNotEqual(node, node2)
        pass

    def test_type_not_eq(self):
        #node = TextNode("This is a text node", TextType.ITALIC)
        #node2 = TextNode("This is not equal", TextType.BOLD)
        #self.assertNotEqual(node, node2)
        pass

if __name__ == "__main__":
    unittest.main()