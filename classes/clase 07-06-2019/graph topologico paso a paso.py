import sys
import os
import random

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# https://stackoverflow.com/questions/21895926/subplots-with-network-analysis-networkx 
# https://networkx.github.io/documentation/stable/reference/generators.html
# H = nx.DiGraph(G)  # convert G to directed graph


def graph_states(G, graphNumber, pos):
	fig=plt.figure(graphNumber)
	fig.suptitle("Topologico paso {}".format(graphNumber), fontsize=16)

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


def generate_random_gnp(n):
	if(n<1):
		return None
	

	

	nodesList=[]
	edgesList=[]
	#startNode=0

	G = nx.gnp_random_graph(n,0.5,directed=True)
	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")
	pos=nx.circular_layout(G)
	ADG= nx.DiGraph()
	numberGraph=0
	
	# Generate random 
	# https://stackoverflow.com/questions/13543069/how-to-create-random-single-source-random-acyclic-directed-graphs-with-negative
	for nodeFrom, nodeTo in G.edges():
		if(nodeFrom<nodeTo):
			if(nodeFrom not in nodesList):
				nodesList.append([nodeFrom, {"color":"silver"}])
			if(nodeTo not in nodesList):
				nodesList.append([nodeTo, {"color":"silver"}])
			edgesList.append([nodeFrom, nodeTo, {"color":"silver"}])

			ADG.add_nodes_from(nodesList)
			ADG.add_edges_from(edgesList)

			graph_states(ADG, numberGraph, pos)

			numberGraph+=1
		
		

	print(nx.is_directed_acyclic_graph(ADG))
	return G
	
if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	
	n=int(sys.argv[1])
	G=generate_random_gnp(n)

	plt.show()
