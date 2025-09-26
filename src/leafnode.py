from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        """Wraps tag and values to create HTML text"""
        if not self.value:
            raise ValueError("Leaf nodes must have value")
        
        if not self.tag:
            return self.value

        return f"<{self.tag}{" " + self.props_to_html() if self.props else ""}>{self.value}</{self.tag}>"

