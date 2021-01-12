import copy
from typing import List
import json

import self as self

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph) -> None:
        self.graph = graph
        self.dists = {}

    def load_from_json(self, file_name: str) -> bool:
        new_graph=DiGraph()
        f = open(file_name, "r")
        universe_json=f.read()
        f.close()
        universe_dict=json.loads(universe_json)
        all_edges=universe_dict.get("Edges")
        all_nodes=universe_dict.get("Nodes")
        for node in all_nodes:
            if node.get("pos") is not None:
                new_graph.add_node(node.get("id"),tuple(map(float,node.get("pos").split(','))))
            else:
                new_graph.add_node(all_nodes[node].get("id"))

        for edge in all_edges:
            new_graph.add_edge(int(edge.get("src")),int(edge.get("dest")),float(edge.get("w")))
        self.graph=new_graph
        return True
    #TODO how to do try and except




    def save_to_json(self, file_name: str) -> bool:
        f = open(file_name, "w")
        edges_list = []
        nodes_list = []
        for keys in self.graph.get_all_e().keys():
            for keys_out in self.graph.all_out_edges_of_node(keys).keys():
                temp_edge_dict={"src":keys,"w":self.graph.all_out_edges_of_node(keys).get(keys_out),"dest":keys_out}
                edges_list.append(temp_edge_dict)
            pos_tuple = self.graph.get_all_v().get(keys)
            pos_str = ",".join(map(str,pos_tuple))
            temp_node_dict = {"pos": pos_str, "id": keys}
            nodes_list.append(temp_node_dict)
        universe={"Edges":edges_list,"Nodes": nodes_list}
        universe_json=json.dumps(universe)
        f.write(universe_json)
        f.close()
        return True
    #TODO how to do try and except







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
