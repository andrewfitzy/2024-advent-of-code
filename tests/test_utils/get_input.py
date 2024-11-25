# Standard Library
import pathlib


def get_input(filename):
    """
    Takes a filename and returns a list of lines from the file
    """
    output = []
    file = pathlib.Path(filename)
    with open(file) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output
