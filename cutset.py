from itertools import combinations
from Graph import *

def is_connected_after_removal(graph, removed_nodes):
    
    # find a start node that is not removed
    remaining_nodes = [node for node in graph.adj if node not in removed_nodes]
    
    if not remaining_nodes:
        return False  # no nodees left = considered disconnected
    
    start = remaining_nodes[0]
    
    visited = bfs(graph, start, excluded_nodes=removed_nodes)

    # graph is connected if allremaining nodes are visited
    return len(visited) == len(remaining_nodes)


def k_cutset(graph, k):
    nodes = list(graph.adj.keys())

    # try all combinations of k nodes
    for combo in combinations(nodes, k):
        removed = set(combo)

        if not is_connected_after_removal(graph, removed):
            print("Cutset found:", combo)
            return True

    return False


def min_cutsets(graph):
    nodes = list(graph.adj.keys())

    for k in range(1, len(nodes)):
        cutsets = []

        for combo in combinations(nodes, k):
            removed = set(combo)

            if not is_connected_after_removal(graph, removed):
                cutsets.append(combo)

        if cutsets:
            return k, cutsets

    return None, []
