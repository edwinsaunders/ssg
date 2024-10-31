import unittest
from markdown_to_html_node import *

class Test_markdown_to_html_node(unittest.TestCase):
	def test(self):
		markdown = """1. sdfsga
2. sdfgasdf
3. sdfgsdgbnbv

* sdfghsdfg
* fvcnxsdsd
* ydghm6ue6

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

###### fghdfhfd

####### dfgsdf"""
		#print(type(markdown))
		control = ParentNode(
			'div', [ParentNode(
				'ol', [LeafNode(
					'li', 'sdfsga', None), LeafNode(
					'li', 'sdfgasdf', None), LeafNode(
					'li', 'sdfgsdgbnbv', None)], None
					),
			ParentNode(
				'ul', [LeafNode(
					'li', 'sdfghsdfg', None), LeafNode(
					'li', 'fvcnxsdsd', None), LeafNode(
					'li', 'ydghm6ue6', None)], None
					),
			ParentNode(
				'ul', [LeafNode(
					'li', 'cvxbcv', None), LeafNode(
					'li', 'dfgdfg', None)], None
					),
			ParentNode(
				'pre', [LeafNode(
					'code', '\nfgbxfxcvbxcvb\ndsfgdfg\ndfgdf\n', None)], None
				),
			LeafNode(
				'blockquote', 'dfgdfgdfsd dfhgdfgdwetert', None),
			LeafNode(
				'h1', 'gfdddfg', None),
			LeafNode(
				'h2', 'dfgdfgds', None),
			LeafNode(
				'h3', 'dfgdf', None),
			LeafNode(
				'h6', 'fghdfhfd', None),
			LeafNode(
				'p', '####### dfgsdf', None)], None
			)
		#print(type(control))
		#print(type(markdown_to_html_node(markdown)))
		self.assertEqual(markdown_to_html_node(markdown), control)