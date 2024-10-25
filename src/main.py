from textnode import *

def main():

    #node = TextNode("dummy text", TextType.BOLD, "http://www.zombo.com")
    #print(node)
    #textnode_t = TextNode("text", TextType.TEXT, None)
    #textnode_b = TextNode("bold text", TextType.BOLD, None)
    #textnode_it = TextNode("italic text", TextType.ITALIC, None)
    #textnode_c = TextNode("def codetext(): return", TextType.CODE, None)
    #textnode_l = TextNode("link text", TextType.LINK, "http://www.test.com")
    #textnode_im = TextNode("img alt text", TextType.IMAGE, "http://www.imgsrc.com")

    doc = "hgjhghg `hghghg`\n`hjhggf` dfg dtyfyu\njhgfj `hfjf` gffgfk\njhgfddhg `sestres`"
    nodes = []
    lines = doc.split('\n')
    for string in lines:
        nodes.append(TextNode(string, TextType.TEXT))

    print(nodes)

    new_nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)

    print(new_nodes)

main()