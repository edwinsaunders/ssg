import unittest
from block_to_block_type import *

class Test_block_to_block_type(unittest.TestCase):
	def test_heading(self):
		block = '## dfgdfgds'
		self.assertEqual(block_to_block_type(block), BlockType.HEADING)
	def test_code(self):
		block = '```- sdfghsdfg\n- fvcnxsdsd\n- ydghm6ue6```'
		self.assertEqual(block_to_block_type(block), BlockType.CODE)
	def test_quote(self):
		block = '>```- sdfghsdfg\n>- fvcnxsdsd\n>- ydghm6ue6```'
		self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
	def test_unordered(self):
		block = '- sdfghsdfg\n- fvcnxsdsd\n- ydghm6ue6'
		self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
	def test_ordered(self):
		block = '1. sdfghsdfg\n2. fvcnxsdsd\n3. ydghm6ue6'
		self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
	def test_headingFAIL(self):
		block = '####### dfgdfgds'
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	def test_codeFAIL(self):
		block = '```- sdfghsdfg\n- fvcnxsdsd\n- ydghm6ue6``k`'
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	def test_quoteFAIL(self):
		block = '>```- sdfghsdfg\n- fvcnxsdsd\n>- ydghm6ue6```'
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	def test_unorderedFAIL(self):
		block = '- sdfghsdfg\n* fvcnxsdsd\n- ydghm6ue6'
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	def test_orderedFAIL(self):
		block = '1. sdfghsdfg\n3. fvcnxsdsd\n3. ydghm6ue6'
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()