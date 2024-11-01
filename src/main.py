import shutil
import os
from textnode import *
from copy_files_recursive import *
from generate_page import *

def main():
    
    source_dir = './static'
    dest_dir = './public'
    
    print(f"deleting contents of {dest_dir}...")
    shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    
    print(f"copying files from {source_dir} to {dest_dir}")
    copy_files_recursive(source_dir, dest_dir)

    generate_page('content/index.md', 'template.html', 'public/index.html')
    

main()