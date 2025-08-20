from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        #print(f"Node: {node}")
        
        markdown = extract_markdown_images(node.text)
        if markdown:
            #print(f"Markdown: {markdown}")
            original_text = node.text
            for each in markdown:
                image_alt = each[0]
                image_link = each[1]
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                if sections:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = sections[1]
                #print(f"Sections: {sections}")
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
        else:
            new_nodes.append(node)

    #print(f"New Nodes: {new_nodes}")
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        markdown = extract_markdown_links(node.text)
        if markdown:
            original_text = node.text
            #print(f"Markdown: {markdown}")
            for each in markdown:
                link_text = each[0]
                link_url = each[1]
                sections = original_text.split(f"[{link_text}]({link_url})", 1)
                #print(f"Sections: {sections}")
                if sections:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes