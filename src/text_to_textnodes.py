from textnode import *
from split_nodes_delimiter import *
from split_nodes_imgORlink import *

def text_to_textnodes(text):
	new_nodes = []
	start_node = [TextNode(text, TextType.TEXT)]

	bold_nodesplit = split_nodes_delimiter(start_node, '**', TextType.BOLD)
	italic_nodesplit = split_nodes_delimiter(bold_nodesplit, '*', TextType.ITALIC)
	code_nodesplit = split_nodes_delimiter(italic_nodesplit, '`', TextType.CODE)
	image_nodesplit = split_nodes_image(code_nodesplit)
	link_nodesplit = split_nodes_link(image_nodesplit)

	new_nodes = link_nodesplit

	return new_nodes
