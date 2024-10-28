import unittest
from textnode import *
from text_to_textnodes import *


class Test_text_to_textnodes(unittest.TestCase):
	def test_standard(self):
		input_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

		self.assertEqual(
			[
			TextNode('This is ', TextType.TEXT, None),
			TextNode('text', TextType.BOLD, None),
			TextNode(' with an ', TextType.TEXT, None),
			TextNode('italic', TextType.ITALIC, None),
			TextNode(' word and a ', TextType.TEXT, None),
			TextNode('code block', TextType.CODE, None),
			TextNode(' and an ', TextType.TEXT, None),
			TextNode('obi wan image', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
			TextNode(' and a ', TextType.TEXT, None),
			TextNode('link', TextType.LINK, 'https://boot.dev')
			],
			text_to_textnodes(input_text)
		)






if __name__ == "__main__":
    unittest.main()