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


def draw_graph_states(G, graphNumber, pos):
	plt.figure(graphNumber)
	plt.title("Clique Parte {}".format(graphNumber), fontsize=16)

	# get atributes
	edge_labels = nx.get_edge_attributes(G,'weight')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),
		with_labels=True, font_weight='bold'
	)
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, 
		font_weight='bold'
	)

if __name__ == "__main__":
	G = nx.Graph()

	colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
	
	graphNodes=[
		[0, {"pos":np.array([0, 3])}], 
		[1, {"pos":np.array([1, 3])}],
		[2, {"pos":np.array([0, 2])}],
		[3, {"pos":np.array([1, 2])}], 
		[4, {"pos":np.array([2, 3])}], 
		[5, {"pos":np.array([3, 3])}], 
		[6, {"pos":np.array([2, 2])}], 
		[7, {"pos":np.array([3, 2])}], 
		[8, {"pos":np.array([0, 1])}],
		[9, {"pos":np.array([1, 1])}],
		[10, {"pos":np.array([0, 0])}],
		[11, {"pos":np.array([1, 0])}],
		[12, {"pos":np.array([2, 1])}],
		[13, {"pos":np.array([2, 0])}],
		[14, {"pos":np.array([3, 0])}]
	]


	graphEdges=[
		[0, 3], 
		[0, 1],
		[0, 2],
		[1, 3],
		[2, 3],
		[2, 8],
		[3, 6],
		[3, 12],
		[3, 9],
		[4, 5],
		[4, 6],
		[5, 7],
		[5, 6],
		[6, 7],
		[6, 9],
		[6, 12],
		[8, 9],
		[9, 12],
		[9, 11],
		[10, 11],
		[12, 13],
		[12, 14],
		[13, 14],
	]


	G.add_nodes_from(graphNodes)
	G.add_edges_from(graphEdges)


	#print(nx.number_of_cliques(G))
	#print(list(nx.find_cliques(G)))


	pos={}
	# Replace pos from node attribute
	for nodeI, posI in G.nodes.data("pos"):
		pos[nodeI]=posI
		

	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")

	draw_graph_states(G, 0, pos)

	for enum, cliqueI in enumerate(nx.find_cliques(G)):
		nx.set_node_attributes(G, "w", 'color')
		nx.set_edge_attributes(G, "w", "color")

		#change color for each node
		for nodeJ in cliqueI:
			G.nodes[nodeJ]["color"]="silver"

		# change color in edges of clique
		for nodeFromI, nodeToI in G.edges(cliqueI):
			# check if edge are in the cliqueI
			if(nodeFromI in cliqueI and nodeToI in cliqueI):
				G.edges[nodeFromI, nodeToI]["color"]="black"

		draw_graph_states(G, enum+1, pos)


	plt.show()