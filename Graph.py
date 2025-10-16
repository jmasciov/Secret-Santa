import networkx as nx
from netgraph import InteractiveGraph
import matplotlib.pyplot as plt


"""
Create an adjacency list graph
Visualize the adjacency list
"""

## Create adjacency list using dictionary
members_list = ["Josh", "Molly", "Morgon", "Louis", "Harry", "Justin", "Johann"]
members_graph = {}
members_graph['Josh'] = ["Molly", "Morgon", "Louis"]
members_graph['Molly'] = ["Josh", "Harry", "Justin", "Louis", "Johann"]
members_graph['Morgon'] = ["Harry", "Justin"]
members_graph['Louis'] = ["Harry", "Justin"]
members_graph['Harry'] = ["Molly", "Morgon"]
members_graph['Justin'] = ["Harry", "Justin"]
members_graph['Johann'] = ["Molly", "Morgon"]


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
