import sys
import random

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

def trayectoria_aumento(G):
	
	tempG=G.to_directed()
	tempG=nx.create_empty_copy(tempG)



	leftNodes, rigthNodes = nx.bipartite.sets(G)
	maximalMatch=nx.maximal_matching(G)

	tempG.add_nodes_from(
		[
			["start", {"color":"orange"}], 
			["end", {"color":"orange"}]
		]
	)

	# set new post

	top = nx.bipartite.sets(G)[0]# Top is leftpart
	pos=nx.bipartite_layout(G, top)
	pos["start"]=np.array([-1.5, 0.5])
	pos["end"]=np.array([1.5, 0.5])


	for nodeFromI, nodeToI in maximalMatch:
		tempG.add_edges_from(
			[
				[nodeFromI, nodeToI, {"color":"red"}]
			]
		)

		if(nodeFromI in leftNodes):
			tempG.add_edges_from(
				[
					["start", nodeFromI, {"color":"silver"}]
				]
			)
		if(nodeToI in leftNodes):
			tempG.add_edges_from(
				[
					["start", nodeToI, {"color":"silver"}]
				]
			)
		if(nodeFromI in rigthNodes):
			tempG.add_edges_from(
				[
					[nodeFromI, "end", {"color":"silver"}]
				]
			)
		if(nodeToI in rigthNodes):
			tempG.add_edges_from(
				[
					[nodeToI, "end", {"color":"silver"}]
				]
			)
	for edgeI in G.edges():###
		if(not edgeI in tempG.edges() and not edgeI[::-1] in tempG.edges()):
			tempG.add_edges_from(
			[
				[nodeFromI, nodeToI, {"color":"black"}]
			]
		)
	return tempG, pos

		


if __name__ == "__main__":
	G = nx.Graph()
	X=[1,3,6,8,10,12,14,15,17,18]
	Y=[2,4,5,7,9,11,13,16,19]
	G.add_nodes_from(X, bipartite=0)
	G.add_nodes_from(Y, bipartite=1)
	graphEdgesList=[
		[1, 2], 
		[1, 5],
		[2, 6],
		[5, 6],
		[5, 10],
		[6, 11],
		[10, 11],
		[11, 12],
		[11, 15],
		[12, 16],
		[12, 7],
		[12, 13],
		[15, 16],
		[16, 18],
		[7, 3],
		[3, 4],
		[4, 8],
		[8, 9],
		[8, 13],
		[9, 14],
		[13, 14],
		[13, 17],
		[17, 19],
		[18, 19],

	]
	G.add_edges_from(graphEdgesList)
	
	#G = nx.bipartite.gnmk_random_graph(3, 5, 10, seed=123)
	
	#G =  nx.complete_graph(5)



	colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
	
	for edgeI in G.edges:
		G.edges[edgeI]["weight"]=random.randint(1, 99)

	
	# pos=nx.nx_agraph.pygraphviz_layout(G, prog='dot')
	# print(nx.is_tree(G))
	# print(nx.to_prufer_sequence(G))

	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")
	G, pos=trayectoria_aumento(G)
	

	

	
	

	

	edge_labels = nx.get_edge_attributes(G,'weight')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	
	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	#pos[0]=pos[0]+0.2
	#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
	plt.show()