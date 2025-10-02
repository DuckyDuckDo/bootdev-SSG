
def markdown_to_blocks(markdown_text):
    """
    Convert markdown text down into blocks
    """
    blocks = markdown_text.split("\n\n")
    result = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        result.append(block)

    return result