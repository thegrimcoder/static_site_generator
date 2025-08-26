from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    test_string = ""
    temp_block = block
    block_lines = block.splitlines()

    for char in temp_block:
        test_string += char

        if test_string == "#" or test_string == "##" or test_string == "###" or test_string == "####" or test_string == "#####":
            continue

        if test_string == "# " or test_string == "## " or test_string == "### " or test_string == "#### " or test_string == "##### " or test_string == "###### ":
            return BlockType.HEADING
        
        if test_string == "`" or test_string == "``":
            continue

        if test_string == "```" and block[-3:] == "```":
            return BlockType.CODE
        

    for line in block_lines:
        if line:
            first_char = line[0]
        
        