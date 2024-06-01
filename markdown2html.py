#!/usr/bin/python3
"""
markdown2html.py: Convert a Markdown file to an HTML file.
"""

import sys
import os
import re

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)
    
    # Read the content of the Markdown file
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()
    
    # Convert the Markdown content to HTML
    html_content = convert_markdown_to_html(markdown_content)
    
    # Write the HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    # Exit successfully
    exit(0)

def convert_markdown_to_html(markdown_text):
    html_lines = []
    in_paragraph = False
    in_ul_list = False
    in_ol_list = False

    lines = markdown_text.splitlines()
    for line in lines:
        if line.startswith('#'):
            if in_paragraph:
                html_lines.append("</p>")
                in_paragraph = False
            level = len(line.split(' ')[0])
            content = line[level + 1:].strip()
            content = parse_inline_markdown(content)
            html_lines.append(f"<h{level}>{content}</h{level}>")
        elif line.startswith('- '):
            if in_paragraph:
                html_lines.append("</p>")
                in_paragraph = False
            if in_ol_list:
                html_lines.append("</ol>")
                in_ol_list = False
            if not in_ul_list:
                html_lines.append("<ul>")
                in_ul_list = True
            content = line[2:].strip()
            content = parse_inline_markdown(content)
            html_lines.append(f"<li>{content}</li>")
        elif line.startswith('* '):
            if in_paragraph:
                html_lines.append("</p>")
                in_paragraph = False
            if in_ul_list:
                html_lines.append("</ul>")
                in_ul_list = False
            if not in_ol_list:
                html_lines.append("<ol>")
                in_ol_list = True
            content = line[2:].strip()
            content = parse_inline_markdown(content)
            html_lines.append(f"<li>{content}</li>")
        else:
            if in_ul_list:
                html_lines.append("</ul>")
                in_ul_list = False
            if in_ol_list:
                html_lines.append("</ol>")
                in_ol_list = False
            if line.strip() == "":
                if in_paragraph:
                    html_lines.append("</p>")
                    in_paragraph = False
            else:
                if not in_paragraph:
                    html_lines.append("<p>")
                    in_paragraph = True
                content = parse_inline_markdown(line.strip())
                html_lines.append(content)

    if in_ul_list:
        html_lines.append("</ul>")
    if in_ol_list:
        html_lines.append("</ol>")
    if in_paragraph:
        html_lines.append("</p>")

    return '\n'.join(html_lines)

def parse_inline_markdown(text):
    # Replace **bold** with <b>bold</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Replace __emphasis__ with <em>emphasis</em>
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    # Replace [[highlight]] with <mark>highlight</mark>
    text = re.sub(r'\[\[(.*?)\]\]', r'<mark>\1</mark>', text)
    # Replace ((insert)) with <ins>insert</ins>
    text = re.sub(r'\(\((.*?)\)\)', r'<ins>\1</ins>', text)
    return text

if __name__ == "__main__":
    main()
