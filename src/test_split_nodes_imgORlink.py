import unittest

from htmlnode import *
from textnode import *
from split_nodes_imgORlink import *


class Test_split_nodes_imgORlink(unittest.TestCase):

	def test_standard(self):
		old_nodes = [
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
			TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg')
			],
			split_nodes_image(old_nodes)
		)


if __name__ == "__main__":
    unittest.main()