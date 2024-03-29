import os

def create_snippet(s) -> str:
    return "\n".join([
        "```",
        s,
        "```\n"
    ])

def create_image_link(file):
    return f"![]({os.path.relpath(file)})"

def section_template(section_name, snippets) -> str:
    return f"""
## {section_name}

{snippets}
"""

def create_section(d) -> str:
    snippets = []
    files = os.scandir(d.path)
    for file in files:
        is_image = file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
        if is_image:
            snippet = create_image_link(file)
            snippets.append(snippet)
        else:
            with open(file, encoding="utf8") as f:
                snippet = create_snippet(f.read())
                snippets.append(snippet)

    combined_snippets = "\n".join(snippets)

    return section_template(d.name, combined_snippets)


def main():
    sections = [create_section(d)
                for d in os.scandir(".")
                if d.name != '.git' and d.is_dir()]

    with open("SNIPPETS.md", "w", encoding="utf8") as snippets_file:
        snippets_file.write("# All Snippets \n")
        for s in sections:
            snippets_file.write(s)


if __name__ == '__main__':
    main()
