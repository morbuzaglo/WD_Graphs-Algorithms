Our project
In this project we presents an implementation of a directed weighted graph using Python.

Main algorithms in our project
shortest_path - This method calculate the shortest path from one node to other node, using Dijkstra's algorithm.

connected_component - This merthod finds the Strongly Connected Component(SCC) that node id1 is a part of, return the list of nodes in the SCC.

connected_components - This method finds all the Strongly Connected Component(SCC) in the graph, return the list all SCC.

Dijkstra's Algorithm:
Dijkstra work by getting 2 nodes - source node and destination node. The algorithm should get from the src node to the dest node and go through the nodes with the lowest weight. The algorithm works as follows: We will first initialize all the weights of the nodes to infinity so that we know which node we have not yet updated, and then we set a priority queue that will contain the nodes we will visit and update their weights. we enter the first node and initialize its weight to 0, and all the other nodes in the graph are initialized to infinity. For the current junction, we will include all its neighbors and update their temporary weights. The weight of each node is updated according to the parent weight of that node plus the distance between them which is the weight on the edge. Then the same node we started with becomes the father of this node and leaves the queue, it is marked as one we have already visited and we will not return to it again. when the algorithm is finished we get the shortest path betweeen these nodes. we get it as shortest_path which give us the actual number it will take to travel from sec to dest. and we get is as shortest_path which will give us the path from src to dest by nodes we have to go.
