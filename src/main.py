from textnode import TextNode, TextType
import os
import shutil
from htmlnode import *
from md_to_html import *

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("#"):
            return line.split("#")[1].strip()
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as md_file:
        md_text = md_file.read()
        title = extract_title(md_text)

    
    with open(template_path, "r") as template_file:
        template_text = template_file.read()
    
    md_html_node = markdown_to_html_node(md_text)
    md_html = md_html_node.to_html()
    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", md_html)

    with open(dest_path, "w") as final_html:
        final_html.write(template_text)



dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


if __name__ == "__main__":
    main()
