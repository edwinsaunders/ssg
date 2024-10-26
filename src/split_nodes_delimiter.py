import re
from textnode import *

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