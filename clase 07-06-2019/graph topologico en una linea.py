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

colorNonSetNode="lime"
colorStartNode="yellow"
colorReadyNode="silver"
colorNonConecctedEdge="silver"


#def topological_solution(G):
#	for 

def generate_random_gnp(n):
	if(n<1):
		return None
	startNode=0
	while True:
		try:
			G = nx.gnp_random_graph(n,0.5,directed=True)
			# Generate random 
			# https://stackoverflow.com/questions/13543069/how-to-create-random-single-source-random-acyclic-directed-graphs-with-negative
			G = nx.DiGraph([(u,v) for (u,v) in G.edges() if u<v])
			nx.set_node_attributes(G, colorNonSetNode, 'color')
			nx.set_edge_attributes(G, colorNonConecctedEdge, "color")
			break
		except:
			continue

	# numberConecctions=random.randint(1, n)
	# for timesI in range(numberConecctions):
	# 	neighborsList=nx.neighbors(G, startNode)
	# 	while True:
	# 		nodeList=list(G.nodes())
	# 		nodeRandom=nodeList[random.randint(0, len(nodeList)-1)]
	# 		if(startNode!=nodeRandom and not(nodeRandom in neighborsList)):
	# 			break
	# 	G.add_edges_from([[startNode, nodeRandom, {"color": "black"}]])

	print(nx.is_directed_acyclic_graph(G))
	return G
	
if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	
	n=int(sys.argv[1])
	G=generate_random_gnp(n)

	pos=nx.circular_layout(G)

	# get atributes
	edge_labels = nx.get_edge_attributes(G,'label')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

	plt.show()
