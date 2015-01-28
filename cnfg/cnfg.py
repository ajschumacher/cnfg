import os
import codecs


def contents_of(path):
    """
    Return the file contents from `path` using UTF-8.
    """
    with codecs.open(path, "r", "utf-8") as f:
        contents = f.read()
    return contents

def load(filename):
    """
    Load `filename` from the user's home directory
    and return it `eval`'ed.
    A Python dict literal containing configuration settings
    is a good choice for the contents of the file.
    """
    implied_path = os.path.join("~", filename)
    full_path = os.path.expanduser(implied_path)
    contents = contents_of(full_path)
    python_thing = eval(contents)
    return python_thing
