# OOP - DIRECTED WEIGHTED GRAPH -> in PYTHON!
As a part of the "Object Oriented Programming", we created a project the implements the ideas and algorithms on directed weighted graph. the purpose is to expirience with python, and compare our results to "NetworkX" (python) library and to our java code that implements the same ideas.
## MAIN STRUCTURES:
##DIGRAPH:
- we have deviced a graph structure which contains everything in a single class. while the nodes and edges are are mere tuples and dictionaries but the graph itself is a novel object of our creation
note: we didnt have to create a copy function for DIgraph since our graph is built from basic python friendly strucures which are already accustomed to the deep copy function of the built in copy class
##GraphAlgo:
- its a graph based algorthim object which we run our 3 mmain algorithims on it.
## MAIN ALGORITHMS:
- `shortest_path` - returns (float, list), float -> the shortest distance from one node to another, list -> of the nodes in the way on the shortest path.

- `connected_component` - returns a list the contains all the nodes that on the same SCC of a specific nodes.

- `connected_components` - returns all the SCC lists in the graph.

In the wiki page yo can see the comparations between our java, our pyhton and the NetworkX library.
