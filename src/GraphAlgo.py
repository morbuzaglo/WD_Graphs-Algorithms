import copy
import json
import math

import matplotlib.pyplot as plt
from typing import List

from src import GraphInterface

"""This abstract class represents an interface of a graph."""
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None) -> None:
        if graph is not None:
            self.graph = graph
        else:
            self.graph = None

    def get_graph(self) -> GraphInterface:
        return self.graph

    """
            :return: the directed graph on which the algorithm works on.
    """

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            new_graph = DiGraph()
            f = open(file_name, "r")
            universe_json = f.read()
            f.close()
            universe_dict = json.loads(universe_json)
            all_edges = universe_dict.get("Edges")
            all_nodes = universe_dict.get("Nodes")
            for node in all_nodes:
                if node.get("pos") is not None:
                    new_graph.add_node(node.get("id"), tuple(map(float, node.get("pos").split(','))))
                else:
                    new_graph.add_node(node.get("id"))

            for edge in all_edges:
                new_graph.add_edge(int(edge.get("src")), int(edge.get("dest")), float(edge.get("w")))
            self.graph = new_graph
            return True

    # TODO how to do try and except
    """
            Loads a graph from a json file.
            @param file_name: The path to the json file
            @returns True if the loading was successful, False o.w.
    """

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w') as f:
            if self.graph is not None:
                f = open(file_name, "w")
                edges_list = []
                nodes_list = []
                for keys in self.graph.get_all_e().keys():
                    for keys_out in self.graph.all_out_edges_of_node(keys).keys():
                        temp_edge_dict = {"src": keys, "w": self.graph.all_out_edges_of_node(keys).get(keys_out),
                                          "dest": keys_out}
                        edges_list.append(temp_edge_dict)
                    pos_tuple = self.graph.get_all_v().get(keys)
                    pos_str = ",".join(map(str, pos_tuple))
                    temp_node_dict = {"pos": pos_str, "id": keys}
                    nodes_list.append(temp_node_dict)
                universe = {"Edges": edges_list, "Nodes": nodes_list}
                universe_json = json.dumps(universe)
                f.write(universe_json)
                f.close()
                return True
            else:
                return False

    # TODO how to do try and except
    """
            Saves the graph in JSON format to a file
            @param file_name: The path to the out file
            @return: True if the save was successful, False o.w.
    """

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        t1 = self.graph.get_all_v().__contains__(id1)
        t2 = self.graph.get_all_v().__contains__(id2)

        if t1 is False or t2 is False:
            return float('inf'), []
        elif id1 is id2:
            return 0.0, [id1]

        nodes = self.graph.get_all_v()
        father = {}  # father
        dists = {}
        queue = []

        for key in nodes.keys():
            dists[key] = float('inf')

        queue.append(id1)
        dists[id1] = 0.0
        father[id1] = -1  # STOP condition

        while queue:
            id1 = queue.pop()

            for nei in self.graph.all_out_edges_of_node(id1).keys():
                d1 = dists[id1]
                d2 = self.graph.all_out_edges_of_node(id1).get(nei)

                if dists[nei] > (d1 + d2):
                    dists[nei] = d1 + d2
                    father[nei] = id1
                    queue.append(nei)
        if dists[id2]<float('inf'):
            key = id2
        else:
            key=-1
        paths = []

        while key != -1:
            paths.insert(0, key)
            key = father[key]

        return dists[id2], paths

    """
            Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
            @param id1: The start node id
            @param id2: The end node id
            @return: The distance of the path, a list of the nodes ids that the path goes through
    """

    def connected_component(self, id1: int) -> list:
        if self.graph is None or self.graph.get_all_v().__contains__(id1) is False:
            return []

        comps = self.connected_components()
        des_comp = []

        for comp in comps:
            if comp.__contains__(id1):
                des_comp = comp
                break

        return des_comp

    """
            Finds the Strongly Connected Component(SCC) that node id1 is a part of.
            @param id1: The node id
            @return: The list of nodes in the SCC
            Notes:
            If the graph is None or id1 is not in the graph, the function should return an empty list []
    """

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        else:
            comps = []  # List[list]
            nodes = copy.deepcopy(self.graph.get_all_v())

            while len(nodes) > 1:
                comp = []  # list

                it = nodes.keys().__iter__()
                n1 = it.__next__()

                dists_out = self.dfs(n1)
                dists_in = self.dfs_opp(n1)

                for n in self.graph.get_all_v().keys():
                    if dists_out.__contains__(n) and dists_in.__contains__(n) and nodes.__contains__(n):
                        comp.append(n)
                        del nodes[n]

                comps.append(comp)

            if len(nodes) == 1:
                comp = [nodes.__iter__().__next__()]
                comps.append(comp)

            return comps

    def dfs(self, id1) -> list:

        dists = {}
        queue = [id1]

        dists[id1] = 1

        while queue:
            id1 = queue.pop()

            for nei in self.graph.all_out_edges_of_node(id1).keys():
                if not dists.__contains__(nei):
                    dists[nei] = 1
                    queue.append(nei)

        return dists

    def dfs_opp(self, id1) -> list:

        dists = {}
        queue = []

        queue.append(id1)
        dists[id1] = 1

        while queue:
            id1 = queue.pop()

            for nei in self.graph.all_in_edges_of_node(id1).keys():
                if not dists.__contains__(nei):
                    dists[nei] = 1
                    queue.append(nei)

        return dists

    """
            Finds all the Strongly Connected Component(SCC) in the graph.
            @return: The list all SCC
            Notes:
            If the graph is None the function should return an empty list []
    """

    def plot_graph(self) -> None:
        ax = plt.axes()
        R = min((self.MinMaxPoints()[0][1] - self.MinMaxPoints()[0][0]) / 30.0,
                (self.MinMaxPoints()[1][1] - self.MinMaxPoints()[1][0]) / 30.0)

        for k1 in self.graph.get_all_v().keys():
            for k2 in self.graph.all_out_edges_of_node(k1):

                if k1 == k2:
                    continue

                pos1 = self.graph.get_all_v().get(k1)
                pos2 = self.graph.get_all_v().get(k2)

                x1 = pos1[0]
                y1 = pos1[1]
                x2 = pos2[0]
                y2 = pos2[1]

                alfa = math.atan2(y2 - y1, x2 - x1)
                ax.arrow(x1, y1, x2 - x1 - 2 * R * math.cos(alfa), y2 - y1 - 2 * R * math.sin(alfa), head_width=R / 30, head_length=R, fc='k', ec='k')
                # ax.text((x2 + x1) / 2 - R / 2, (y2 + y1) / 2 + R / 2, f"{self.graph.get_all_e().get(k1)[0].get(k2)}",
                # fontsize=9, color='r')

        for k1 in self.graph.get_all_v().keys():
            pos = self.graph.get_all_v().get(k1)
            circle = plt.Circle((pos[0], pos[1]), R, color='r')
            ax.text(pos[0] - R / 4, pos[1] - R / 4, f"{k1}", fontsize=9, color='w')

            ax.add_artist(circle)

        ax.set(xlim=self.MinMaxPoints()[0], ylim=self.MinMaxPoints()[1])
        plt.show()

    """
            Plots the graph.
            If the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None
    """

    def MinMaxPoints(self) -> ((float, float), (float, float)):  # ((xmin, xmax), (ymin, ymax))
        if self.graph is None or self.graph.v_size() == 0:
            return (None, None), (None, None)
        else:
            xmin = self.graph.get_all_v().values().__iter__().__next__()[0]
            xmax = xmin
            ymin = self.graph.get_all_v().values().__iter__().__next__()[1]
            ymax = ymin

            for n in self.graph.get_all_v().values():
                if n[0] > xmax:
                    xmax = n[0]
                else:
                    if n[0] < xmin:
                        xmin = n[0]

                if n[1] > ymax:
                    ymax = n[1]
                else:
                    if n[1] < ymin:
                        ymin = n[1]

            dx_add = (xmax - xmin) * 0.1
            dy_add = (ymax - ymin) * 0.1

            return (xmin - dx_add, xmax + dx_add), (ymin - dy_add, ymax + dy_add)

    def _str_(self):
        s = "Strongly Connected Components in graph:\n"
        i = 0
        for comp in self.connected_components():
            i = i + 1
            s = s + f"Component {i}: {comp}\n"

        return s

    def _repr_(self):
        return self.__str__()