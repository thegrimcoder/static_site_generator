from enum import Enum

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""

        if not self.props:
            return ""

        for k, v in self.props.items():
            html_string += f' {k}:"{v}"'

        return html_string
        
    def __repr__(self):
        #html_string = self.props_to_html()
        return f"tag: {self.tag} - value: {self.value} - children: {len(self.children) if self.children else 0} - props:{self.props}"