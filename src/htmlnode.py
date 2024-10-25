from functools import *

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		# messy reduce with lambda for practice just accumulates all attributes into one string
		if not self.props:
			return ""

		string = reduce(lambda acc, key: acc + f' {key}="{self.props[key]}"', self.props, '')
		return string

	def __eq__(self, other):
		if (
			self.tag == other.tag and
			self.value == other.value and
			self.children == other.children and
			self.props == other.props
			):
			return True
		return False

	def __repr__(self):

		return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, children=None, props=None):
				
		super().__init__(tag, value, children, props)


	def to_html(self):
		if not self.value:
			raise ValueError('no value')
		if not self.tag:
			return self.value
		return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None):
				
		super().__init__(tag, None, children, props)

	def to_html(self):
		
		if not self.tag:
			raise ValueError('no tag')
		if not self.children:
			raise ValueError('no children')
		

		string = ""
		for child in self.children:
			string += child.to_html()

		return f"<{self.tag}>{string}</{self.tag}>"
