from markdown_to_blocks import *
import unittest

class Test_markdown_to_blocks(unittest.TestCase):
	def test_good_md(self):
		test_good = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
		self.assertListEqual(
			[
			'# This is a heading', 
			'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
			'* This is the first list item in a list block\n* This is a list item\n* This is another list item'
			],
			markdown_to_blocks(test_good)
		)

	def test_bad_md(self):
		test_bad = "# This is a heading   \n\n\n\n    This is a paragraph of text. It has some **bold** and *italic* words inside of it. \n\n\n\n * This is the first list item in a list block\n* This is a list item\n* This is another list item  "
		self.assertListEqual(
			[
			'# This is a heading', 
			'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
			'* This is the first list item in a list block\n* This is a list item\n* This is another list item'
			],
			markdown_to_blocks(test_bad)
		)

if __name__ == "__main__":
    unittest.main()