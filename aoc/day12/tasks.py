from __future__ import annotations
from enum import Enum, auto
from collections.abc import Callable


class NodeType(Enum):
    START = auto()
    END = auto()
    BIG = auto()
    SMALL = auto()


class Node:
    type: NodeType
    name: str
    edges: set[Node]

    def __init__(self, node_type: NodeType, name: str):
        self.name = name
        self.type = node_type
        self.edges = set()

    def __hash__(self) -> int:
        return hash(self.name)

    @classmethod
    def create(cls, name: str) -> Node:
        if name == 'start':
            return cls(NodeType.START, name)
        elif name == 'end':
            return cls(NodeType.END, name)
        elif name.islower():
            return cls(NodeType.SMALL, name)
        elif name.isupper():
            return cls(NodeType.BIG, name)
        raise ValueError('Name %s not allowed' % name)

    def connect(self, node: Node):
        self.edges.add(node)


class NetworkBuilder:
    nodes: dict[str, Node]

    def __init__(self):
        self.nodes = dict()

    def add_connection(self, one: str, two: str):
        if one not in self.nodes:
            self.nodes[one] = Node.create(one)
        if two not in self.nodes:
            self.nodes[two] = Node.create(two)
        self._connect(self.nodes[one], self.nodes[two])

    def start(self) -> Node:
        return self.nodes['start']

    def end(self) -> Node:
        return self.nodes['end']

    def valid(self) -> bool:
        return 'start' in self.nodes and 'end' in self.nodes

    def _connect(self, one: Node, two: Node):
        one.connect(two)
        two.connect(one)


def dfs(frm: Node, to: Node, constraint: Callable[[Node, list[Node]], bool], current_path: list[Node], found_paths: list[list[Node]]):
    current_path = current_path + [frm]
    if frm == to:
        found_paths.append(current_path)
        return
    valid_next_nodes = list(filter(lambda e: constraint(e, current_path), frm.edges))
    for node in valid_next_nodes:
        dfs(node, to, constraint, current_path, found_paths)


def satisfy_small_caves_allowed_once(node: Node, current_path: list[Node]) -> bool:
    return node.type == NodeType.BIG or node not in current_path


def satisfy_one_small_cave_allowed_twice(node: Node, current_path: list[Node]) -> bool:
    return satisfy_small_caves_allowed_once(node, current_path) or \
           (node.type == NodeType.SMALL and
            len(list(filter(lambda n: current_path.count(n) > 1 and n.type == NodeType.SMALL, current_path))) < 2)


def visualize(found_paths: list[list[Node]]):
    for found_path in found_paths:
        print('->'.join([node.name for node in found_path]))


def get_input() -> NetworkBuilder:
    with open('input.txt', 'r') as fp:
        builder = NetworkBuilder()
        for line in fp:
            n1, n2 = line.strip().split('-')
            builder.add_connection(n1, n2)

    assert builder.valid()
    return builder


def first_task():
    builder = get_input()
    found_paths = []
    dfs(builder.start(), builder.end(), satisfy_small_caves_allowed_once, [], found_paths)
    print(len(found_paths))


def second_task():
    builder = get_input()
    found_paths = []
    dfs(builder.start(), builder.end(), satisfy_one_small_cave_allowed_twice, [], found_paths)
    print(len(found_paths))


def main():
    first_task()
    second_task()


if __name__ == '__main__':
    main()
