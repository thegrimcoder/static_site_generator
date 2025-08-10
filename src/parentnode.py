from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No Tag")
        elif self.children is None:
            raise ValueError("No children")
        else:
            html_string = f"<{self.tag}>"
            
            for child in self.children:
                html_string += child.to_html()
            
            html_string += f"</{self.tag}>"

            return html_string