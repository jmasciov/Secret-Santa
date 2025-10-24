import networkx as nx
from netgraph import InteractiveGraph
import matplotlib.pyplot as plt
from MembersInformation import member_graph
import time
import sys
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
###

## Create adjacency list using dictionary
members_graph = member_graph.LEGEND_GRAPH

## create a visualization of adjacency list as a directed graph
print("Creating input graph...")
input_graph = nx.DiGraph()
for node in members_graph:
    for neighbor in members_graph[node]:
        input_graph.add_edge(node, neighbor)
        # print(node, neighbor)
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
hamilton_path = nx.approximation.traveling_salesman_problem(input_graph, cycle=True)
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

plt.figure(2)
plot_instance = InteractiveGraph(
    hamilton_path_graph,
          node_size=5, node_color='red',
          node_labels=True, node_label_fontdict=dict(size=24),
          edge_color='grey', edge_width=2,
          arrows=True
)
# plt.draw()
# plt.show()