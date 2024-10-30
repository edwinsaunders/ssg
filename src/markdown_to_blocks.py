def markdown_to_blocks(markdown):

	#with open(filename, 'r') as file:
	#	content = file.read()

	block_split = markdown.split('\n\n')
	
	block_split_stripped = []
	
	for string in block_split:
		block_split_stripped.append(string.strip())

	block_split_stripped = list(filter(lambda x: x != "", block_split_stripped))

	return block_split_stripped


"""
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

"""