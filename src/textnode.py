from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    TEXT = "text"
    LINK = "link"


class TextNode():
    def __init__(self,  text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node):
        return self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node): 
    if not isinstance(text_node, TextNode):
        raise ValueError("Please Pass in a TextNode Object")
    if not isinstance(text_node.text_type, TextType):
        return ValueError("Invalid Text Type")
    
    # Maps text type to its corresponding tag
    tag_map = {
        "text": None,
        "bold": "b",
        "italic": "i",
        "code": "code",
        "image": "img",
        "link": "a"
    }

    # Handle specific cases for images and links
    if text_node.text_type.value == "image":
        return LeafNode(tag = tag_map["image"], value = "", props = {"src": text_node.url, "alt": text_node.text})
    
    if text_node.text_type.value == "link":
        return LeafNode(tag = tag_map["link"], value = text_node.text, props = {"href": text_node.url})
    
    return LeafNode(tag = tag_map[text_node.text_type.value], value = text_node.text)