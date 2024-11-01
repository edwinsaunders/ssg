import os
from generate_page import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	if not os.path.exists(dest_dir_path):
		os.mkdir(dest_dir_path)

	for dir_item in os.listdir(dir_path_content):
		source_path = os.path.join(dir_path_content, dir_item)
		dest_path = os.path.join(dest_dir_path, dir_item)
		if os.path.isfile(source_path):
			print(source_path, dest_path, os.path.isfile(source_path))

			file_parts = dir_item.split('.')

			new_file_path = os.path.join(dest_dir_path, file_parts[0] + '.html')
			generate_page(source_path, template_path, new_file_path)
		else:
			print(source_path, dest_path)
			generate_pages_recursive(source_path, template_path, dest_path)
