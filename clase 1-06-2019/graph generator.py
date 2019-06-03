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
	(1, {"color":colors[0]}), 
	(2, {'color':colors[0]}),
	(3, {'color':colors[0]}),
	(4, {"color":colors[0]}), 
	(5, {'color':colors[0]}),
	(6, {'color':colors[0]}),
	(7, {'color':colors[0]}),
	(8, {'color':colors[0]}),
]

graphEdges=[
	(1, 2), 
	(1, 4),
	(2, "Q"),
	("NT", "SA"),
	("SA", "Q"),
	("SA", "NSW"),
	("SA", "V"),
	("SA", "Q"),
	("Q", "NSW"),
	("Q", "SA"),
	("Q", "NT"),
	("NSW", "V"),
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

for i in nx.neighbors(G, "WA"):
	print(i)


nx.draw(G, pos, node_color=node_colors.values(),with_labels=True, font_weight='bold')

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

plt.show()