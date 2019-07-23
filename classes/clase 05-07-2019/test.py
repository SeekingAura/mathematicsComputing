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

	colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
	# graphNodes=[
	# 	[0, {"color":"silver"}], 
	# 	[1, {'color':"silver"}],
	# 	[2, {'color':"silver"}],
	# 	[3, {"color":"silver"}], 
	# 	[4, {'color':"silver"}],
	# 	[5, {"color":"silver"}], 
	# 	[6, {"color":"silver"}], 
	# 	[7, {"color":"silver"}], 
	# 	[8, {"color":"silver"}], 
	# 	["j", {"color":"silver"}]
	# ]
	graphNodes=[
		[0, {"color":"silver", "pos":np.array([0, 1.4])}], 
		[1, {'color':"lime", "pos":np.array([1, 1.6])}],
		[2, {'color':"lime", "pos":np.array([2, 1.4])}],
		[3, {"color":"silver", "pos":np.array([3, 2])}], 
		[4, {"color":"silver", "pos":np.array([0, 0.4])}], 
		[5, {"color":"lime", "pos":np.array([1, 0.2])}], 
		[6, {"color":"lime", "pos":np.array([2,0.4])}], 
		[7, {"color":"silver", "pos":np.array([3,1])}], 
		[8, {"color":"silver", "pos":np.array([3,0])}]
	]

	# graphEdges=[
	# 	[0, 1, {"color":"silver"}], 
	# 	[1, 2, {"color":"silver"}],
	# 	[2, 3, {"color":"silver"}],
	# 	[2, 8, {"color":"silver"}],
	# 	[2, 6, {"color":"silver"}],
	# 	[3, 0, {"color":"silver"}],
	# 	[4, 5, {"color":"silver"}],
	# 	[5, 7, {"color":"silver"}],
	# 	[6, 7, {"color":"silver"}],
	# 	[6, 4, {"color":"silver"}],
	# 	[8, "j", {"color":"silver"}]
	# ]

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

	#G.add_weighted_edges_from(graphEdges)
	# nx.set_node_attributes(G, colors[0], 'color')


	pos={}
	# Replace pos from node attribute
	for nodeI, posI in G.nodes.data("pos"):
		pos[nodeI]=posI
		
	# pos[1]=np.array([0.1, 0.1])
	#print(pos)

	print(G.edges[1,2])
	print(G.edges[[1,2]])
	# print(G.edges[(0, 1)]["weight"])
	data=[0, 1]
	
	print(G.edges([1,2]))

	#G=nx.from_prufer_sequence([3,1,3,2,4,5])
	#G=nx.random_tree(10)
	# pos=nx.spring_layout(G)
	#pos=nx.nx_agraph.pygraphviz_layout(G, prog='dot')
	#print(nx.is_tree(G))
	#print(nx.to_prufer_sequence(G))
	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")



	#edge_labels = nx.get_edge_attributes(G,'weight')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	print(nx.neighbors(G, 6))
	
	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	#pos[0]=pos[0]+0.2
	#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
	plt.show()