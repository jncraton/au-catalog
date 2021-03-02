import re

with open("catalog.txt") as f:
    content = f.read()

    # Remove page footer
    content = re.sub('^\d+\s+Anderson University Undergraduate Catalog.*$', '', content, flags=re.M)
    content = re.sub('^.*Anderson University Undergraduate Catalog, .*\d+.*$', '', content, flags=re.M)

    # Use proper headings
    content = re.sub(r'^\s{20,}([\w ]{5,50})$', r'\n\1\n============================\n', content, flags=re.M)
    content = re.sub(r'^([A-Z\W]{5,})$', r'\n\1\n------------------------------\n', content, flags=re.M)

    # Misc fix-ups
    content = re.sub(r'\.{20,}', '', content)

    # Add paragraph double spacing (identified using leading whitespace)
    content = re.sub(r"^\s+(\w)", r"\n\1", content, flags=re.M)

    # Remove excessive spacing
    #content = re.sub('\n(\s*\n)+', '\n\n', content, flags=re.M)

    print(content)
