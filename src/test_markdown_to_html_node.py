import unittest
from markdown_to_html_node import *

class Test_markdown_to_html_node(unittest.TestCase):
	def test(self):
		markdown = """1. sdfsga
2. sdf**ga**sdf
3. sdfgsdgbnbv

* sdf`ghs`dfg
* fvcnxsdsd
* yd*gh*m6ue6

- cvxbcv
- dfgdfg


```
fgbxfxcvbxcvb
dsfgdfg
dfgdf
```

>dfgdfgdfsd
>dfhgdfgdwetert

# gfdddfg

## dfgdfgds

### dfgdf

###### fgh**dfh**fd

####### **dfgsdf**"""
		#print(type(markdown))
		control = ParentNode('div', [ParentNode('ol', [ParentNode('li', [LeafNode(None, 'sdfsga', None)], None)
, ParentNode('li', [LeafNode(None, 'sdf', None), LeafNode('b', 'ga', None), LeafNode(None, 'sdf', None)], None)
, ParentNode('li', [LeafNode(None, 'sdfgsdgbnbv', None)], None)
], None)
, ParentNode('ul', [ParentNode('li', [LeafNode(None, 'sdf', None), LeafNode('code', 'ghs', None), LeafNode(None, 'dfg', None)], None)
, ParentNode('li', [LeafNode(None, 'fvcnxsdsd', None)], None)
, ParentNode('li', [LeafNode(None, 'yd', None), LeafNode('i', 'gh', None), LeafNode(None, 'm6ue6', None)], None)
], None)
, ParentNode('ul', [ParentNode('li', [LeafNode(None, 'cvxbcv', None)], None)
, ParentNode('li', [LeafNode(None, 'dfgdfg', None)], None)
], None)
, ParentNode('pre', ParentNode('code', [LeafNode(None, '\nfgbxfxcvbxcvb\ndsfgdfg\ndfgdf\n', None)], None)
, None)
, ParentNode('blockquote', [LeafNode(None, 'dfgdfgdfsd dfhgdfgdwetert', None)], None)
, ParentNode('h1', [LeafNode(None, 'gfdddfg', None)], None)
, ParentNode('h2', [LeafNode(None, 'dfgdfgds', None)], None)
, ParentNode('h3', [LeafNode(None, 'dfgdf', None)], None)
, ParentNode('h6', [LeafNode(None, 'fgh', None), LeafNode('b', 'dfh', None), LeafNode(None, 'fd', None)], None)
, ParentNode('p', [LeafNode(None, '####### ', None), LeafNode('b', 'dfgsdf', None)], None)
], None)
		#print(type(control))
		#print(type(markdown_to_html_node(markdown)))
		self.assertEqual(markdown_to_html_node(markdown), control)