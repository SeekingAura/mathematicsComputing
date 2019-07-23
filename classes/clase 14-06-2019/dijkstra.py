import sys
import os

import matplotlib.pyplot as plt
import networkx as nx

notConnectedNodeColor="yellow"
connectedNodeColor="silver"
connectedNodeOutGroup="c"
notConnectedEdgeColor="silver"
connectedEdgecolor="black"
discardEdgeColor="r"

def generate_random_gnp(n):
	if(n<1):
		return None
	return nx.gnp_random_graph(n,0.5,directed=False)
	

def dijkstra(G):
	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")

	for nodeI in G.nodes():
		G.nodes[nodeI]["color"]==connectedNodeColor
		break
	
	n=nx.number_of_nodes(G)
	connectedNodes=0
	while connectedNodes<n:
		if(connectedNodes==0):
			

			connectedNodes+=1
