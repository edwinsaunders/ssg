import unittest
from textnode import *
from text_node_to_html_node import *

class Test_text_node_to_html_node(unittest.TestCase):
	
	textnode_t = TextNode("text", TextType.TEXT, None)
	textnode_b = TextNode("bold text", TextType.BOLD, None)
	textnode_it = TextNode("italic text", TextType.ITALIC, None)
	textnode_c = TextNode("def codetext(): return", TextType.CODE, None)
	textnode_l = TextNode("link text", TextType.LINK, "http://www.test.com")
	textnode_im = TextNode("img alt text", TextType.IMAGE, "http://www.imgsrc.com")


	def test_text(self):        
		compare_node = LeafNode(None, "text", None)       
		self.assertEqual(text_node_to_html_node(self.textnode_t), compare_node)
	def test_bold(self):
		compare_node = LeafNode('b', "bold text", None)       
		self.assertEqual(text_node_to_html_node(self.textnode_b), compare_node)
	def test_italic(self):
		compare_node = LeafNode('i', "italic text", None)     
		self.assertEqual(text_node_to_html_node(self.textnode_it), compare_node)
	def test_code(self):
		compare_node = LeafNode('code', "def codetext(): return", None)       
		self.assertEqual(text_node_to_html_node(self.textnode_c), compare_node)
	def test_link(self):
		compare_node = LeafNode('a', "link text", {'href': 'http://www.test.com'})        
		self.assertEqual(text_node_to_html_node(self.textnode_l), compare_node)
	def test_image(self):
		compare_node = LeafNode('img', "", {'src': 'http://www.imgsrc.com', 'alt': "img alt text"})       
		self.assertEqual(text_node_to_html_node(self.textnode_im), compare_node)
	
	# Decision was made to forego testing of exeption raising functionality since python3
		# library modules catch this exception before the text node can be passed to my function
		# Will use try/except block around text node instantiation in main() 


if __name__ == "__main__":
	unittest.main()