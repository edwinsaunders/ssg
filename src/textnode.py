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
		return f"TextNode({self.text}, {self.text_type}, {self.url})\n"




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

	#handle nodes of type TEXT, not sure if there will be empty stri g if delimiter is at beginning of string

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

			
			# figure out whther list of string starts with MD block or plain text block
				#based on presence of empty string at index 0 or not
			text_split = re.split(regexes[d_index], node.text)
			if text_split[0] == "":
				start_switch = 0 #starting with MD block
			else:
				start_switch = 1 #starting with plain text
			
			#if first or last string is empty, remove from list, odd/even switch below, del empty string
			#get rid of empty strings
			text_split = list(filter(lambda x: x != "", text_split))
			
			#if first is empty, we know odds are going to be diff text type, evens are just plain text
				#otherwise, other way round
			for string_index in range(0, len(text_split)):
				if (string_index + 1) % 2 == start_switch:
					#print('test')
					new_nodes.append(TextNode(text_split[string_index], TextType.TEXT, node.url))
				else:
					new_nodes.append(TextNode(text_split[string_index], text_type, node.url))
	return new_nodes

#function to partially parse document string into list of TextNode objects, all of type TextNode.TEXT
	#to feed into split_nodes_delimiter function
def create_old_nodes(string):
	old_nodes = []

	
	#Using these two tuples in parallel to find/ delimiters.  delim and corrsponding
		#regex need to have same index
	delimiters = ('*', '**', '`')
	regexes = (r'(?<!\*)\*(?!\*)', r'\*\*', r'`')
	
	current_delim = ""
	current_delim_pos = -1

	remaining_string = string
	
	string_list = []
	
	# while there are still delimiters in the remaining string
	# loop to breakdown string into list of strings every time a delim is encountered that is not the current delim
	while(current_delim_pos != float('inf') and remaining_string != ''):
		
		current_delim_pos = float('inf')
		#find first delim type in remaining_string
		for i in range(0, len(delimiters)):

			#find regex that corresponds to delim
			match = re.search(regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the delim
					current_delim = delimiters[i]
					current_regex = regexes[i]
			else:
				#if current delim type being searched for is not found, skip iteration to look for next delim type
				continue

		
		#if no delims found, put entire remaining string into string list break out of loop
		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			break
		

		# create new delim tuple and regex tuple without current_delim an delim regex
			#in order to use same process as above to find next delim type
			#creates tuples with the remaining delim types that have not been encountered yet
		delim_index = delimiters.index(current_delim)
		new_delims = delimiters[:delim_index] + delimiters[delim_index + 1:]
		regex_index = regexes.index(current_regex)
		new_regexes = regexes[:regex_index] + regexes[regex_index + 1:]
		
		
		
		#reset current_delim_pos to inf for comparison later if no delims found searching for next delim type
		current_delim_pos = float('inf')


		#find next delim type in doc string using same process for finding the first one above
		for i in range(0, len(new_delims)):


			match = re.search(new_regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the next delim type
					current_delim = new_delims[i]
					current_regex = new_regexes[i]
			else:
				#skip iteration if curent delim type not found
				continue

		
		#if no other delims found, put entire remaining string into string list break out of loop
		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			break
				

		#split off one chunk on current_delim, append to list of strings to iterate through later
		chunk = remaining_string[:current_delim_pos]
		string_list.append(chunk)

		#set remaining string to eveything except the chunk that was split off from the beginning
		remaining_string = remaining_string[current_delim_pos:]
		

		#repeat for remainder of string while current_delim_pos != -1

	# this code may prove useful for something later
	# SAVE - types = (TextType.ITALIC, TextType.BOLD, TextType.CODE)
	# SAVE - for i in range(0, len(string_list)):
	# SAVE - 	for j in range(0, len(delimiters)):
	# SAVE - 		match = re.search(regexes[j], string_list[i]) #find delim
	# SAVE - 		if match:
	# SAVE - 			nodetype = types[j]
	# SAVE - 			delim = delimiters[j]
	# SAVE - 			break
	for string in string_list:
		old_nodes.append(TextNode(string, TextType.TEXT))

	return old_nodes
