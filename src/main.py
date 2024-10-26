from textnode import *

def main():

    #doc = "hgjhghg `hghghg`\n`hjhggf` dfg dtyfyu\njhgfj `hfjf` gffgfk\njhgfddhg `sestres`"
    nodes = []
    #lines = doc.split('\n')
    #for string in lines:
    #    nodes.append(TextNode(string, TextType.TEXT))

    nodes = create_old_nodes()

    new_nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    new_new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
    new_new_new_nodes = split_nodes_delimiter(new_new_nodes, '**', TextType.BOLD)

    print(new_new_new_nodes)
    
main()