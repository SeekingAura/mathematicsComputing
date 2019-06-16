import sys

import matplotlib.pyplot as plt
import networkx as nx
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph


G = nx.Graph()

colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
graphNodes=[
	["1", {"color":colors[0]}], 
	["2", {'color':colors[0]}],
	["3", {'color':colors[0]}],
	["4", {"color":colors[0]}], 
	["5", {'color':colors[0]}]
]

graphEdges=[
	["1", "2", {"color":colors[-1]}], 
	["1", "3", {"color":colors[-1]}],
	["1", "4", {"color":colors[-1]}],
	["1", "4", {"color":colors[-1]}],
	["2", "3", {"color":colors[-1]}],
	["3", "5", {"color":colors[-1]}],
	["5", "4", {"color":colors[-1]}],
	["5", "2", {"color":colors[-1]}],
	["4", "2", {"color":colors[-1]}]
]


G.add_nodes_from(graphNodes)
G.add_edges_from(graphEdges)

#G.add_weighted_edges_from(graphEdges)
# nx.set_node_attributes(G, colors[1], 'color')


pos=nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
node_colors=nx.get_node_attributes(G,'color')
edge_colors=nx.get_edge_attributes(G,'color')

#for i in nx.neighbors(G, "WA"):
#	print(i)
print("---------")
for nodeI, listI in zip(sorted(G.nodes), nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()):
	print("{}\t{}".format(nodeI, listI))

print("---------")
#A^2
print("---------")
print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense())
print("---------")

print("---------")
print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()**2)
print("---------")
#for i in nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense():
#	print(i)
# print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense())

nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
plt.show()