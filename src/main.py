import shutil
import os
from textnode import *
from copy_files_recursive import *
from generate_pages_recursive import *

def main():
    
    source_dir = './static'
    dest_dir = './public'
    content_dir = './content'
    template = 'template.html'
    
    print(f"deleting contents of {dest_dir}...")
    shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    
    print(f"copying files from {source_dir} to {dest_dir}")
    copy_files_recursive(source_dir, dest_dir)

    generate_pages_recursive(content_dir, template, dest_dir)
    

main()