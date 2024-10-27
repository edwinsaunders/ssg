import re
from textnode import *
from extract_images_links import *


def split_nodes_image(old_nodes):

	new_nodes = []
	
	#loops through input textnode list(all of type "text"), create a new list of one or more textnodes, extend new_nodes with node list for current old node
	for node in old_nodes:
		if node.text_type != TextType.TEXT.value:
			new_nodes.append(node)
			continue

		#list of nodes for current old node
		split_nodes = []

		#tuples of alt_text and img src
		imagenode_tups = extract_markdown_images(node.text)

		#list of strings
		#regex with no capture groups so it is strictly used as delimiter
		sections = re.split(r"!\[[^\[\]]*\]\([^\(\)]*\)", node.text)
		img_start = True if sections[0] == "" else False

		#get rid of empty strings
		sections = list(filter(lambda x: x != "", sections))

		#take list of strings, and tuples, and append/extend new nodes with nodes created with each alternating
		# if sections starts wih "", first node in split_nodes should be image type
		#if len(sections) % 2 == 0:
		#    raise ValueError("Invalid markdown, formatted section not closed")
		if img_start == 0:
			for i in range(0, len(sections) + len(imagenode_tups)):
				if i < len(sections):
					split_nodes.append(TextNode(sections[i], TextType.TEXT))
				if i < len(imagenode_tups):
					split_nodes.append(TextNode(imagenode_tups[i][0], TextType.IMAGE, imagenode_tups[i][1]))
		else:
			for i in range(0, len(sections) + len(imagenode_tups)):
				if i < len(imagenode_tups):
					split_nodes.append(TextNode(imagenode_tups[i][0], TextType.IMAGE, imagenode_tups[i][1]))
				if i < len(sections):
					split_nodes.append(TextNode(sections[i], TextType.TEXT))

		new_nodes.extend(split_nodes)
	return new_nodes


def split_nodes_link(old_nodes):
	pass