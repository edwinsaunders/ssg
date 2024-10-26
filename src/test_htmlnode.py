import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):

    #base class tests
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

    
    #LeafNode tests
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


    #ParentNode tests
    def test_to_html_oneChild(self):
        child = LeafNode(
            "b", "this is a\nparagraph\n", 
            None, 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        node = ParentNode(
            "p", 
            [child], 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        test_string = '<p><b>this is a\nparagraph\n</b></p>'
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_nestedParents(self):
        leaf = LeafNode(
            "b", "this is a\nparagraph\n", 
            None, 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        parent1 = ParentNode(
            "p", 
            [leaf], 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        node = ParentNode(
            "h", 
            [parent1], 
            {
            'href': 'http://www.x.com', 
            'blah': 'poopoo', 'third': 'i dunno'
            }
            )
        test_string = '<h><p><b>this is a\nparagraph\n</b></p></h>'
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_complex(self):

        lnodeB2 = LeafNode("d", "blah", None, None)

        lnodeB1 = LeafNode("c", "blahblah", None, None)

        pnodeB  = ParentNode("a", [lnodeB1, lnodeB2], None)

        lnodeA1 = LeafNode("b", "this is a\nparagraph\n", None, None)

        pnodeA = ParentNode("p", [lnodeA1], None)
            
        masternode = ParentNode("h", [pnodeA, pnodeB], None)

        test_string = '<h><p><b>this is a\nparagraph\n</b></p><a><c>blahblah</c><d>blah</d></a></h>'

        self.assertEqual(masternode.to_html(), test_string)

    def test_to_html_noChildren(self):
        node = ParentNode("p", None, None)
        
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_Tag(self):
        node2 = LeafNode("d", "blah", None, None)
        node = ParentNode(None, [node2], None)
        
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()