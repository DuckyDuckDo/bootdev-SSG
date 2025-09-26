
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        """Prepares a props string to add to opening tag of HTML elements"""
        res = []
        for tag, value in self.props.items():
            res.append(f'{tag}=\"{value}\"')
        return " ".join(res) 
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"