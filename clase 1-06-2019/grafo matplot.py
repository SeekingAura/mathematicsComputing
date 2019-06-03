import sys

import matplotlib.pyplot as plt
import networkx as nx
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph


DG = nx.DiGraph()

colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
graphNodes=[
	["WA", {"size":11, "color":colors[0]}], 
	["NT", {'color':colors[0]}],
	["SA", {'color':colors[0]}],
	["Q", {"size":11, "color":colors[0]}], 
	["NSW", {'color':colors[0]}],
	["V", {'color':colors[0]}]
]

graphEdges=[
	["WA", "NT", {"color":colors[-1]}], 
	["WA", "SA", {"color":colors[-1]}],
	["NT", "Q", {"color":colors[-1]}],
	["NT", "SA", {"color":colors[-1]}],
	["SA", "Q", {"color":colors[-1]}],
	["SA", "NSW", {"color":colors[-1]}],
	["SA", "V", {"color":colors[-1]}],
	["SA", "Q", {"color":colors[-1]}],
	["Q", "NSW", {"color":colors[-1]}],
	["Q", "SA", {"color":colors[-2]}],
	["Q", "NT", {"color":colors[-1]}],
	["NSW", "V", {"color":colors[-1]}],
]

# graphEdges=[
# 	("uno", "dos", 3.0), 
# 	("dos", "tres", 7.5)
# ]

G = nx.Graph()
G.add_nodes_from(graphNodes)
G.add_edges_from(graphEdges)

#G.add_weighted_edges_from(graphEdges)
nx.set_node_attributes(G, colors[1], 'color')
G.node["NSW"]["color"]=colors[2]


pos=nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
node_colors=nx.get_node_attributes(G,'color')
edge_colors=nx.get_edge_attributes(G,'color')

#for i in nx.neighbors(G, "WA"):
#	print(i)

for nodeI, listI in zip(sorted(G.nodes), nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()):
	print("{}\t{}".format(nodeI, listI))

#A^2
print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()**2)

#print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()*)

#for i in nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense():
#	print(i)
# print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense())

nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

plt.show()