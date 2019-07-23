import sys

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph

if __name__ == "__main__":
    G = nx.Graph()

    colors=["silver", "red", "forestgreen", "oliva", "gold", "teal"]
    # graphNodes=[
    # 	["a", {"color":"silver"}], 
    # 	["b", {'color':"silver"}],
    # 	["c", {'color':"silver"}],
    # 	["d", {"color":"silver"}], 
    # 	["e", {'color':"silver"}],
    # 	["f", {"color":"silver"}], 
    # 	["g", {"color":"silver"}], 
    # 	["h", {"color":"silver"}], 
    # 	["i", {"color":"silver"}], 
    # 	["j", {"color":"silver"}]
    # ]
    [[],2,3,4,5]
    graphNodes=[
        ["a", {"color":"silver", "pos":np.array([1, 2.5])}], 
        ["b", {'color':"lime", "pos":np.array([2, 2.7])}],
        ["c", {'color':"lime", "pos":np.array([3, 2.5])}],
        ["d", {"color":"silver", "pos":np.array([4, 3])}], 
        ["e", {"color":"silver", "pos":np.array([1, 1.5])}], 
        ["f", {"color":"lime", "pos":np.array([2, 1.3])}], 
        ["g", {"color":"lime", "pos":np.array([3,1.5])}], 
        ["h", {"color":"silver", "pos":np.array([4,2])}], 
        ["i", {"color":"silver", "pos":np.array([4,1])}]
    ]

    # graphEdges=[
    # 	["a", "b", {"color":"silver"}], 
    # 	["b", "c", {"color":"silver"}],
    # 	["c", "d", {"color":"silver"}],
    # 	["c", "i", {"color":"silver"}],
    # 	["c", "g", {"color":"silver"}],
    # 	["d", "a", {"color":"silver"}],
    # 	["e", "f", {"color":"silver"}],
    # 	["f", "h", {"color":"silver"}],
    # 	["g", "h", {"color":"silver"}],
    # 	["g", "e", {"color":"silver"}],
    # 	["i", "j", {"color":"silver"}]
    # ]

    graphEdges=[
        ["a", "b", {"color":"silver", "weight":1}], 
        ["a", "e", {"color":"silver", "weight":1}],
        ["a", "f", {"color":"silver", "weight":1}],
        ["b", "e", {"color":"silver", "weight":1}],
        ["b", "c", {"color":"black", "weight":1}],
        ["b", "f", {"color":"silver", "weight":1}],
        ["e", "f", {"color":"silver", "weight":1}],
        ["f", "g", {"color":"black", "weight":1}],
        ["c", "d", {"color":"silver", "weight":1}],
        ["c", "h", {"color":"silver", "weight":1}],
        ["c", "g", {"color":"silver", "weight":1}],
        ["d", "h", {"color":"silver", "weight":1}],
        ["g", "i", {"color":"silver", "weight":1}],
        ["g", "h", {"color":"silver", "weight":1}],
        ["i", "h", {"color":"silver", "weight":1}]

    ]


    G.add_nodes_from(graphNodes)
    G.add_edges_from(graphEdges)

    #G.add_weighted_edges_from(graphEdges)
    # nx.set_node_attributes(G, colors[1], 'color')


    pos={}
    #print(pos)
    for nodeI, posI in G.nodes.data("pos"):
        pos[nodeI]=posI
        
    # pos["b"]=np.array([0.2, 0.2])
    #print(pos)

    print(G.edges(["a", "b"]))
    data=["a", "b"]
    G.edges[data]["color"]="red"

    edge_labels = nx.get_edge_attributes(G,'weight')
    node_colors=nx.get_node_attributes(G,'color')
    edge_colors=nx.get_edge_attributes(G,'color')

    
    nx.draw(G, pos, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

    #pos["a"]=pos["a"]+0.3
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')
    plt.show()

    #for i in nx.neighbors(G, "WA"):
    #	print(i)
    # print("---------")
    # for nodeI, listI in zip(sorted(G.nodes), nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()):
    # 	print("{}\t{}".format(nodeI, listI))

    # print("---------")
    # #A^2
    # for i in range(1, 4):
    #     print("---A^{}---".format(i))
    #     print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()**i)
    #     print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense().shape[1])
    #     print("---------")



    ####
    # print("formula")
    # matrixA=nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()
    # identidad=np.identity(matrixA.shape[0])

    # identidadMenosA=identidad-matrixA
    # print(identidadMenosA)
    # print(np.linalg.inv(identidadMenosA))
    # print(np.identity(3))
    ####
    #for i in nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense():
    #	print(i)
    # print(nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense())


    #print(nx.number_strongly_connected_components(G))