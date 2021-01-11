import copy
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph) -> None:
        self.graph = graph
        self.dists = {}

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 is id2:
            return 0.0, [id1]

        t1 = self.graph.get_all_v().__contains__(id1)
        t2 = self.graph.get_all_v().__contains__(id2)

        if t1 is False or t2 is False:
            return float('inf'), []
        else:
            nodes = self.graph.get_all_v()
            paths = {}  # dict[list]
            dists = {}
            queue = []

            for key in nodes.keys():
                dists[key] = float('inf')
                paths.update({key: []})

            queue.append(id1)
            dists[id1] = 0.0
            paths[id1].append(id1)

            while len(queue) != 0:
                id1 = queue.pop()

                for nei in self.graph.all_out_edges_of_node(id1).keys():
                    d1 = dists[id1]
                    d2 = self.graph.all_out_edges_of_node(id1).get(nei)

                    if dists[nei] > (d1 + d2):
                        dists[nei] = d1 + d2
                        paths[nei] = copy.deepcopy(paths[id1])
                        paths[nei].append(nei)
                        queue.append(nei)

        self.dists = dists
        return dists[id2], paths[id2]

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

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        else:
            comps = []  # List[list]
            nodes = copy.deepcopy(self.graph.get_all_v())

            while len(nodes) != 0:
                comp = []  # list
                n = nodes.keys().__iter__().__next__()
                comp.append(n)

                queue = [n]

                while len(queue) != 0:
                    s = queue.pop()
                    del nodes[s]

                    for nei in self.graph.all_out_edges_of_node(s).keys():
                        if nodes.keys().__contains__(nei):
                            queue.append(nei)
                        if comp.__contains__(nei) is False:
                            self.shortest_path(nei, s)

                            comp_copy = copy.deepcopy(comp)
                            b = True
                            for c in comp_copy:
                                if (self.dists[c] < float('inf')) is False:
                                    b = False
                                    queue.remove(nei)
                                    break

                            if b is True:
                                comp.append(nei)

                comps.append(comp)

            return comps

    def plot_graph(self) -> None:
        pass

    def __str__(self):
        pass
