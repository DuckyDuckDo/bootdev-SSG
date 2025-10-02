from textnode import *

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

