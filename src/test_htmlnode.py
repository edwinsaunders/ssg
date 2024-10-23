import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_generic(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        node3 = HTMLNode()
        node = HTMLNode("p", "this is a\nparagraph\n", [node1, node2, node3], {'href': 'http://www.x.com', 'blah': 'poopoo', 'third': 'i dunno'})
        string = ' href="http://www.x.com" blah="poopoo" third="i dunno"'
        self.assertEqual(node.props_to_html(), string)

    def test_props_to_html_emptynode(self):

        node = HTMLNode()
        string = ""
        self.assertEqual(node.props_to_html(), string)

    def test_props_to_html_emptyprops(self):
        
        node = HTMLNode(None, None, None, {})
        string = ""
        self.assertEqual(node.props_to_html(), string)

    def test_props_to_html_allnone(self):
        
        node = HTMLNode(None, None, None, None)
        string = ""
        self.assertEqual(node.props_to_html(), string)
    


if __name__ == "__main__":
    unittest.main()