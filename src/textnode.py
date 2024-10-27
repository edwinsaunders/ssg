from enum import Enum
from htmlnode import *

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
		self.text_type = text_type.value
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