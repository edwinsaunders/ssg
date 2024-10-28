import unittest
from textnode import *
from split_nodes_imgORlink import *


class Test_split_nodes_imgORlink(unittest.TestCase):

	def test_standard_image(self):
		old_nodes = [
		TextNode(
			"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
			TextType.TEXT
			),
		TextNode(
			"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
			TextType.TEXT
			)
		]
		self.assertListEqual(
			[
			TextNode('This is text with a ', TextType.TEXT, None),
			TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
			TextNode(' and ', TextType.TEXT, None),
			TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
			TextNode('This is text with a ', TextType.TEXT, None),
			TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
			TextNode(' and ', TextType.TEXT, None),
			TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg')
			],
			split_nodes_image(old_nodes)
		)

	def test_standard_link(self):
		old_nodes = [
		TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
			TextType.TEXT
			),
		TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
			TextType.TEXT
			)
		]
		self.assertListEqual(
			[
			TextNode('This is text with a link ', TextType.TEXT, None),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
			TextNode(' and ', TextType.TEXT, None),
			TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'),
			TextNode('This is text with a link ', TextType.TEXT, None),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
			TextNode(' and ', TextType.TEXT, None),
			TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
			],
			split_nodes_link(old_nodes)
		)

if __name__ == "__main__":
    unittest.main()