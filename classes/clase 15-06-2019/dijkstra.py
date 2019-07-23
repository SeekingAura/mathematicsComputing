import sys
import os
import random


import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html

# Global vars
notConnectedNodeColor="yellow"
connectedNodeColor="silver"
connectedNodeFistColor="c"
notConnectedEdgeColor="silver"
connectedEdgecolor="black"
discardEdgeColor="r"

def generate_random_gnp(n):
	if(n<1):
		return None

	G = nx.Graph()
	G.add_nodes_from([i for i in range(n)])
	for nodeI in G.nodes():
		# incident edges to nodeI
		nodeIdegree=nx.degree(G,nodeI)
		if(nodeIdegree<n-1):
			# set number of edges in nodeI (max is n-1-nodeIdegree where n is number node sin graph (max edges in one node))
			for edgesNum in range(random.randint(1,(n-1)-nodeIdegree)):
				neighborsList=nx.neighbors(G,nodeI)
				while True:
					nodeJ=list(G.nodes())[random.randint(0,n-1)]
					if(nodeI!=nodeJ and not(nodeJ in neighborsList)):
						break
				G.add_weighted_edges_from([[nodeI, nodeJ, round(random.uniform(1, n**3), 2)]])

			
	return G
	
def draw_graph_states(G, graphNumber, pos):
	# create and connect to draw figure
	plt.figure(graphNumber, constrained_layout=True)
	plt.title("Dijkstra Parte {}".format(graphNumber), fontsize=16)

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
	# For debuggin
	# plt.show()


def dijkstra(G, pos=None, startNode=None):
	if(pos is None):
		pos=nx.spring_layout(G)
	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")


	for nodeI in G.nodes():
		G.nodes[nodeI]["color"]==connectedNodeColor
		break
	# list(G.edges())[random.randint(0, nx.number_of_edges(G))-1]
	n=nx.number_of_nodes(G)
	connectedNodes=[]
	
	# A
	totalWeigth={nodeI:0 for nodeI in G.nodes()}
	# B
	pathsResult={nodeI:[] for nodeI in G.nodes()}

	# draw first time
	stateNumber=0
	draw_graph_states(G, stateNumber, pos)
	stateNumber+=1

	# a starter node
	if(startNode is None):
		randomNode=list(G.nodes())[random.randint(0, nx.number_of_nodes(G))-1]
		G.nodes[randomNode]["color"]=connectedNodeFistColor
		connectedNodes.append(randomNode)
	else:
		G.edges[startNode]["color"]=connectedNodeFistColor
		connectedNodes.append(startNode)

	# Draw after first random node
	draw_graph_states(G, stateNumber, pos)
	stateNumber+=1

	while len(connectedNodes)<n:
		
		# check all edges
		minWeight=sys.maxsize
		edgeMinWeight=None
		for nodeFromI, nodeToI in G.edges(connectedNodes):
			if(G.edges[nodeFromI, nodeToI]["color"]==notConnectedEdgeColor):
				actualWeight=round(G.edges[nodeFromI, nodeToI]["weight"]+totalWeigth.get(nodeFromI), 2)
				if(actualWeight<minWeight):
					minWeight=actualWeight
					edgeMinWeight=[nodeFromI, nodeToI]

		#conect edge and node with minimun path weigth		
		G.edges[edgeMinWeight]["color"]=connectedEdgecolor
		G.nodes[edgeMinWeight[1]]["color"]=connectedNodeColor
		connectedNodes.append(edgeMinWeight[1])

		# Update hash of weigth and path data
		totalWeigth[edgeMinWeight[1]]=round(totalWeigth[edgeMinWeight[0]]+minWeight, 2)
		pathsResult[edgeMinWeight[1]]=pathsResult[edgeMinWeight[0]]+[edgeMinWeight]
		

		# check edges of the last added node and discart never uses of node
		for nodeFrom, nodeToI in G.edges(connectedNodes[-1]):
			if(G.edges[nodeFrom, nodeToI]["color"]==notConnectedEdgeColor and 
				(G.nodes[nodeToI]["color"]==connectedNodeColor or G.nodes[nodeToI]["color"]==connectedNodeFistColor)
			):
				G.edges[nodeFrom, nodeToI]["color"]=discardEdgeColor

		draw_graph_states(G, stateNumber, pos)
		stateNumber+=1
	return G, totalWeigth, pathsResult

if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	
	n=int(sys.argv[1])
	G=generate_random_gnp(n)
	G, totalWeigth, pathResult=dijkstra(G)
	print("pesos",totalWeigth)
	print("paths",pathResult)

	plt.show()


		


				

