import re
from markdown_to_blocks import *
from block_to_block_type import *
from htmlnode import *

#takes markdown doc as a string and returns nested html node representation
def markdown_to_html_node(markdown):
	
	# using file for testing, function should take a string called 'markdown' as input
	#with open(filename, 'r') as file:
	#	markdown = file.read()

	blocks = markdown_to_blocks(markdown)

	block_types = []
	html_nodes = []
	#parent_nodes = []

	for i in range(0, len(blocks)):
		block_types.append(block_to_block_type(blocks[i]))

		#make html nodes
		match block_types[i]:
			case BlockType.HEADING:
				regex = r'^#* '
				prefix = re.findall(regex, blocks[i])[0]
				text = blocks[i].split(prefix)[1]
				numhash = prefix.count('#')
				html_nodes.append(LeafNode(f"h{numhash}", text))
			case BlockType.CODE:
				code_list = []
				text = blocks[i].split('```')[1] #(second item in list is the text)
				node = LeafNode("code", text)
				code_list.append(node)
				#leaf_nodes.append(node)
				html_nodes.append(ParentNode('pre', code_list))
			case BlockType.QUOTE:
				#remove '>' from each line
				list_items = blocks[i].split('\n')
				#print(list_items)
				new_list = []
				for item in list_items:
					new_list.append(item[1:]) # slice off the '>'
				#print(new_list)
				#print('\n'.join(new_list))
				text = ' '.join(new_list)
				html_nodes.append(LeafNode("blockquote", text))
			case BlockType.ORDERED_LIST:
				#remove number, '.', and space
				ol_list = []
				regex = r'^(\d*)\. '
				#print(blocks[i])
				list_items = blocks[i].split('\n')
				for item in list_items:
					denum = re.split(regex, item)
					text = denum[2] # we want the third item in the list (the text, first is "", second is te captured regex)
					node = LeafNode("li", text)
					ol_list.append(node)
					#leaf_nodes.append(node)
				html_nodes.append(ParentNode('ol', ol_list))
			case BlockType.UNORDERED_LIST:
				#remove number, '*' or '-', and space
				ul_list = []
				regex = r'^(\d*)\. '
				#print(blocks[i])
				list_items = blocks[i].split('\n')
				for item in list_items:
					debul = item[2:] # string without bullet and space
					text = debul 
					node = LeafNode(f"li", text)
					ul_list.append(node)
					#leaf_nodes.append(node)
				html_nodes.append(ParentNode('ul', ul_list))
			case BlockType.PARAGRAPH:
				list_items = blocks[i].split('\n')
				text = " ".join(list_items)
				node = LeafNode('p', text)
				html_nodes.append(node)
			case _:
				pass

	div_node = ParentNode('div', html_nodes)

	#print(blocks)
	#print(block_types)
	return div_node
