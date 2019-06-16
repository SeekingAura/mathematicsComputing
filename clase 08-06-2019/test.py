import sys

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph


G = nx.DiGraph()

colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
# graphNodes=[
# 	["a", {"color":colors[0]}], 
# 	["b", {'color':colors[0]}],
# 	["c", {'color':colors[0]}],
# 	["d", {"color":colors[0]}], 
# 	["e", {'color':colors[0]}],
# 	["f", {"color":colors[0]}], 
# 	["g", {"color":colors[0]}], 
# 	["h", {"color":colors[0]}], 
# 	["i", {"color":colors[0]}], 
# 	["j", {"color":colors[0]}]
# ]

graphNodes=[
	["a", {"color":colors[0]}], 
	["b", {'color':colors[0]}],
	["c", {'color':colors[0]}],
	["d", {"color":colors[0]}], 
]

# graphEdges=[
# 	["a", "b", {"color":colors[-1]}], 
# 	["b", "c", {"color":colors[-1]}],
# 	["c", "d", {"color":colors[-1]}],
# 	["c", "i", {"color":colors[-1]}],
# 	["c", "g", {"color":colors[-1]}],
# 	["d", "a", {"color":colors[-1]}],
# 	["e", "f", {"color":colors[-1]}],
# 	["f", "h", {"color":colors[-1]}],
# 	["g", "h", {"color":colors[-1]}],
# 	["g", "e", {"color":colors[-1]}],
# 	["i", "j", {"color":colors[-1]}]
# ]

graphEdges=[
	["a", "b", {"color":colors[-1]}], 
	["b", "a", {"color":colors[-1]}],
    ["b", "c", {"color":colors[-1]}],
    ["a", "d", {"color":colors[-1]}],
]


G.add_nodes_from(graphNodes)
G.add_edges_from(graphEdges)

#G.add_weighted_edges_from(graphEdges)
# nx.set_node_attributes(G, colors[1], 'color')


pos=nx.circular_layout(G)
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
for i in range(1, 4):
    print("---A^{}---".format(i))
    print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()**i)
    print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense().shape[1])
    print("---------")



####
# print("formula")
# matrixA=nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()
# identidad=np.identity(matrixA.shape[0])

# identidadMenosA=identidad-matrixA
# print(identidadMenosA)
# print(np.linalg.inv(identidadMenosA))
# print(np.identity(3))
####
#for i in nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense():
#	print(i)
# print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense())


#print(nx.number_strongly_connected_components(G))

nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
# plt.show()