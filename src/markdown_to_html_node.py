from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                pass
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass
    