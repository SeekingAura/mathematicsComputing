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
		[0, {"pos":np.array([0, 1.4])}], 
		[1, {"pos":np.array([1, 1.6])}],
		[2, {"pos":np.array([2, 1.4])}],
		[3, {"pos":np.array([3, 2])}], 
		[4, {"pos":np.array([0, 0.4])}], 
		[5, {"pos":np.array([1, 0.2])}], 
		[6, {"pos":np.array([2,0.4])}], 
		[7, {"pos":np.array([3,1])}], 
		[8, {"pos":np.array([3,0])}]
	]

	graphEdgesList=[
		[0, 1, {"weight" : 1}],
		[2, 1, {"weight" : 1}],
		[2, 3, {"weight" : 2}],
		[2, 4, {"weight" : 3}],
		[2, 7, {"weight" : 4}],
		[1, 6, {"weight" : 5}],
		[1, 3, {"weight" : 6}],
		[4, 1, {"weight" : 7}],
		[4, 3, {"weight" : 8}],
		[4, 5, {"weight" : 9}],
		[4, 7, {"weight" : 10}],
		[7, 6, {"weight" : 11}],
		[3, 6, {"weight" : 12}],
		[3, 5, {"weight" : 14}],
		[5, 7, {"weight" : 15}],
		[5, 6, {"weight" : 16}]
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

"""
# Prims makes a graph to minimun Spanning Tree, on first step get a random node
# and for each iteration search from the connected nodes the lesser weigth and 
"""
def draw_graph_states(G, graphNumber, pos):
	plt.figure(graphNumber)
	plt.title("Prims Parte {}".format(graphNumber), fontsize=16)

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
def mst_prims(G, pos):
	graphNumber=0
	draw_graph_states(G, graphNumber, pos)
	graphNumber+=1


	firstNode=list(G.nodes())[random.randint(0, nx.number_of_nodes(G))-1]
	G.nodes[firstNode]["color"]=connectedNodeColor
	connectedNodes=[firstNode]

	draw_graph_states(G, graphNumber, pos)
	graphNumber+=1
	
	while len(connectedNodes)<nx.number_of_nodes(G):
		lesserWeigthEdge=None
		minWeigthValue=sys.maxsize
		# Get lesser weigth
		for edgeI in G.edges(connectedNodes):
			# Check if edge is not alredy connected
			if(G.edges[edgeI]["color"]==notConnectedEdgeColor):
				if(G.edges[edgeI]["weight"]<minWeigthValue):
					minWeigthValue=G.edges[edgeI]["weight"]
					lesserWeigthEdge=edgeI
			
		connectedNodes.append(lesserWeigthEdge[1])
		G.nodes[lesserWeigthEdge[1]]["color"]=connectedNodeColor
		G.edges[lesserWeigthEdge]["color"]=connectedEdgecolor

		# Discard alredy connected edges
		for nodeFromI, nodeToI in G.edges(lesserWeigthEdge[1]):
			if(G.edges[nodeFromI, nodeToI]["color"]==notConnectedEdgeColor):
				if(G.nodes[nodeToI]["color"]==connectedNodeColor):
					G.edges[nodeFromI, nodeToI]["color"]=discardEdgeColor
		
		draw_graph_states(G, graphNumber, pos)
		graphNumber+=1
			
			
			
					
	
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
		pos=nx.spring_layout(G)
	mst_prims(G, pos)
	plt.show()