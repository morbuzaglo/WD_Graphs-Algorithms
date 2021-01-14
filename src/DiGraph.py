import copy
import random

from src.GraphInterface import GraphInterface

random.seed(11)
"""This abstract class represents an interface of a graph."""


class DiGraph(GraphInterface):

    def __init__(self):
        self.__v = {}
        self.__e = {}  # {key: ({neis out},{neis in}, ...)
        self.__mc = 0

    def v_size(self) -> int:
        return len(self.__v)

    """
            Returns the number of vertices in this graph
            @return: The number of vertices in this graph
    """

    def e_size(self) -> int:
        s = 0
        for val in self.__e.values():
            s = s + len(val[0])
        return s

    """
            Returns the number of edges in this graph
            @return: The number of edges in this graph
    """

    def get_mc(self) -> int:
        return self.__mc

    """
           Returns the current version of this graph,
           on every change in the graph state - the MC should be increased
           @return: The current version of this graph.
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.__v.get(id1) is None or self.__v.get(id2) is None:
            return False
        elif (self.__e.get(id1)[0]).get(id2) is not None:
            return False
        else:
            (self.__e.get(id1)[0]).update({id2: weight})
            (self.__e.get(id2)[1]).update({id1: weight})

            self.__mc = self.__mc + 1
            return True

    """
            Adds an edge to the graph.
            @param id1: The start node of the edge
            @param id2: The end node of the edge
            @param weight: The weight of the edge
            @return: True if the edge was added successfully, False o.w.
            Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.__v.get(node_id) is not None:
            return False
        if pos is None:
            x = random.uniform(0.0, 100.0)
            y = random.uniform(0.0, 100.0)
            z = 0.0
            pos = (x, y, z)

        self.__v.update({node_id: pos})
        self.__e.update({node_id: ({}, {})})
        self.__mc = self.__mc + 1
        return True

    """
            Adds a node to the graph.
            @param node_id: The node ID
            @param pos: The position of the node
            @return: True if the node was added successfully, False o.w.
            Note: if the node id already exists the node will not be added
    """

    def remove_node(self, node_id: int) -> bool:
        if self.__v.get(node_id) is None:
            return False
        else:
            self.__mc = self.__mc + 1

            e_copy = copy.deepcopy(self.__e)

            for key1 in (e_copy.get(node_id)[0]).keys():
                del ((self.__e[key1])[1])[node_id]

            for key1 in (e_copy.get(node_id)[1]).keys():
                del ((self.__e[key1])[0])[node_id]

            del self.__v[node_id]
            del self.__e[node_id]
            return True

    """
            Removes a node from the graph.
            @param node_id: The node ID
            @return: True if the node was removed successfully, False o.w.
            Note: if the node id does not exists the function will do nothing
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.__v.get(node_id1) is None or self.__v.get(node_id2) is None:
            return False
        elif (self.__e.get(node_id1)[0]).get(node_id2) is None:
            return False
        else:
            del ((self.__e[node_id1])[0])[node_id2]
            del ((self.__e[node_id2])[1])[node_id1]

            self.__mc = self.__mc + 1
            return True

    """
            Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.
            Note: If such an edge does not exists the function will do nothing
    """

    def get_all_v(self) -> dict:
        return self.__v

    """return a dictionary of all the nodes in the Graph, each node is represented using a pair
             (node_id, node_data)
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__e.get(id1)[1]

    """return a dictionary of all the nodes connected to (into) node_id ,
           each node is represented using a pair (other_node_id, weight)
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__e.get(id1)[0]

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
            (other_node_id, weight)
    """

    def get_all_e(self) -> dict:
        return self.__e

    def __str__(self):
        s = f"Directed Graph:\n|V| = {self.v_size()}, |E| = {self.e_size()}\nNode and Edges:\n {self.__e} "
        return s

    def __repr__(self):
        self.__str__()

