from markdown_to_blocks import *
import unittest

class Test_markdown_to_blocks(unittest.TestCase):
	def test_good_md(self):
		self.assertListEqual(
			[
			'# This is a heading', 
			'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
			'* This is the first list item in a list block\n* This is a list item\n* This is another list item'
			],
			markdown_to_blocks('src/test_good.md')
		)

	def test_bad_md(self):
		self.assertListEqual(
			[
			'# This is a heading', 
			'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
			'* This is the first list item in a list block\n* This is a list item\n* This is another list item'
			],
			markdown_to_blocks('src/test_bad.md')
		)