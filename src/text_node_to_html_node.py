from htmlnode import *

#takes a text node and returns a leaf html node
def text_node_to_html_node(text_node):
	
	match text_node.text_type:
		case 'text':
			leafnode = LeafNode(None, text_node.text)
		case 'bold':
			leafnode = LeafNode('b', text_node.text)
		case 'italic':
			leafnode = LeafNode('i', text_node.text)
		case 'code':
			leafnode = LeafNode('code', text_node.text)
		case 'link':
			leafnode = LeafNode(
				'a', 
				text_node.text, 
				{'href': text_node.url}
				)
		case 'image':
			leafnode = LeafNode(
				'img', 
				"", 
				{'src': text_node.url, 'alt': text_node.text}
				)
		case _:
			raise Exception(f'invalid text type: {text_node.text_type}')

	return leafnode