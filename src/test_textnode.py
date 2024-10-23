import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This too is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.zombo.com")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This three is a text node", TextType.BOLD, "http://www.github.com")
        node2 = TextNode("This three is a text node", TextType.BOLD, "http://www.github.com")
        self.assertEqual(node, node2)

    def test_one_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.github.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()