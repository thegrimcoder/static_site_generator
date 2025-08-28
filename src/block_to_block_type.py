from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    test_string = ""

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split('\n')

    if re.match(r"#{1,6}\s", lines[0]):
        return BlockType.HEADING
    
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

            
            