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
# H = nx.DiGraph(G)  # convert G to directed graph

""" set colors vars
	yellow are for not connected nodes
	silver nodes are connected
	black edges using for connected nodes
	red edges discard edges
"""
notConnectedNodeColor="yellow"
connectedNodeColor="silver"
notConnectedEdgeColor="silver"
connectedEdgecolor="blue"
discardEdgeColor="r"

def generate_custom_graph():
	G=nx.Graph()

	graphNodesList=[
		[1, {"pos":np.array([0, 1])}],
		[2, {"pos":np.array([1, 2])}],
		[3, {"pos":np.array([1, 0])}], 
		[4, {"pos":np.array([4, 2])}], 
		[5, {"pos":np.array([1, 1])}], 
		[6, {"pos":np.array([2, 1])}], 
		[7, {"pos":np.array([3, 1.3])}], 
		[8, {"pos":np.array([4, 1])}]
	]

	graphEdgesList=[
		#[0, 1, {"weight" : 1}],
		[1, 2, {"weight" : 1}],
		[1, 3, {"weight" : 7}],
		[1, 5, {"weight" : 19}],
		[2, 5, {"weight" : 6}],
		[2, 4, {"weight" : 10}],
		[2, 6, {"weight" : 15}],
		[3, 6, {"weight" : 2}],
		[3, 8, {"weight" : 14}],
		[4, 5, {"weight" : 3}],
		[4, 7, {"weight" : 4}],
		[4, 8, {"weight" : 20}],
		[5, 6, {"weight" : 11}],
		[6, 7, {"weight" : 12}],
		[6, 8, {"weight" : 13}],
		[7, 8, {"weight" : 5}],
	]

	G.add_nodes_from(graphNodesList)
	G.add_edges_from(graphEdgesList)

	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")

	return G


# Random graph generator where use a randopm python methods
def generate_random_graph_for_MST(n):
	if(n<1):
		return None
	
	G = nx.Graph()
	G.add_nodes_from([i for i in range(n)])
	
	for nodeI in G.nodes():
		# Edges for nodeI
		nodeIdegree=nx.degree(G,nodeI)
		# check if node is alredy full connected (max of edges)
		if(nodeIdegree<n-1):
			"""
			# Degree 0 indicates node are not conected yet in graph, should 
			# be set 1 edge to granted a connected graph
			"""
			if(nodeIdegree>0):
				minimunEdges=0
			else:
				minimunEdges=1

			"""
			Number of for iterations is a value between minimunEdges to n-1-nodeIdegree
			minimun edges depend of node degree.
			"""
			for edgesNum in range(random.randint(minimunEdges,(n-1)-nodeIdegree)):
				neighborsList=nx.neighbors(G,nodeI)
				while True:
					nodeJ=list(G.nodes())[random.randint(0,n-1)]
					if(nodeI!=nodeJ and not(nodeJ in neighborsList)):
						break
				# Set the random edges from last function with random weight
				G.add_weighted_edges_from([[nodeI, nodeJ, round(random.uniform(1, n), 2)]])

	# Set color of all nodes
	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")
	return G


def draw_graph_states(G, graphNumber, pos):
	plt.figure(graphNumber)
	plt.title("Boruvka Parte {}".format(graphNumber), fontsize=16)

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

# Undirected graphs
"""
# boruvka algorithm search a for lowest edge in edge and change color, on fist
# iteration is possible are graph not full conected in these case the next iterations are over
# this sub-graphs search for the edge with lowest weigth and change color if this edge
# connect to another sub-graph
"""
def partition_groups(G, pos):
	graphNumber=0

	groups=[[list(G.nodes())[0]]]
	for nodeI in G.nodes():
		neverAgrouped=False
		for enumGroups, groupI in enumerate(groups):
			haveNeighbors=False
			for nodeGroup in groupI:
				if(nodeI in nx.neighbors(G, nodeGroup)):
					# groups[enumGroups].append(nodeI)
					haveNeighbors=True
			
			# check if already exist on sub-groups
			if(not haveNeighbors):
				neverAgrouped=True
				groups[enumGroups].append(nodeI)
				# break

		if(neverAgrouped):
			groups.append([nodeI])

	return groups

					
	
if __name__=="__main__":
	if(len(sys.argv)>2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	elif(len(sys.argv)==2):	
		n=int(sys.argv[1])
		G=generate_random_graph_for_MST(n)
		pos=nx.spring_layout(G)
	else:
		G=generate_custom_graph()
		#pos=nx.circular_layout(G)
		pos={}
		# Replace pos from node attribute
		for nodeI, posI in G.nodes.data("pos"):
			pos[nodeI]=posI
	#mst_boruvka(G, pos)
	print(partition_groups(G, pos))
	#plt.show()