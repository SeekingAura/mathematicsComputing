import sys

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph
# PyGraphviz
# https://github.com/CristiFati/Prebuilt-Binaries/tree/master/Windows/PyGraphviz
# Graphviz 64 bit windows
# https://github.com/mahkoCosmo/GraphViz_x64/
if __name__ == "__main__":
	G = nx.Graph()

	graphNodes=[
		0,1,2,3,4,5,6,7,8, 9.2
	]

	graphEdges=[
		[0, 1, {"color":"silver"}], 
		[1, 4, {"color":"silver"}],
		[1, 2, {"color":"black"}],
		[1, 5, {"color":"silver"}],
		[2, 3, {"color":"silver"}],
		[2, 7, {"color":"silver"}],
		[2, 6, {"color":"silver"}],
		[8, 7, {"color":"silver"}]

	]

	G.add_nodes_from(graphNodes)
	G.add_edges_from(graphEdges)

	nx.set_node_attributes(G, "silver", "color")
	nx.set_edge_attributes(G, "black", "color")

	G.nodes[1]["color"]="black"

	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	# Get position from node attrbiute
	pos=nx.spring_layout(G)
	
	nx.draw(G, pos, edge_color=edge_colors.values(), 
		node_color=node_colors.values(),with_labels=True, font_weight='bold'
	)
	plt.show()