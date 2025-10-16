import networkx as nx
from netgraph import InteractiveGraph
import matplotlib.pyplot as plt
from Members import MembersGraph


"""
Create an adjacency list graph
Visualize the adjacency list
"""

## Create adjacency list using dictionary
members_list = ["Josh", "Molly", "Morgon", "Louis", "Harry", "Justin", "Johann"]
members_graph = MembersGraph.LEGEND_GRAPH

## create a visualization of adjacency list as a directed graph
Graph = nx.DiGraph()
for node in members_graph:
    for neighbor in members_graph[node]:
        Graph.add_edge(node, neighbor)
        print(node, neighbor)
    print("###################")

# nx.draw(Graph, with_labels=True, node_color='blue')
plot_instance = InteractiveGraph(
    Graph,
          node_size=5, node_color='blue',
          node_labels=True, node_label_fontdict=dict(size=24),
          edge_color='grey', edge_width=2,
          arrows=True
)
plt.show()
