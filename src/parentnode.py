from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        """Parse Parent Node to HTML recursively iterating over its children"""
        
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        res = []
        for child in self.children:
            res.append(child.to_html())
        return f"<{self.tag}{" " + self.props_to_html() if self.props else ""}>{"".join(res)}</{self.tag}>"