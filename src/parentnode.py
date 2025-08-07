from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super.__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        elif not self.children:
            raise ValueError("No children")
        else:
            