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

def graph_states(G, graphNumber, pos):
	fig=plt.figure(graphNumber)
	fig.suptitle("Eurelian Parte {}".format(graphNumber), fontsize=16)

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

	colors=["silver", "red", "orange", "lime", "y", "c"]
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
		["v1", {"color":"silver", "pos":np.array([1, 3])}], 
		["v2", {'color':"silver", "pos":np.array([0, 2])}],
		["v3", {'color':"silver", "pos":np.array([1, 2])}],
		["v4", {"color":"silver", "pos":np.array([2, 2])}], 
		["v5", {"color":"silver", "pos":np.array([0, 1])}], 
		["v6", {"color":"silver", "pos":np.array([1, 1])}],
		["v7", {"color":"silver", "pos":np.array([2, 1])}],
		["v8", {"color":"silver", "pos":np.array([1, 0])}]
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
		["v1", "v2", {"color":"black"}], 
		["v1", "v3", {"color":"black"}],
		["v1", "v4", {"color":"black"}],
		["v2", "v3", {"color":"black"}],
		["v2", "v5", {"color":"black"}],
		["v3", "v4", {"color":"black"}],
		["v3", "v6", {"color":"black"}],
		["v4", "v7", {"color":"black"}],
		["v5", "v6", {"color":"black"}],
		["v5", "v8", {"color":"black"}],
		["v6", "v7", {"color":"black"}],
		["v6", "v8", {"color":"black"}],
		["v7", "v8", {"color":"black"}]
	]	
	

	G.add_nodes_from(graphNodes)

	# graphEdges=[]
	# for nodeI in G.nodes():
	# 	for nodeJ in G.nodes():
	# 		print(nodeI, nodeJ)
	# 		if(nodeI!=nodeJ):
	# 			graphEdges.append([nodeI, nodeJ, {"color":"silver"}])
	G.add_edges_from(graphEdges)		


	

	#G.add_weighted_edges_from(graphEdges)
	# nx.set_node_attributes(G, colors[0], 'color')


	

	# pos=nx.spring_layout(G)
		
	# pos[1]=np.array([0.1, 0.1])
	#print(pos)

	#print(G.edges[1,2])
	#print(G.edges[[1,2]])
	# print(G.edges[(0, 1)]["weight"])
	# data=[0, 1]
	
	# print(G.edges([1,2]))

	#G=nx.from_prufer_sequence([3,1,3,2,4,5])
	#G=nx.random_tree(10)
	# pos=nx.spring_layout(G)
	#pos=nx.nx_agraph.pygraphviz_layout(G, prog='dot')
	#print(nx.is_tree(G))
	#print(nx.to_prufer_sequence(G))

	# G=nx.complete_graph(5)

	# 

	# nx.set_node_attributes(G, "silver", 'color')
	# nx.set_edge_attributes(G, "black", "color")

	# https://networkx.github.io/documentation/stable/reference/algorithms/tournament.html

	# https://networkx.github.io/documentation/stable/reference/algorithms/euler.html
	#print(nx.is_eulerian(G))
	#print(list(nx.eulerian_circuit(G)))
	# number=0
	# #for edgeI in nx.eulerian_circuit(G):
	# 	G.edges[edgeI]["color"]="red"
	# 	graph_states(G,number, pos)
	# 	number+=1

	###
	#G.edges[edgeI]["color"]="red"

	#G=nx.algorithms.tournament.random_tournament(6)
	#pos=nx.spring_layout(G)

	
	
	

	pos={}
	# Replace pos from node attribute
	for nodeI, posI in G.nodes.data("pos"):
		pos[nodeI]=posI

	G=nx.icosahedral_graph()

	pos=nx.spring_layout(G)


	chromaticDict=nx.coloring.greedy_color(G, strategy='largest_first')

	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")

	for nodeI in chromaticDict:
		# print(colors[chromaticDict.get(nodeI)])
		G.nodes[nodeI]["color"]=colors[chromaticDict.get(nodeI)]

	

	edge_labels = nx.get_edge_attributes(G,'weight')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	# print(nx.neighbors(G, 6))
	
	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	#pos[0]=pos[0]+0.2
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
	plt.show()