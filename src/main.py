import shutil
import os
from textnode import *
from markdown_to_html_node import *

def main():
    
    source_dir = './static'
    dest_dir = './public'
    
    print(f"deleting contents of {dest_dir}...")
    shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    
    print(f"copying files from {source_dir} to {dest_dir}")
    copy_files_recursive(source_dir, dest_dir)

    generate_page('content/index.md', 'template.html', 'public/index.html')
    """
    #check if both source and dest path exist
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        raise ValueError('either source or dest path does not exist')

    
    #create list of paths to copy later
    dir_tree = build_source_tree(source_dir)
    dir_list = list_files(dir_tree, source_dir)
    

    

    #function to create dir structure at dest_dir, should take dir_tree, remove code below when done    
    create_dest_tree(source_dir, dest_dir)
    
   
    for path in dir_list:
        
        if os.path.isfile(path):
            new_path = dest_dir + path.lstrip(source_dir)
            
            shutil.copy(path, new_path)
            print(f'file:  ./{path}\ncopied to:  ./{new_path}')
        else:
            new_path = dest_dir + path.lstrip(source_dir)
            print(f'directory tree:  ./{path}\ncopied to:  ./{new_path}')
            
       """ 



def copy_files_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for dir_item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, dir_item)
        dest_path = os.path.join(dest_dir, dir_item)
        print(f"* {source_path} --> {dest_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files_recursive(source_path, dest_path)


def extract_title(markdown):
    header = markdown.split('\n', maxsplit=1)

    if header[0][:2] != "# ":
        raise ValueError('no h1 header found')
    return header[0][2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file_obj = open(from_path)
    md_content = file_obj.read()

    file_obj = open(template_path)
    template_content = file_obj.read()

    html_node = markdown_to_html_node(md_content)
    html = html_node.to_html()

    title = extract_title(md_content)

    new_html1 = template_content.replace('{{ Content }}', html)
    new_html2 = new_html1.replace('{{ Title }}', title)


    file_obj = open(dest_path, 'wt')
    file_obj.write(new_html2)






main()

"""
#build dictionary of dir tree starting from start_path(relative to cwd)
def build_source_tree(start_path):
    #base case: path has no files
    #base case 2: path has no subdirs
    tree_dict = {}
    dirlist = os.listdir(start_path)
    if not dirlist:
        return None
        

    #check for dir of all files, no subdirs
    type_list = []
    for item in dirlist:
        type_list.append(os.path.isdir(start_path + '/' + item))

    
    #recursive case
    # if item is a subdir, else do the thing for files above
    for item in dirlist:
        if os.path.isdir(start_path + '/' + item):
            subdir_path = start_path + '/' + item
            subdir_tree = build_source_tree(subdir_path)
            tree_dict[item] = subdir_tree
        else:
            tree_dict[item] = None

    return tree_dict
    
def list_files(current_filetree, current_path="."):
    file_list = []
    for node in current_filetree:
        nested_nodes = current_filetree[node]
        if nested_nodes is None:
            file_list.append(current_path + "/" + node)
        else:
            file_list.extend(list_files(nested_nodes, current_path + "/" + node))
    return file_list

    
def create_dest_tree(source_dir, dest_dir):
    #base case: no subdir, return
    #recursive case: subdir
    for item in os.listdir(source_dir):
        if os.path.isdir(source_dir + '/' + item):
            #print(item)
            os.mkdir(dest_dir + '/' + item)
            new_source = source_dir + '/' + item
            new_dest = dest_dir + '/' + item
            create_dest_tree(new_source, new_dest)
    return
"""