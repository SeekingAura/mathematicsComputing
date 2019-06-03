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
connectedNodeOutGroup="c"
notConnectedEdgeColor="silver"
connectedEdgecolor="black"
discardEdgeColor="r"

def generate_random_graph_for_MST(n):
	if(n<1):
		return None
	
	G = nx.Graph()
	G.add_nodes_from([i for i in range(n)])
	
	for nodeI in G.nodes():
		# Edges for nodeI
		nodeIdegree=nx.degree(G,nodeI)
		if(nodeIdegree<n-1):
			for edgesNum in range(random.randint(1,(n-1)-nodeIdegree)):
				neighborsList=nx.neighbors(G,nodeI)
				while True:
					nodeJ=list(G.nodes())[random.randint(0,n-1)]
					if(nodeI!=nodeJ and not(nodeJ in neighborsList)
					):
						break
				G.add_weighted_edges_from([[nodeI, nodeJ, round(random.uniform(1, n), 2)]])

	# Set color of all nodes
	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")
	return G


# Kruskal makes a graph to minimun Spanning Tree, get all edges and
# order by weight (minumun to max) and for each edge iteration connect nodes
# the nodes to connect only connect with edge if not are alredy connected at
# the same graph
def graph_states(G, graphNumber, pos):
	fig=plt.figure(graphNumber)
	fig.suptitle("Kruskal Parte {}".format(graphNumber), fontsize=16)

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

def connect_neighbors_nodes(G, nodeCheck, connectedNodes):
	# Check if nodeFromI are not connected yet
	for nodeFromI, nodeToI, colorEdgeI in G.edges.data("color", nbunch=nodeCheck):
		# Set nodeTo with different node to nodeFromI
		if(nodeFromI!=nodeCheck):
			temp=nodeToI
			nodeToI=nodeFromI
			nodeFromI=temp

		"""Check if edge go from new connected edge 
			to alredy connected edge
		"""
		if(colorEdgeI==connectedEdgecolor and 
			G.nodes[nodeToI]["color"]==connectedNodeOutGroup
		):
			G.nodes[nodeToI]["color"]=connectedNodeColor
			connectedNodes.append(nodeToI)
			discard_edges(G, nodeToI)
			connect_neighbors_nodes(G, nodeToI, connectedNodes)

def discard_edges(G, nodeCheck):
	# Check if nodeFromI are not connected yet
	for nodeFromI, nodeToI, colorEdgeI in G.edges.data("color", nbunch=nodeCheck):
		# Set nodeTo with different node to nodeFromI

		"""Check if edge go from new connected edge 
			to alredy connected edge
		"""
		if(colorEdgeI==notConnectedEdgeColor):
			if((G.nodes[nodeFromI]["color"]==connectedNodeColor and 
				G.nodes[nodeToI]["color"]==connectedNodeColor) or 
				(G.nodes[nodeFromI]["color"]==connectedNodeOutGroup and 
				G.nodes[nodeToI]["color"]==connectedNodeOutGroup)
			):
				G.edges[nodeFromI, nodeToI]["color"]=discardEdgeColor

# Undirected graphs
def mst_kruskal(G):
	pos=nx.circular_layout(G)
	graphNumber=0
	graph_states(G, graphNumber, pos)
	graphNumber+=1


	connectedNodes=[]
	
	while len(connectedNodes)<n:
		for nodeFromI, nodeToI, weightFromTo in sorted(G.edges.data("weight"), 
			key=lambda edge: edge[2]
		):
			
			if(len(connectedNodes)==0):		# For first time
				connectedNodes.append(nodeFromI)
				connectedNodes.append(nodeToI)
				G.nodes[nodeFromI]["color"]=connectedNodeColor
				G.nodes[nodeToI]["color"]=connectedNodeColor
				G.edges[nodeFromI, nodeToI]["color"]=connectedEdgecolor
				graph_states(G, graphNumber, pos)
				graphNumber+=1
				continue

			# for others connections, only check silver edges
			if(G.edges[nodeFromI, nodeToI]["color"]==notConnectedEdgeColor):
				
				# check if are nodeFromI or nodeToI not already connected
				if(G.nodes[nodeFromI]["color"]==notConnectedNodeColor or 
					G.nodes[nodeToI]["color"]==notConnectedNodeColor or
					(nodeFromI in connectedNodes and 
					not(nodeToI in connectedNodes)) or 
					(nodeToI in connectedNodes and 
					not(nodeFromI in connectedNodes))
				):
					G.edges[nodeFromI, nodeToI]["color"]=connectedEdgecolor
					

				# Case a nodeFromI not conected yet but nodeToI is in main connected
				if(nodeFromI in connectedNodes and
					not(nodeToI in connectedNodes)
				):
					G.nodes[nodeToI]["color"]=connectedNodeColor
					connectedNodes.append(nodeToI)
					connect_neighbors_nodes(G, nodeToI, connectedNodes)
					discard_edges(G, nodeToI)
				elif(nodeToI in connectedNodes and 
					not(nodeFromI in connectedNodes)
				):
					G.nodes[nodeFromI]["color"]=connectedNodeColor
					connectedNodes.append(nodeFromI)
					connect_neighbors_nodes(G, nodeFromI, connectedNodes)
					discard_edges(G, nodeFromI)
				
				
				
				if(not(nodeFromI in connectedNodes)):
					G.nodes[nodeFromI]["color"]=connectedNodeOutGroup
				if(not(nodeToI in connectedNodes)):
					G.nodes[nodeToI]["color"]=connectedNodeOutGroup

				graph_states(G, graphNumber, pos)
				graphNumber+=1
					
	
if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	
	n=int(sys.argv[1])
	G=generate_random_graph_for_MST(n)
	mst_kruskal(G)

	plt.show()