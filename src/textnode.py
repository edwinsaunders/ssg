import re
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
		#if not isinstance(text_type, TextType):
		#	raise Exception(f"{text_type} is not a valid text node type")
		#if text_type not in TextType:
		#	raise ValueError(f"Invalid text_type: {text_type}")
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
	delimiters = ('*', '**', '`')
	regexes = (r'(?<!\*)\*(?!\*)', r'\*\*', r'`')
	#print(old_nodes[0].text_type)
	#handle nodes of type TEXT, not sure if there will be empty stri g if delimiter is at beginning of string
	#print(old_nodes)
	loop_count = 0
	for node in old_nodes:
		#print(node.text_type)
		#handle nodes with other text types( bold, italic, etc)
		if node.text_type is not TextType.TEXT:
			new_nodes.append(node)
		else:
			d_index = delimiters.index(delimiter)
			delim_count = len(re.findall(regexes[d_index], node.text)) #count delimiters
			
			#delim_count = node.text.count(delimiter)
			#count delims, if odd, raise except.
			if not delim_count % 2 == 0:
				raise Exception('invalid Markdown syntax')

			text_split = re.split(regexes[d_index], node.text)
			#text_split = node.text.split(delimiter)
			if text_split[0] == "":
				start_switch = 0 #starting with MD block
			else:
				start_switch = 1 #starting with plain text
			#if first or last string is empty, remove from list, odd/even switch below, del empty string
			#get rid of empty strings
			text_split = list(filter(lambda x: x != "", text_split))
			#print(loop_count)
			#print(text_split)
			#if first is empty, we know odds are going to be diff text type, evens are just plain text
			#otherwise, other way round
			#print(start_switch)
			#need to count delims first and raise ex if odd count outide loop? use node.text somehow?
			#delim_count = 0
			for string_index in range(0, len(text_split)):
				if (string_index + 1) % 2 == start_switch:
					#print('test')
					new_nodes.append(TextNode(text_split[string_index], TextType.TEXT, node.url))
				else:
					new_nodes.append(TextNode(text_split[string_index], text_type, node.url))
		#loop_count += 1
	return new_nodes

def create_old_nodes():
	old_nodes = []
	#string = 'dfgdafg `dsg sdfgg s*dfgg sdfgsdfgsdhfa'
	string = 'Decision *was* made to **forego** `testing` exeption raising **functionality** since `python3`'
	doc_invalid = 'library modules catch this\nexception before the text node\ncan be passed to my function'
	doc3 = 'Will use try/except block around text node instantiation in main()'

	delimiters = ('*', '**', '`')
	regexes = (r'(?<!\*)\*(?!\*)', r'\*\*', r'`')
	
	#break off chunks
	current_delim = ""
	current_delim_pos = -1

	remaining_string = string
	# loop to breakdown string into list of strings every time a delim is encountered that is not the current delim

	# while there are still delimiters in the remaining string
	string_list = []
	loop_count = 0


	

	
	while(current_delim_pos != float('inf') and remaining_string != ''):
		
		current_delim_pos = float('inf')
		#find first delim type in remaining_string
		for i in range(0, len(delimiters)):


			match = re.search(regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the match
					current_delim = delimiters[i]
					current_regex = regexes[i]		# or you can use match.end() for the ending position
			else:
				continue

		

		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			#print(string_list)
			break
		

		# create new delim tuple and regex tuple without current_delim an delim regex
		delim_index = delimiters.index(current_delim)
		new_delims = delimiters[:delim_index] + delimiters[delim_index + 1:]
		regex_index = regexes.index(current_regex)
		new_regexes = regexes[:regex_index] + regexes[regex_index + 1:]
		
		
		
		#reset current_delim_pos to inf, otherwise it will always be 0, less than pos of next delim type
		current_delim_pos = float('inf')



		for i in range(0, len(new_delims)):


			match = re.search(new_regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the match
					current_delim = new_delims[i]
					current_regex = new_regexes[i]		# or you can use match.end() for the ending position
			else:
				continue


		
		
		
		
		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			#print('\n')
			#print(string_list)
			break
		
		

		#split off one chunk on current_delim, append to list of strings to iterate through later

		chunk = remaining_string[:current_delim_pos]
		string_list.append(chunk)
		remaining_string = remaining_string[current_delim_pos:]
		

		#repeat for remainder of string while current_delim_pos != -1
		loop_count += 1


	types = (TextType.ITALIC, TextType.BOLD, TextType.CODE)
	for i in range(0, len(string_list)):
		for j in range(0, len(delimiters)):
			match = re.search(regexes[j], string_list[i]) #find delim
			if match:
				nodetype = types[j]
				delim = delimiters[j]
				break
		old_nodes.append(TextNode(string_list[i], TextType.TEXT))

	return old_nodes
