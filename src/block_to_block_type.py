import re
from enum import Enum

class BlockType(Enum):
		PARAGRAPH = 'paragraph'
		HEADING = 'heading'
		CODE = 'code'
		QUOTE = 'quote'
		UNORDERED_LIST = 'unordered_list'
		ORDERED_LIST = 'ordered_list'


def block_to_block_type(block):

	


	#Heading logic:
	#if first chars are '#' + space', break, not a heading
	#Line must start with 1-6 #'s + space
	#coutn number of consecutive #'s, if less than eq 6 or greater than eq 1,
		# return or print BlockType.HEADING
	#if no space after final #, break, not a heading
	
	#test block to be removed later
	#block = '- sdfghsdfg\n- fvcnxsdsd\n- ydghm6ue6'

	#find heading
	regex = r'^#* '
	if re.findall(regex, block):
		prefix = re.findall(regex, block)[0]
		numhash = prefix.count('#')
		if numhash <= 6:
			#print(BlockType.HEADING)
			return 'heading'

	#find code
	regex1 = r'^```'
	regex2 = r'```$'
	if re.findall(regex1, block) and re.findall(regex2, block):
		#print(BlockType.CODE)
		return 'code'
	

	#Quote logic:
	#If first char on every line is '>', return or print BlockType.QUOTE
	isQuote = True
	block_lines = block.split('\n')
	for line in block_lines:
		if line[0] != '>':
			isQuote = False
			#return
	if isQuote == True:
		#print(BlockType.QUOTE)
		return "quote"



	#unordered logic:
	#if first char on every line is '* ' or '- ' (note space), all lines must use same char, not mixed,
		# return or print BlockType.UNORDERED_LIST
	isUnord = True
	#block_lines = block.split('\n')
	chosen_bul = block_lines[0][:2]
	for line in block_lines:		
		if chosen_bul == '* ' :
			if line[:2] != '* ':
				isUnord = False
				#print('\n' + line[:2], isUnord)
				break
		elif chosen_bul == '- ':
			if line[:2] != '- ':
				isUnord = False
				#print('\n' + line[:2])
				break
		else:
			isUnord = False
	#print(block)
	#print(isUnord)
	if isUnord == True:
		#print(BlockType.UNORDERED_LIST)
		return "unordered_list"




	# for ordred lists: 
	# make sure each line starts with a number a '.', and a space
	
	# block = "1. dsfgd2 sdfsa\n2. asdf5 sdfg\n3. asdfa"
	# split multiline blocks into list of lines
	block_lines = block.split('\n')

	i = 0 # line counter
	isOrderedList = True
	for line in block_lines:
		i += 1 # current list item number(index + 1)
		# if line n doesn't start with a '<n>. ', break
			#2 steps:  check for num + '.' + space, then check that num equals line num
		#linenum = int(re.findall(r'^(\d*)\. ', line)[0]) # get number from beginning of string(always list item index 0)
		
		
		#print(re.findall(r'^(\d*)\. ', line))

		# if empty list , break no number at begiining of line, not ordered list
		if not re.findall(r'^(\d*)\. ', line):
			isOrderedList = False
			break

		linenum = int(re.findall(r'^(\d*)\. ', line)[0])
		
		#print(linenum)
		#print(i)
		
		# if line num chars at beginning of string not equal to current loop
			# iteration number (i), break, not ordered list
		if linenum != i:
			isOrderedList = False
			break
	if isOrderedList == True:
		#print(BlockType.ORDERED_LIST)
		return 'ordered_list'
	else:
		#print(BlockType.PARAGRAPH)
		return "paragraph"


#block_to_block_type()