import sys
import os

import matplotlib.pyplot as plt
import networkx as nx
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.DiGraph(G)  # convert G to directed graph

""" strongly regular graph
	Exercise 1.1.3 from Graphs, Networks and Algorithms
	a -> grade of all verices
	c -> number of nodes adjacent to both x and y if area x and y are adjacent
	d -> number of nodes adjacent to x and y if area x and y are not adjacent
	n ->  number of elements for two-subsets nodes
	rules:
		a=2n-4, c=n-2, d=4
"""
def SGRGraphs(n):
	if(n<3):
		return None
	# get english alphabet
	alphaEnglishList=[chr(i) for i in range(ord("a"),ord("a")+26)]
	graphNodes=[]

	""" set pairs of x and y from with n different chars, works for networkx
		estructure such as
		graphNodes=[
			"ab", 
			"bc", 
			"ac"
		]
	"""
	for x in alphaEnglishList[:n]:
		for y in alphaEnglishList[:n]:
			if(x==y):       # discart a equal char
				continue
			
			pairChar=x+y        # set xy pair
			# discards xy and yx chars in the list[::-1] is a reverse string
			if(not (pairChar in graphNodes or pairChar[::-1] in graphNodes)):
				graphNodes.append(pairChar)
	
	# list of colors from matplotlib
	colors=[
		"k", "silver", "brown", "r", "salmon","orangered", "orange", 
		"chocolate","tan", "olive", "y", "yellow", "g", "lime", "darkcyan", "aqua",
		"cadetblue", "navy", "mediumpurple", "indigo", "darkviolet", "violet",
		"purple", "magenta", "mediumvioletred", "crimson", ""
	]
	graphEdges=[]
	for nodeX in graphNodes:
		for nodeY in graphNodes:
			if(nodeX==nodeY):
				continue
			if(nodeX[0] in nodeY):
				graphEdges.append([nodeX, nodeY, {"label":nodeX[0], 
					"color":colors[alphaEnglishList.index(nodeX[0])]
				}])
			elif(nodeX[1] in nodeY):
				graphEdges.append([nodeX, nodeY, {"label":nodeX[1],
					"color":colors[alphaEnglishList.index(nodeX[1])]
				}])
	
	return graphNodes, graphEdges

if __name__=="__main__":
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $n\n'.format(sys.argv[0]))
		os._exit(1)
	
	n=int(sys.argv[1])
	graphNodes, graphEdges=SGRGraphs(n)

	# Create a graph
	G = nx.Graph()
	G.add_nodes_from(graphNodes)
	G.add_edges_from(graphEdges)

	# Set color of all nodes
	nx.set_node_attributes(G, "silver", 'color')

	""" Draw Positions
	bipartite_layout(G, nodes[, align, scale, …])	Position nodes in two straight lines.
	circular_layout(G[, scale, center, dim])	Position nodes on a circle.
	kamada_kawai_layout(G[, dist, pos, weight, …])	Position nodes using Kamada-Kawai path-length cost-function.
	planar_layout(G[, scale, center, dim])	Position nodes without edge intersections.
	random_layout(G[, center, dim, seed])	Position nodes uniformly at random in the unit square.
	rescale_layout(pos[, scale])	Returns scaled position array to (-scale, scale) in all axes.
	shell_layout(G[, nlist, scale, center, dim])	Position nodes in concentric circles.
	spring_layout(G[, k, pos, fixed, …])	Position nodes using Fruchterman-Reingold force-directed algorithm.
	spectral_layout(G[, weight, scale, center, dim])	Position nodes using the eigenvectors of the graph Laplacian.
	"""
	pos=nx.circular_layout(G)

	# get atributes
	edge_labels = nx.get_edge_attributes(G,'label')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

	plt.show()