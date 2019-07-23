import sys
import random 

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph

# Define colors
notConnectedNodeColor="yellow"
connectedNodeColor="silver"
connectedNodeOutGroup="c"
notConnectedEdgeColor="silver"
connectedEdgecolor="black"
discardEdgeColor="r"


def custom_graph():
	G = nx.Graph()
	graphNodes=[
		["a", {"pos":np.array([1, 2.5])}], 
		["b", {"pos":np.array([2, 2.7])}],
		["c", {"pos":np.array([3, 2.5])}],
		["d", {"pos":np.array([4, 3])}], 
		["e", {"pos":np.array([1, 1.5])}], 
		["f", {"pos":np.array([2, 1.3])}], 
		["g", {"pos":np.array([3,1.5])}], 
		["h", {"pos":np.array([4,2])}], 
		["i", {"pos":np.array([4,1])}]
	]

	graphEdges=[
		["a", "b", {"capacity":1}], 
		["a", "e", {"capacity":1}],
		["a", "f", {"capacity":1}],
		["b", "e", {"capacity":1}],
		["b", "c", {"capacity":1}],
		["b", "f", {"capacity":1}],
		["e", "f", {"capacity":1}],
		["f", "g", {"capacity":1}],
		["c", "d", {"capacity":1}],
		["c", "h", {"capacity":1}],
		["c", "g", {"capacity":1}],
		["d", "h", {"capacity":1}],
		["g", "i", {"capacity":1}],
		["g", "h", {"capacity":1}],
		["i", "h", {"capacity":1}]

	]


	G.add_nodes_from(graphNodes)
	G.add_edges_from(graphEdges)

	#G.add_capacityed_edges_from(graphEdges)
	# nx.set_node_attributes(G, colors[1], 'color')


	pos={}
	#print(pos)
	for nodeI, posI in G.nodes.data("pos"):
		pos[nodeI]=posI
	
	nx.set_node_attributes(G, notConnectedNodeColor, 'color')
	nx.set_edge_attributes(G, notConnectedEdgeColor, "color")

	return G
# El arco a "comprimir" siempre es aleatorio hasta que haya 1 solo arco en el grafo
def min_cut(G):
	#while nx.number_of_edges(G)>1:
	toReduceNode=list(G.edges())[random.randint(0, nx.number_of_edges(G))-1]
	# G.nodes[toReduce]
	for nodeFrom, nodeto in nx.neighbors(toReduceNode):



		




if __name__ == "__main__":
	

	colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
	
	G=custom_graph()
	
	min_cut(G)
	
		
	# pos["b"]=np.array([0.2, 0.2])
	#print(pos)
	# edge_labels = nx.get_edge_attributes(G,'capacity')
	# node_colors=nx.get_node_attributes(G,'color')
	# edge_colors=nx.get_edge_attributes(G,'color')

	# nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_capacity='bold')

	# #pos["a"]=pos["a"]+0.3
	# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_capacity='bold')
	# plt.show()