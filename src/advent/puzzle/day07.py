class Node(object):
    def __init__(self, name, type, parent=None, size=0):
        self.name = name
        self.type = type
        self.parent = parent
        self._size = size
        self.children = []

    def add_child(self, child):
        assert isinstance(child, Node)
        self.children.append(child)

    @property
    def size(self):
        return self._size + sum([child.size for child in self.children])

    def traverse(self, node_types=None):
        node_types = node_types or ["file", "dir"]
        all_childrens = [child for child in self.children if child.type in node_types]
        for child in self.children:
            all_childrens += child.traverse(node_types)
        return all_childrens

    def display(self, increment=0):
        print(increment * "  " + "- {}".format(self))
        increment += 1
        for child in self.children:
            child.display(increment)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.type, self.size)


INSTRUCTION_CD = "$ cd"
INSTRUCTION_LS = "$ ls"


def build_graph(data):
    root_directory = None
    current_directory = None
    listing = False
    for line in data:
        if line.startswith(INSTRUCTION_CD):
            name = line.split(INSTRUCTION_CD)[-1].strip()
            if not current_directory:
                current_directory = Node(name, None, 0)
                root_directory = current_directory
            elif name == "..":
                current_directory = current_directory.parent
            else:
                new_directory = [
                    dir for dir in current_directory.children if dir.name == name
                ][0]
                current_directory = new_directory
            listing = False
        elif line.startswith(INSTRUCTION_LS):
            listing = True
        elif listing:
            size, name = line.split()
            typ = "dir" if size == "dir" else "file"
            size = int(size) if typ == "file" else 0
            node = Node(name, typ, current_directory, size)
            current_directory.add_child(node)
    root_directory.display()
    return root_directory


class Puzzle(object):
    @classmethod
    def resolve_part_01(cls, data):
        root_directory = build_graph(data)
        size = sum(
            [
                node.size
                for node in root_directory.traverse(node_types=["dir"])
                if node.size <= 100000
            ]
        )
        return size

    @classmethod
    def resolve_part_02(cls, data):
        root_directory = build_graph(data)
        available_space = 70000000 - root_directory.size
        needed_space = abs(30000000 - available_space)
        candidates = [
            directory
            for directory in root_directory.traverse(node_types=["dir"])
            if directory.size >= needed_space
        ]
        return sorted(candidates, key=lambda dir: dir.size)[0].size
