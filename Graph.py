from collections import deque

class Graph:
    def __init__(self):
        self.adj= {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = deque()

    def connect_node(self, a, b):
        if a not in self.adj or b not in self.adj:
            return
        if b not in self.adj[a]:
            self.adj[a].append(b)
            self.adj[b].append(a)

# we use index to avoid list.pop(0) which is O(n)
# we can remove elements once the queue is large to reduce memory
def bfs(graph, start, excluded_nodes=None):
    if excluded_nodes is None:
        excluded_nodes = set()

    visited = set([start])
    index = 0
    queue = [start]
    traversal_order = []
    THRESHOLD = 25

    while index < len(queue):
        current_node = queue[index]
        index += 1
        traversal_order.append(current_node)

        for neighbour in graph.adj[current_node]:
            if neighbour not in visited and neighbour not in excluded_nodes:
                visited.add(neighbour)
                queue.append(neighbour)

        #trim the queue in order to reduce memory
        if index >= THRESHOLD:
            queue = queue[index:]
            index = 0

    return traversal_order