import unittest

from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    """
    A test suite for the block_to_block_type function.
    """

    def test_paragraph(self):
        """Test a normal paragraph block."""
        block = "This is a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block_multi_line = "This is a paragraph\nthat spans multiple lines."
        self.assertEqual(block_to_block_type(block_multi_line), BlockType.PARAGRAPH)
        
        block_mixed_content = "Not a list line\n- this looks like a list item\nBut it is a paragraph block because not all lines start with a dash."
        self.assertEqual(block_to_block_type(block_mixed_content), BlockType.PARAGRAPH)

    def test_heading(self):
        """Test different levels of heading blocks."""
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        
        # Negative test cases for headings
        self.assertNotEqual(block_to_block_type("####### Not a heading"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("#No space after hash"), BlockType.HEADING)

    def test_code(self):
        """Test a code block."""
        code_block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        
        # Test a multi-line code block with code that looks like other types
        code_with_other_syntax = "```\n# This is a heading\n> This is a quote\n1. This is a list item\n```"
        self.assertEqual(block_to_block_type(code_with_other_syntax), BlockType.CODE)
        
        # Negative test case
        self.assertNotEqual(block_to_block_type("`Single backtick`"), BlockType.CODE)
        self.assertNotEqual(block_to_block_type("```\nNo closing backticks"), BlockType.CODE)

    def test_quote(self):
        """Test a quote block."""
        quote_block = "> This is a quote."
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        
        quote_multi_line = "> This is a multi-line quote.\n> It has a second line.\n> And a third."
        self.assertEqual(block_to_block_type(quote_multi_line), BlockType.QUOTE)
        
        # Negative test case where not all lines start with '>'
        not_a_quote = "> This is a quote line.\nThis is not."
        self.assertNotEqual(block_to_block_type(not_a_quote), BlockType.QUOTE)

    def test_unordered_list(self):
        """Test an unordered list block."""
        list_block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(list_block), BlockType.UNORDERED_LIST)
        
        list_block_with_space = "-   Item with extra space"
        self.assertEqual(block_to_block_type(list_block_with_space), BlockType.UNORDERED_LIST)
        
        # Negative test case where not all lines start with '- '
        not_a_list = "- List item\nNot a list item"
        self.assertNotEqual(block_to_block_type(not_a_list), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        """Test an ordered list block."""
        ordered_block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ordered_block), BlockType.ORDERED_LIST)
        
        # Negative test case for a non-sequential list
        not_ordered_block = "1. Item\n3. Item"
        self.assertNotEqual(block_to_block_type(not_ordered_block), BlockType.ORDERED_LIST)

        # Negative test case with incorrect starting number
        not_ordered_block_start_at_zero = "0. First item\n1. Second item"
        self.assertNotEqual(block_to_block_type(not_ordered_block_start_at_zero), BlockType.ORDERED_LIST)

    def test_empty_block(self):
        """Test an empty string input."""
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)


if __name__ == '__main__':
    # This will discover and run all test methods in this file
    unittest.main()