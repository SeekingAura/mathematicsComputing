# Getting Started
Graphs theory is a important discipline because of its Computer Science, Communication Networks, and Combinatorial optimization with this can design a representation of algorithms and make more efficient in python with **networkx** can make graphs in computing systems for understood how this python module work graphs start with a simple graphs

# Content
* S


# Make a custom graph with python list
Networkx can interpret differents data python structures, on certain structures can set custom features, but the networkx graph instances can edit the graph with  methods and access to data structure and nodes but for custom graphs and add new nodes is better use an external python data structure such as list and dictionaries.

### Graph instance
Manage graph data and execute algorithms of networx work with python data structures for usage of module networkx require a instance of graph this module use different graph instances from type of graph some of these are:
* Undirected
* Directed
* Multi-Undirected
* Multi-Directed

This instances are separated because the operations and some features must be different, a graph can be create empty with the next code:

```python
# import module for graphs with alias nx
import networkx as nx

# Undirected graph
G = nx.Graph()

# Directed graph
DiG=nx.DiGraph()

# Multi-Undirected graph
MG=nx.MultiGraph()

# Multi-Directed graph
MDiG=nx.MultiDiGraph()
```

The previous code create empty graph of different graph type's all can receive different params such as edges, nodes, graph name and more. This object instances of graphs have methods that manage a graph, can add nodes, edges, edit features of nodes and edges, execute some algorithms andtheorems, get values of graph properties and more.

### Nodes
To add nodes into [graph instance](#Graph-instance) can use methods of that for add nodes manually but is complicated and the method add one to one this is ineficient for multiple nodes, to add multiple nodes the module networkx have methods that interpret a python list with certain structure one simple way following the next code:
```python
nodesList=[
	"name 1",
	"name 2",
	...
	"name n"
]
```

Each value of list is a name or ID of every node, this "name" is most common use a data type be a string or integer but networkx accept a lot diferent data types such as float, long, double and custom objects that have a diferent *\_\_str\_\_* (python attribute objects for string representation) value between object instances from the same class, the method to add nodes from python list is with the method of graph instance *add_nodes_from*, here a example.

```python
# Add the nodes in the list to graph instance
G.add_nodes_from(nodesList)
```

**G** is a graph instance and **nodesList** is the list with node names but is only node names, the features can set in the previous list with list of lists, that is sub-list per node, where first element is name of node and second element is a python dictionary with keys the name of feature and value is value of that feature, here a example.

```python
nodesList=[
	[1, {"color": "white", "size": 10, "secondary_name":"one"}],
	[2],
	[3, {"executed":True, "color":"black"}]
	...,
	["node n", {"key 1":"value 1", "key 2":"value 2" ... "key n":"value n"}]
]
```

The previous list indicates the features with dictionary per node, this features can set diferent for each node and not require set in all the keys of others nodes but for avoid errors and can operate all algoritms should be set in all any value for all different keys in the graph nodes.

### Edges
To add nodes into [graph instance](#Graph-instance) can use methods of that for add edges manually but have similary problems that nodes and networkx have a similary function to add from python list, here a example with edge features

```python
edgesList=[
	["nodeFrom 1", "nodeTo 1", {"color":"black", "otherFeature": "otherValue"}],
	["nodeFrom 2", "nodeTo 2"] ,
	...
	["nodeFrom n", "nodeTo n", {"otherFeature": "otherValue"}] ,
]
```

The previous structure for each edge require the start node and end node where each sub-list is a edge first value is node from, second value is node to this nodes are the same key used on the list (if used string "1" the key for this node is string "1" and not integer 1), features are similary to nodes but on this case dictionary are in the position 3 of sub-list with the same rules.


# Drawing

# Simple Graphs
Simple graph or Strict graph is a set of nodes and edges where the edges connect nodes with few features and follow the next rules.
* Edges have exactly 2 nodes
* Conections of edges between their pairs nodes must be different (no loops).
* All edges orientation is only in both directions (undirected graph)
* Edges dont have weigth or other similary value (unweighted graph)
* Edges and nodes can have draw features such as:
	* Color
	* Size
	* Position
	* Style
	* Label (name, work such as ID)

The graphs of this examples will be connected (from any node can make a path to any other node)

