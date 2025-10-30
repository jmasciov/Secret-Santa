import networkx as nx
from netgraph import InteractiveGraph
import matplotlib.pyplot as plt
from MembersInformation import member_graph
import time
import sys
import random
"""
Create an adjacency list graph
Visualize the adjacency list
https://networkx.org/documentation/stable/
https://networkx.org/documentation/stable/reference/algorithms/index.html
"""

###
### Lazy debug mode
# hamilton_path = ['B', 'C', 'D', 'A', 'G', 'E', 'F', 'B']

###
def find_hamiltonian_cycle(graph):
    N = len(graph.nodes)
    start_node = next(iter(graph.nodes)) # Pick any node to start

    # Recursive function for backtracking
    def backtrack(current_node, path):
        # Base case: Path is complete and can return to start_node
        if len(path) == N:
            if start_node in graph[current_node]:
                # Cycle found!
                return path + [start_node]
            return None

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in path:
                # Add neighbor to path and recurse
                new_path = backtrack(neighbor, path + [neighbor])
                if new_path:
                    return new_path
        return None

    return backtrack(start_node, [start_node])
###

###
def find_random_hamiltonian_cycle(graph):
    """
    Finds a directed Hamiltonian cycle using randomized backtracking.
    Returns a randomly chosen path (list of nodes) forming the cycle, or None.
    """
    N = len(graph.nodes)
    if N == 0:
        return None

    # Start the search from a random node to increase randomness
    nodes_list = list(graph.nodes)
    random.shuffle(nodes_list)
    start_node = nodes_list[0]

    def backtrack(current_node, path):
        # Base Case: Path is complete
        if len(path) == N:
            if start_node in graph[current_node]:
                return path + [start_node]
            return None

        # Get neighbors and SHUFFLE them for randomization
        neighbors = list(graph.neighbors(current_node))
        random.shuffle(neighbors)  # <--- The key randomization step

        # Explore neighbors in a randomized order
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = backtrack(neighbor, path + [neighbor])
                if new_path:
                    return new_path
        return None

    return backtrack(start_node, [start_node])
###

###
###

## Create adjacency list using dictionary
members_graph = member_graph.LEGEND_GRAPH

## create a visualization of adjacency list as a directed graph
print("Creating input graph...")
input_graph = nx.DiGraph()
for node in members_graph:
    for neighbor in members_graph[node]:
        input_graph.add_edge(node, neighbor)
    #     print(node, neighbor)
    # print("###################")
# nx.draw(Graph, with_labels=True, node_color='blue')
print("Input graph created.")
plt.figure(1)
plot_instance = InteractiveGraph(
    input_graph,
          node_size=5, node_color='blue',
          node_labels=True, node_label_fontdict=dict(size=24),
          edge_color='grey', edge_width=2,
          arrows=True
)
# plt.draw()
# plt.show()


# Find cycle and create new graph
## https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem.html#networkx.algorithms.approximation.traveling_salesman.traveling_salesman_problem

print("Starting Hamilton Path...")
start_time = time.perf_counter()
# hamilton_path = nx.approximation.traveling_salesman_problem(input_graph, cycle=True)
# hamilton_path = find_hamiltonian_cycle(input_graph)
hamilton_path = find_random_hamiltonian_cycle(input_graph)
end_time = time.perf_counter()
print("Hamilton Path created.")
elapsed_time = end_time - start_time
print(f"Hamilton Path elapsed time: {elapsed_time:.6f} seconds.")
# print(hamilton_path)
# print(type(hamilton_path))

hamilton_path_graph = nx.DiGraph()
for i in range(len(hamilton_path) - 1):
    hamilton_path_graph.add_edge(hamilton_path[i], hamilton_path[i+1])
# print(hamilton_path_graph)

# plt.figure(2)
# plot_instance = InteractiveGraph(
#     hamilton_path_graph,
#           node_size=5, node_color='red',
#           node_labels=True, node_label_fontdict=dict(size=24),
#           edge_color='grey', edge_width=2,
#           arrows=True
# )
# plt.draw()
# plt.show()