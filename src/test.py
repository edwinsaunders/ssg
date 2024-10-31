def main():
	dict = {
		"Documents": {
			"Proposal.docx": None,
			"Receipts": {
				"January": {
					"receipt1.txt": None,
					"receipt2.txt": None
				},
				"February": None
					}
				},
			}

	print(list_files(dict))

def list_files(current_filetree, current_path=""):
    file_list = []
    for node in current_filetree:
        nested_nodes = current_filetree[node]
        if nested_nodes is None:
            file_list.append(current_path + "/" + node)
        else:
            file_list.extend(list_files(nested_nodes, current_path + "/" + node))
    return file_list

main()