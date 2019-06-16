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

colorNonReadyNode="lime"
colorReadyNode="silver"
colorNonConecctedEdge="silver"


#def topological_solution(G):
#	for 

def graph_states(G, graphNumber, pos):
	fig=plt.figure(graphNumber)
	fig.suptitle("Topologico Parte {}".format(graphNumber), fontsize=16)

	# pos=nx.spring_layout(G)
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
	startNode=0
	while True:
		try:
			G = nx.gnp_random_graph(n,0.5,directed=True)
			# Generate random 
			# https://stackoverflow.com/questions/13543069/how-to-create-random-single-source-random-acyclic-directed-graphs-with-negative
			G = nx.DiGraph([(u,v) for (u,v) in G.edges() if u<v])
			nx.set_node_attributes(G, colorNonReadyNode, 'color')
			nx.set_edge_attributes(G, colorNonConecctedEdge, "color")
			break
		except:
			continue

	return G

def generateCustomGraph():
	G=nx.DiGraph()

	graphNodesList=[[i, {}] for i in range(1, 8)]

	graphEdgesList=[
		[2, 1, {}],
		[2, 3, {}],
		[2, 4, {}],
		[2, 7, {}],
		[1, 6, {}],
		[1, 3, {}],
		[4, 1, {}],
		[4, 3, {}],
		[4, 5, {}],
		[4, 7, {}],
		[7, 6, {}],
		[3, 6, {}],
		[3, 5, {}],
		[5, 7, {}],
		[5, 6, {}]
	]

	G.add_nodes_from(graphNodesList)
	G.add_edges_from(graphEdgesList)

	nx.set_node_attributes(G, "silver", 'color')
	nx.set_edge_attributes(G, "black", "color")

	return G



def setTopologicalADG(G):
	#nx.DiGraph(G)# topological graph
	numberOfNodes=nx.number_of_nodes(G)

	nx.set_node_attributes(G, colorNonReadyNode, 'color')
	nx.set_edge_attributes(G, colorNonConecctedEdge, "color")

	# Relabeling nodes for execute algorithm
	alphabetList=[chr(i) for i in range(ord("a"),ord("a")+26)]
	mapping = {old_label:new_label for new_label, old_label in
		zip(alphabetList[:numberOfNodes], G.nodes())
	}

	G = nx.relabel_nodes(G, mapping)
	pos=nx.spring_layout(G) #principal pos
	# Get equivalent keys before of mapping (for changes while algoritm)
	labelsEquival={label:label for label in pos.keys()}

	labelNodes=0
	# get equivalent
	posUpdate={labelsEquival.get(posEQ):pos.get(posEQ) for posEQ in pos}
	# Graph first state
	graph_states(G, labelNodes, posUpdate)
	labelNodes+=1

	while numberOfNodes>=labelNodes:
		for nodeI, nodeColor in G.nodes.data("color"):

			inNodesNotReady=True
			for nodeFromI, nodeToI in G.in_edges(nodeI):
				# if have 1 node not ready this are discard
				if(G.nodes[nodeFromI]["color"]==colorNonReadyNode):
					inNodesNotReady=False

			if(not inNodesNotReady or nodeColor==colorReadyNode):
				continue

			G = nx.relabel_nodes(G, {nodeI:labelNodes})
			G.nodes[labelNodes]["color"]=colorReadyNode
			if(nodeI in labelsEquival):
				labelsEquival[nodeI]=labelNodes


			posUpdate={labelsEquival.get(posEQ):pos.get(posEQ) for posEQ in pos}
			graph_states(G, labelNodes, posUpdate)
			
			labelNodes+=1


	
if __name__=="__main__":
	if(len(sys.argv)>2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	if(len(sys.argv)==2):
		n=int(sys.argv[1])
		G=generate_random_gnp(n)
	else:
	#G=generate_random_gnp(n)

		G=generateCustomGraph()

	setTopologicalADG(G)
	print(nx.is_directed_acyclic_graph(G))

	# Drawing

	plt.show()
