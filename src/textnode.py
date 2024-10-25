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