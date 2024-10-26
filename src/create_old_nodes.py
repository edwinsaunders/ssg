import re
from textnode import *

#function to partially parse document string into list of TextNode objects, all of type TextNode.TEXT
	#to feed into split_nodes_delimiter function
def create_old_nodes(string):
	old_nodes = []

	
	#Using these two tuples in parallel to find/ delimiters.  delim and corrsponding
		#regex need to have same index
	delimiters = ('*', '**', '`')
	regexes = (r'(?<!\*)\*(?!\*)', r'\*\*', r'`')
	
	current_delim = ""
	current_delim_pos = -1

	remaining_string = string
	
	string_list = []
	
	# while there are still delimiters in the remaining string
	# loop to breakdown string into list of strings every time a delim is encountered that is not the current delim
	while(current_delim_pos != float('inf') and remaining_string != ''):
		
		current_delim_pos = float('inf')
		#find first delim type in remaining_string
		for i in range(0, len(delimiters)):

			#find regex that corresponds to delim
			match = re.search(regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the delim
					current_delim = delimiters[i]
					current_regex = regexes[i]
			else:
				#if current delim type being searched for is not found, skip iteration to look for next delim type
				continue

		
		#if no delims found, put entire remaining string into string list break out of loop
		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			break
		

		# create new delim tuple and regex tuple without current_delim an delim regex
			#in order to use same process as above to find next delim type
			#creates tuples with the remaining delim types that have not been encountered yet
		delim_index = delimiters.index(current_delim)
		new_delims = delimiters[:delim_index] + delimiters[delim_index + 1:]
		regex_index = regexes.index(current_regex)
		new_regexes = regexes[:regex_index] + regexes[regex_index + 1:]
		
		
		
		#reset current_delim_pos to inf for comparison later if no delims found searching for next delim type
		current_delim_pos = float('inf')


		#find next delim type in doc string using same process for finding the first one above
		for i in range(0, len(new_delims)):


			match = re.search(new_regexes[i], remaining_string) #find delim
			if match and match.start() < current_delim_pos:
					current_delim_pos = match.start()  # gets the starting position of the next delim type
					current_delim = new_delims[i]
					current_regex = new_regexes[i]
			else:
				#skip iteration if curent delim type not found
				continue

		
		#if no other delims found, put entire remaining string into string list break out of loop
		if current_delim_pos == float('inf'):
			string_list.append(remaining_string)
			break
				

		#split off one chunk on current_delim, append to list of strings to iterate through later
		chunk = remaining_string[:current_delim_pos]
		string_list.append(chunk)

		#set remaining string to eveything except the chunk that was split off from the beginning
		remaining_string = remaining_string[current_delim_pos:]
		

		#repeat for remainder of string while current_delim_pos != -1

	# this code may prove useful for something later
	# SAVE - types = (TextType.ITALIC, TextType.BOLD, TextType.CODE)
	# SAVE - for i in range(0, len(string_list)):
	# SAVE - 	for j in range(0, len(delimiters)):
	# SAVE - 		match = re.search(regexes[j], string_list[i]) #find delim
	# SAVE - 		if match:
	# SAVE - 			nodetype = types[j]
	# SAVE - 			delim = delimiters[j]
	# SAVE - 			break
	for string in string_list:
		old_nodes.append(TextNode(string, TextType.TEXT))

	return old_nodes