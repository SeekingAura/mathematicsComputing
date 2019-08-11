# Mathematics for computing
This is a course of Master's degree in systems engineering of Technological University of Pereira, here a content of course give some definitions, algorithms and some aplicabilities of graphs, the implements of graphs, the information and some concepts of Graphs theory are based from Books: 

* Saha Ray, S. (2013). Graph Theory with Algorithms and its Applications: In Applied Science and Technology.

* Jungnickel, D. (2005). Graphs, networks and algorithms: Graphen, Netzwerke und Algorithmen.

* Julio Hernando Vargas, Invitación a la Matemática Discreta

The algorithms and some definitions are developed in programing languague [Python](https://www.python.org/about/) 3 with module [Networkx](https://networkx.github.io/) this python module have implemented some algorithms and have data structure for draw graphs and make custom algortims (great for the course)

# Content
Here a links of content of this README, the README have information about installation guide and resume of topics in the *Matemathics computing course
.
* [Basic Concepts](#Basic-Concepts)
    * [Graph](#Graph)
    * [Node](#Node)
    * [Edge](#Edge)
* [Install - Windows](#Install---Windows)
    * [Pre-requisites](#Pre-requisites)
        * [Install Pre-requisites](#Install-Pre-requisites)
            * [Python](#Python)
            * [Scipy](#Scipy)
            * [Numpy](#Numpy)
            * [Matplotlib](#Matplotlib)
            * [PyGraphviz](#PyGraphviz)
* [Data structure in networkx (representation)](#Data-structure-in-networkx-(representation))
    * [Nodes](#Nodes)
    * [Edges](#Edges)


# Basic Concepts
Concepts about main structure of graphs, this is required for algorithms, development and all about graph theory.

## Graph
A graph is a pair of sets N and E, where N is a set of Nodes and E is a set of Edges, graphs have several applications, exist different kind of graphs such as simple, multi-graph, undirected, directed, this depend about the "system" or model to represent.

## Node
In a Graph node is a area point where can interconnect multiple elements in the same area this can represent cities, coordinates, work areas, task, motors, states and others items that have a some usage, relation, connection or something with others nodes (usually in a graph all nodes are the same kind representation). A node can have several features not only a name of node are the representation can have more for example feautres of node in a graph such as size, color, font, etc, and features about representation for example if a node is a city the name of city is the name of node, others features is a latitude, length, altitude, population, etc, this features depend representation and analysis to do in the system or model.

## Edge
In a Graph node is the way, relation, connection that have a node with other node exist some kinds of edges such as directed, undirected, weighted, non weighted and more.

# Install - Windows
The source codes are implemented in *python languague* the version of python is 3.7.3 but also works with others versions of python 3 (the minimal requeriments is about the python modules to install), some modules require an aditional configuration foe example PyGraphiz also works with well with unofficial python modules.

## Pre-requisites
* Windows 7, 8 or 10 (any version, 64 bits recommended)
* Python 3.x
* SciPy (>= 1.1.0)
* NumPy (>= 1.15.4)  
* Matplotlib (>= 3.0.2) 
* PyGraphviz (>= 1.5) 
* pydot (>= 1.2.4) 

### Install Pre-requisites

#### Python
For python instalation can follow the [official installation guide](https://docs.python.org/3/using/windows.html), if python are installed well in Operative system and include a module **pip** can install the pre-requisites with the next steps

#### Scipy
This module is usefull for operations in matrix and use other scientific tools, can install very simply using pip with the next command.

```bat
pip install scipy
```

Also can follow the [Offical installation guide](https://www.scipy.org/install.html)

#### Numpy 
This module provides a matrix managament with high performance, provides some tools for linear algebra, this is used in some graph algorithms, can install very simply using pip with the next command.

```bat
pip install numpy
```

Also can follow the [Offical webpage](https://numpy.org/) and go to instalation guide of **scipy**

#### Matplotlib
Provides all about drawing graphs including coloring, sclaing, export images, can install very simply using pip with the next command.

```bat
pip install matplotlib
```

Also can follow the [Offical installation guide](https://matplotlib.org/users/installing.html) and go to instalation guide of **matplotlib**

#### PyGraphviz
This module provide tools for drawing with GraphViz, is usefull about format and position of nodes specially in certain trees, remember that require alredy installed [Graphviz](http://graphviz.org/) in your system. For install python module can install with pip (official python version) but is probably in windows make a error, so i recomend to use a unofficial binarie of *CristiFati* can download [here](https://github.com/CristiFati/Prebuilt-Binaries/tree/master/Windows/PyGraphviz), when already download to install with pip use the next command:
```bat
pip install pygraphviz-1.5-cp37-cp37m-win_amd64.whl
```

Make sure so the file are in the folder after to execution (probably require a path of Graphviz such as *C:\Program Files (x86)\Graphviz2.38\bin*), is **your responsability** use this unnoficial python module.

# Data structure in networkx (representation)
Based on concept of graphs, nodes and edges on programing can make a data structure for graph representation, here the implementations are in python languague and use module Networkx for that reason the estructure is the most appropriate for the module.

## Nodes
The module networkx work with diferents data structure of python but the most simply usage is with lists, in the case of nodes the representation is a list where each element is a sub-list this sub-lists have node identifier and set initial features, the structure of *nodesList* in python follow the next code:

```python
nodesList=[
    ["name 1", {"feature 1":"value", "feature 2":"value", ... "feature n":"value"}],
    ["name 2", {"feature 1":"value", "feature 2":"value", ... "feature n":"value"}],
    ...
    ["name n", {"feature 1":"value", "feature 2":"value", ... "feature n":"value"}]
]
```

The first element of each sub-list is a node identifier this can be a integer or string with node identifier can modify or get data from features of certain node, the second element of each sub-list is features of node this used for manage a custom drawing (color, position) and can use features such as others values that want store in node (usefull for complementary analysis such as in a city exist data about population, weather, altitude, and more so are usefull for develoment and performance in algoritms) the features can be named with any name (some names are used in functions of module).

## Edges
To represent Edges the simply data structure is a list where each element is a sub-list this sub-lists have a start node, end node and set initial features (similary to nodes list), the structure of *edgesList* in python follow the next code:

```python
edgesList=[
    ["node start 1", "node to 1"{"feature 1":"value", "feature 2":"value", ... "feature n":"value"}],
    ["node start 2", "node to 2"{"feature 1":"value", "feature 2":"value", ... "feature n":"value"}],
    ...
    ["node start n", "node to n"{"feature 1":"value", "feature 2":"value", ... "feature n":"value"}],
```

The first element of each sub-list is a node where edge starts, second element of each sub-list is a node where edge ends and the third element of each sub-list is features of edge this is used for manage a custom drawing (color, position) and can use features such as values in edge weight, capacity and more (can have 1, all or 0 features).

# Topics and algorithms
* [Getting started](/Getting&#32;started&#32;with&#32;graphs)