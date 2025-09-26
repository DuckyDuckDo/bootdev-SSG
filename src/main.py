from textnode import TextNode, TextType
def main():
    dummy_textnode = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    print(dummy_textnode)


if __name__ == "__main__":
    main()
