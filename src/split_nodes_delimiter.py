from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Takes a list of old nodes, a delimiter, and its corresponding text_type
    Splits the old_nodes into new nodes
    "This is **bold text**"
    Splits to 
    TextNode(This is, TextType.TEXT)
    TextNode(bold text, TextType.BOLD)
    """
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid markdown there should only be odd numbers of sections")
            split_nodes = []
            for i, section in enumerate(split_text):
                if section:
                    if i % 2 == 0:
                        split_nodes.append(TextNode(section, TextType.TEXT))
                    else:
                        split_nodes.append(TextNode(section, text_type))
            result.extend(split_nodes)
    return result

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    """
    Split inline nodes containing an image, see comments in split_nodes_links, functions are extremely similar
    """
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        curr_text = old_node.text
        images = extract_markdown_images(old_node.text)
        if not images:
            result.append(old_node)
            continue

        for image in images:
            sections = curr_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, no images found")
            
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(image[0], TextType.IMAGE, image[1]))
            curr_text = sections[1]

        if curr_text != "":
            result.append(TextNode(curr_text, TextType.TEXT))

    return result

def split_nodes_link(old_nodes):
    """
    Splits inline nodes containing a link
    """
    result = []

    # Loops through the input nodes
    for old_node in old_nodes:
        # If node is not a text type, cannot really be split (this is case of this project, avoiding nested splits)
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        
        # Need to keep track of current text
        curr_text = old_node.text

        # Grab any links that exist
        links = extract_markdown_links(old_node.text)

        # If no links exist, we are good with the node, just append to result
        if not links:
            result.append(old_node)
            continue
        
        # Loop through the links and perform the node splits
        for link in links:
            sections = curr_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link not found")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(link[0], TextType.LINK, link[1]))
            curr_text = sections[1]
        
        # Append the ending text after all links if it exists
        if curr_text != "":
            result.append(TextNode(curr_text, TextType.TEXT))

    return result

def text_to_textnodes(text):
    """
    Converts text into text nodes by utilizing all of the splitting functions once and updating the result.
    Result starts with a singular text node of the given input text. 
    """
    delimiter_map = {
        TextType.CODE: '`',
        TextType.ITALIC: '_',
        TextType.BOLD: '**'
    }
    
    result = [TextNode(text, TextType.TEXT)]
    for text_type in delimiter_map:
        result = split_nodes_delimiter(result, delimiter_map[text_type], text_type)
    
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result