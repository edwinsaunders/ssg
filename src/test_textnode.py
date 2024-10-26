import unittest

from textnode import *
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
	def test_eq_nourl(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("This too is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD, "http://www.zombo.com")
		self.assertNotEqual(node, node2)

	def test_eq_url(self):
		node = TextNode("This three is a text node", TextType.BOLD, "http://www.github.com")
		node2 = TextNode("This three is a text node", TextType.BOLD, "http://www.github.com")
		self.assertEqual(node, node2)

	def test_one_url(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD, "http://www.github.com")
		self.assertNotEqual(node, node2)


class Test_text_node_to_html_node(unittest.TestCase):
	
	textnode_t = TextNode("text", TextType.TEXT, None)
	textnode_b = TextNode("bold text", TextType.BOLD, None)
	textnode_it = TextNode("italic text", TextType.ITALIC, None)
	textnode_c = TextNode("def codetext(): return", TextType.CODE, None)
	textnode_l = TextNode("link text", TextType.LINK, "http://www.test.com")
	textnode_im = TextNode("img alt text", TextType.IMAGE, "http://www.imgsrc.com")


	def test_text(self):        
		compare_node = LeafNode(None, "text", None, None)       
		self.assertEqual(text_node_to_html_node(self.textnode_t), compare_node)
	def test_bold(self):
		compare_node = LeafNode('b', "bold text", None, None)       
		self.assertEqual(text_node_to_html_node(self.textnode_b), compare_node)
	def test_italic(self):
		compare_node = LeafNode('i', "italic text", None, None)     
		self.assertEqual(text_node_to_html_node(self.textnode_it), compare_node)
	def test_code(self):
		compare_node = LeafNode('code', "def codetext(): return", None, None)       
		self.assertEqual(text_node_to_html_node(self.textnode_c), compare_node)
	def test_link(self):
		compare_node = LeafNode('a', "link text", None, {'href': 'http://www.test.com'})        
		self.assertEqual(text_node_to_html_node(self.textnode_l), compare_node)
	def test_image(self):
		compare_node = LeafNode('img', "", None, {'src': 'http://www.imgsrc.com', 'alt': "img alt text"})       
		self.assertEqual(text_node_to_html_node(self.textnode_im), compare_node)
	
	# Decision was made to forego testing exeption raising functionality since python3
		# library modules catch this exception before the text node can be passed to my function
		# Will use try/except block around text node instantiation in main() 

class Test_split_nodes_delimiter(unittest.TestCase):
	#test input sets
		#use several different test strings to plug into create_old_nodes func
		#plug old_nodes returned by that func into split nodes delimiter func
		#figure out how to process, it seems like each set of old nodes will 
			#need to be processed 3 times, one for each delimiter
		
	doc_perfect = 'Decision *was* made to **forego** `testing` exeption raising **functionality** since `python3`'
	#doc_invalid = 'library modules catch this\nexception before the text node\ncan be passed to my function'
	#doc3 = 'Will use try/except block around text node instantiation in main()'

	
	#test functions

	def test_all_at_once(self):
		#doc_perfect = 'Decision *was* made to **forego** `testing` exeption raising **functionality** since `python3`'
		nodes = create_old_nodes(self.doc_perfect)

		new_nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
		new_new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
		new_new_new_nodes = split_nodes_delimiter(new_new_nodes, '**', TextType.BOLD)
		control_list = [
		TextNode('Decision ', TextType.TEXT, None),
		TextNode('was', TextType.ITALIC, None),
		TextNode(' made to ', TextType.TEXT, None),
		TextNode('forego', TextType.BOLD, None),
		TextNode(' ', TextType.TEXT, None),
		TextNode('testing', TextType.CODE, None),
		TextNode(' exeption raising ', TextType.TEXT, None),
		TextNode('functionality', TextType.BOLD, None),
		TextNode(' since ', TextType.TEXT, None),
		TextNode('python3', TextType.CODE, None)
		]
		#print(new_new_new_nodes)
		#print(control_list)
		self.assertEqual(new_new_new_nodes, control_list)

	def test_code_delim(self):
		nodes = create_old_nodes(self.doc_perfect)

		new_nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)

		control_list = [
		TextNode('Decision *was* made to ', TextType.TEXT, None),
		TextNode('**forego** ', TextType.TEXT, None),
		TextNode('testing', TextType.CODE, None),
		TextNode(' exeption raising ', TextType.TEXT, None),
		TextNode('**functionality** since ', TextType.TEXT, None),
		TextNode('python3', TextType.CODE, None)
		]

		self.assertEqual(new_nodes, control_list)

	def test_italic_delim(self):
		nodes = create_old_nodes(self.doc_perfect)

		new_nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)

		control_list = [
		TextNode('Decision ', TextType.TEXT, None),
		TextNode('was', TextType.ITALIC, None),
		TextNode(' made to ', TextType.TEXT, None),
		TextNode('**forego** ', TextType.TEXT, None),
		TextNode('`testing` exeption raising ', TextType.TEXT, None),
		TextNode('**functionality** since ', TextType.TEXT, None),
		TextNode('`python3`', TextType.TEXT, None)
		]
		#print(new_nodes)
		self.assertEqual(new_nodes, control_list)

	def test_bold_delim(self):
		nodes = create_old_nodes(self.doc_perfect)

		new_nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)

		control_list = [
		TextNode('Decision *was* made to ', TextType.TEXT, None),
		TextNode('forego', TextType.BOLD, None),
		TextNode(' ', TextType.TEXT, None),
		TextNode('`testing` exeption raising ', TextType.TEXT, None),
		TextNode('functionality', TextType.BOLD, None),
		TextNode(' since ', TextType.TEXT, None),
		TextNode('`python3`', TextType.TEXT, None)
		]
		#print(new_nodes)
		self.assertEqual(new_nodes, control_list)


if __name__ == "__main__":
	unittest.main()