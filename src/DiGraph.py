import copy
import random

from src.GraphInterface import GraphInterface
from src.NodeData import NodeData

random.seed(10)


class DiGraph(GraphInterface):

    def __init__(self):
        self.__v = {}
        self.__e = {}  # {key: ({neis out},{neis in}, ...)
        self.__mc = 0

    def v_size(self) -> int:
        return len(self.__v)

    def e_size(self) -> int:
        s = 0
        for val in self.__e.values():
            s = s + len(val)
        return s

    def get_mc(self) -> int:
        return self.__mc

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

    def remove_node(self, node_id: int) -> bool:
        if self.__v.get(node_id) is None:
            return False
        else:
            self.__mc = self.__mc + len(self.__e.get(node_id)[0]) + len(self.__e.get(node_id)[1]) + 1

            e_copy = copy.deepcopy(self.__e)

            for key1 in (e_copy.get(node_id)[0]).keys():
                del ((self.__e[key1])[1])[node_id]

            for key1 in (e_copy.get(node_id)[1]).keys():
                del ((self.__e[key1])[0])[node_id]

            del self.__v[node_id]
            del self.__e[node_id]
            return True

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

    def get_all_v(self) -> dict:
        return self.__v

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__e.get(id1)[1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__e.get(id1)[0]

    def get_all_e(self) -> dict:
        return self.__e

    def __str__(self):
        pass

