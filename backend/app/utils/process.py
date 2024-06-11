import re

def replace_spaces(strings, replacement):
    modified_strings = [s.replace(" ", replacement) for s in strings]
    return "".join(modified_strings)


def extract_tree_value(url):
    match = re.search(r'tree=(\d+)', url)
    if match:
        return match.group(1)
    return None
