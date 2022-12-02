from os.path import dirname, join, abspath

SRC_FOLDER = abspath(dirname(dirname(__file__)))
DATA_FOLDER = join(dirname(SRC_FOLDER), "data")


def read(filename):
    filepath = join(DATA_FOLDER, filename)
    with open(filepath, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]