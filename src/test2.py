import os

def main():
    start_path = 'public'
    print(build_tree(start_path))

def build_tree(start_path):
    #base case: path has no files
    #base case 2: path has no subdirs
    tree_dict = {}
    dirlist = os.listdir(start_path)
    if not dirlist:
        return None
        #tree_dict[start_path] = None
        #return tree_dict

    #check for dir of all files, no subdirs
    type_list = []
    for item in dirlist:
        type_list.append(os.path.isdir(start_path + '/' + item))
    print(type_list)
    #if no subdirs
    if True not in type_list:
        for item in dirlist:        
            tree_dict[item] = None
            return tree_dict

    #recursive case
    # if item is a subdir, else do the thing for files above
    for item in dirlist:
        if os.path.isdir(start_path + '/' + item):
            subdir_path = start_path + '/' + item
            subdir_tree = build_tree(subdir_path)
            tree_dict[item] = subdir_tree
        else:
            tree_dict[item] = None


    return tree_dict

main()

