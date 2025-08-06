from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(self, tag, value, chlidren=None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            html_string = self.props_to_html()
            print(f"HTML String: {html_string}")
            return f'"<{self.tag}{html_string}>{self.value}</{self.tag}>"'