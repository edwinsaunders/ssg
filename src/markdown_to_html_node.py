import re
from text_node_to_html_node import *
from text_to_textnodes import *
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
			
			case 'heading':
				regex = r'^#* '
				prefix = re.findall(regex, blocks[i])[0]
				text = blocks[i].split(prefix)[1]
				"""
				text_nodes = text_to_textnodes(text)
				
				children = []				
				for node in text_nodes:
					html_node = text_node_to_html_node(node)
					children.append(html_node)
				"""
				children = text_to_children(text)

				numhash = prefix.count('#')
				html_nodes.append(ParentNode(f"h{numhash}", children))
			
			case 'code':
				code_list = []
				temp_list = blocks[i].split('```')
				if len(temp_list) != 3:	# if syntax correct, temp_list will be ["", text, ""]
					raise ValueError("Invalid code block syntax")
				text = temp_list[1] #(second item in list is the text)
				
				children = text_to_children(text)

				code_node = [ParentNode("code", children)]
				#code_list.append(node)
				#leaf_nodes.append(node)
				html_nodes.append(ParentNode('pre', code_node))
			
			case 'quote':
				#remove '>' from each line
				list_items = blocks[i].split('\n')
				#print(list_items)
				new_list = []
				for item in list_items:
					if not item.startswith('> '):
						raise ValueError("Invalid quote block")

					new_list.append(item[2:]) # slice off the '> '
				#print(new_list)
				#print('\n'.join(new_list))
				text = ' '.join(new_list)

				children = text_to_children(text)

				html_nodes.append(ParentNode("blockquote", children))
			
			case 'ordered_list':
				#remove number, '.', and space
				ol_list = []
				regex = r'^(\d*)\. '
				#print(blocks[i])
				list_items = blocks[i].split('\n')
				for item in list_items:
					denum = re.split(regex, item)
					text = denum[2] # we want the third item in the list (the text, first is "", second is te captured regex)
					
					children = text_to_children(text)

					#node = LeafNode("li", text)
					ol_list.append(ParentNode('li', children))
					#leaf_nodes.append(node)
				html_nodes.append(ParentNode('ol', ol_list))
			
			case 'unordered_list':
				#remove number, '*' or '-', and space
				ul_list = []
				regex = r'^(\d*)\. '
				#print(blocks[i])
				list_items = blocks[i].split('\n')
				for item in list_items:
					debul = item[2:] # string without bullet and space
					text = debul
					children = text_to_children(text)
					#node = LeafNode(f"li", text)
					ul_list.append(ParentNode('li', children))
					#leaf_nodes.append(node)
				html_nodes.append(ParentNode('ul', ul_list))
			
			case 'paragraph':
				list_items = blocks[i].split('\n')
				text = " ".join(list_items)
				children = text_to_children(text)
				#node = LeafNode('p', text)
				html_nodes.append(ParentNode('p', children))
			
			case _:
				raise ValueError("Invalid block type")

	div_node = ParentNode('div', html_nodes)

	#print(blocks)
	#print(block_types)
	#print(div_node)
	return div_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children