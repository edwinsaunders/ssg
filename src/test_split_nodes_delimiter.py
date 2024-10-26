import unittest
from create_old_nodes import *
from split_nodes_delimiter import *

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