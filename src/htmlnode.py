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

	def __repr__(self):
		print(f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.url})')

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, children=None, props=None):
				
		super().__init__(tag, value, children, props)


	def to_html(self):
		if not self.value:
			raise ValueError
		if not self.tag:
			return self.value
		return f"<{self.tag}>{self.value}</{self.tag}>"