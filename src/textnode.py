from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = 'code'
	LINK = 'link'
	IMAGE = 'image'

class TextNode:
	def __init__(self, text, text_type, url=None):
		if not isinstance(text_type, TextType):
			raise Exception(f"{text_type} is not a valid text node type")
		if text_type not in TextType:
			raise ValueError(f"Invalid text_type: {text_type}")
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if (
				self.text == other.text and
				self.text_type == other.text_type and
				self.url == other.url
				):
			return True
		return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"




def text_node_to_html_node(text_node):
	
	match text_node.text_type:
		case TextType.TEXT:
			leafnode = LeafNode(None, text_node.text, None, None)
		case TextType.BOLD:
			leafnode = LeafNode('b', text_node.text, None, None)
		case TextType.ITALIC:
			leafnode = LeafNode('i', text_node.text, None, None)
		case TextType.CODE:
			leafnode = LeafNode('code', text_node.text, None, None)
		case TextType.LINK:
			leafnode = LeafNode(
				'a', 
				text_node.text, 
				None, 
				{'href': text_node.url}
				)
		case TextType.IMAGE:
			leafnode = LeafNode(
				'img', 
				"", 
				None, 
				{'src': text_node.url, 'alt': text_node.text}
				)
		case _:
			raise Exception('invalid text type')

	return leafnode

	
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	
	

	


	#handle nodes of type TEXT, not sure if there will be empty stri g if delimiter is at beginning of string
	for node in old_nodes:
		
		#handle nodes with other text types( bold, italic, etc)
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			delim_count = node.text.count(delimiter)
			#count delims, if odd, raise except.
			if not delim_count % 2 == 0:
				raise Exception('invalid Markdown syntax')


			text_split = node.text.split(delimiter)
			if text_split[0] == "":
				start_switch = 0 #starting with MD block
			else:
				start_switch = 1 #starting with plain text
			#if first or last string is empty, remove from list, odd/even switch below, del empty string
			#get rid of empty strings
			text_split = list(filter(lambda x: x != "", text_split))

			#if first is empty, we know odds are going to be diff text type, evens are just plain text
			#otherwise, other way round

			#need to count delims first and raise ex if odd count outide loop? use node.text somehow?
			#delim_count = 0
			for string_index in range(0, len(text_split)):
				if (string_index + 1) % 2 == start_switch:
					new_nodes.append(LeafNode(text_split[string_index], TextType.TEXT, node.url))
				else:
					new_nodes.append(LeafNode(text_split[string_index], text_type, node.url))
	return new_nodes