from markdown_to_html_node import *
from extract_title import *
from htmlnode import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file_obj = open(from_path)
    md_content = file_obj.read()
    file_obj.close()

    file_obj = open(template_path)
    template_content = file_obj.read()
    file_obj.close()

    html_node = markdown_to_html_node(md_content)
    html = html_node.to_html()

    title = extract_title(md_content)

    new_html1 = template_content.replace('{{ Content }}', html)
    new_html2 = new_html1.replace('{{ Title }}', title)


    file_obj = open(dest_path, 'w')
    file_obj.write(new_html2)
    file_obj.close()