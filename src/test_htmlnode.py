import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_to_html_typical(self):
        node = LeafNode(
            "p", "this is a\nparagraph\n", 
            None, 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        test_string = '<p>this is a\nparagraph\n</p>'
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_noValue(self):
        node = LeafNode(
            "p", "", 
            None, 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_noTag(self):
        node = LeafNode(
            "", "this is a\nparagraph\n", 
            None, 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        
        test_string = 'this is a\nparagraph\n'
        self.assertEqual(node.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()