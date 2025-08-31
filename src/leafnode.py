from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        print(f"Tag: {self.tag}, Value: {self.value}")
        if self.value is None:
            raise ValueError("No value")
        if self.tag is None:
            return self.value
        else:
            html_string = self.props_to_html()
            print(f"HTML String: {html_string}")
            return f"<{self.tag}{html_string}>{self.value}</{self.tag}>"