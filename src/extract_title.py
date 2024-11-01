def extract_title(markdown):
    header = markdown.split('\n', maxsplit=1)

    if header[0][:2] != "# ":
        raise ValueError('no h1 header found')
    return header[0][2:]