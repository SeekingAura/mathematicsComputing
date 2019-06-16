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
	("a", {"size":11, "color":colors[0]}), 
	("b", {'color':colors[0]}),
	("c", {'color':colors[0]}),
	("d", {"size":11, "color":colors[0]}), 
	("e", {'color':colors[0]})
]

graphEdges=[
	("a", "b", {"color":colors[-1], "weight":0.73}), 
	("a", "e", {"color":colors[-1]}),
	("a", "c", {"color":colors[-1]}),
	("b", "d", {"color":colors[-1]}),
	("b", "c", {"color":colors[-1]}),
	("b", "e", {"color":colors[-1]}),
	("c", "d", {"color":colors[-1]})
]

# graphEdges=[
# 	("uno", "dos", 3.0), 
# 	("dos", "tres", 7.5)
# ]

G = nx.DiGraph()
G.add_nodes_from(graphNodes)
G.add_edges_from(graphEdges)

#G.add_weighted_edges_from(graphEdges)
nx.set_node_attributes(G, colors[1], 'color')
G.node["b"]["color"]=colors[2]


pos=nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
node_colors=nx.get_node_attributes(G,'color')
edge_colors=nx.get_edge_attributes(G,'color')

#for i in nx.neighbors(G, "WA"):
#	print(i)



for enum, nodeI in enumerate(sorted(G.nodes)):
	if(enum<len(sorted(G.nodes))-1):
		print("\t{}".format(nodeI), end="")
	else:
		print("\t{}".format(nodeI))

for nodeI, listI in zip(sorted(G.nodes), nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense().tolist()):
	print("{}\t".format(nodeI), end="")
	for enum, listJ in enumerate(listI):
		if(enum<len(listI)-1):
			print(listJ,end="\t")
		else:
			print(listJ)

#A^2
# print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()**2)

nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

plt.show()