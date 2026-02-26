class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, origin, destination, weight):
        if origin not in self.graph:
            self.graph[origin] = []
        self.graph[origin].append((destination, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])
