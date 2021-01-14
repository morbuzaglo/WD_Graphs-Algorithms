import unittest
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from timeit import default_timer
import networkx as nx


def shortest_path(file_name):
    g = DiGraph()
    graph_algo = GraphAlgo()
    graph_algo.load_from_json(file_name)
    start = default_timer()
    print('file name: ', file_name)
    d=graph_algo.shortest_path(0, 5)
    end = default_timer()
    print("my time = ", end - start)
    print("our diatnce :",d[0])
    graph_nx = nx.DiGraph()
    for keys in graph_algo.get_graph().get_all_v().keys():
        graph_nx.add_node(keys)
    for keys in graph_algo.get_graph().get_all_e().keys():
        for keys_out in graph_algo.get_graph().all_out_edges_of_node(keys).keys():
            w = graph_algo.get_graph().all_out_edges_of_node(keys).get(keys_out)
            graph_nx.add_edge(keys, keys_out, weight=w)
    start = default_timer()
    d=nx.dijkstra_path_length(graph_nx, 0, 5)
    end = default_timer()
    print("nx time = ", end - start)
    print("nx diatnce :",d)



def connected_components(file_name):
    g = DiGraph()
    graph_algo = GraphAlgo()
    graph_algo.load_from_json(file_name)
    start = default_timer()
    print('file name: ', file_name)
    graph_algo.connected_components()
    end = default_timer()
    print("my time = ", end - start)
    graph_nx = nx.DiGraph()
    for keys in graph_algo.get_graph().get_all_v().keys():
        graph_nx.add_node(keys)
    for keys in graph_algo.get_graph().get_all_e().keys():
        for keys_out in graph_algo.get_graph().all_out_edges_of_node(keys).keys():
            w = graph_algo.get_graph().all_out_edges_of_node(keys).get(keys_out)
            graph_nx.add_edge(keys, keys_out, weight=w)
    start = default_timer()
    nx.strongly_connected_components(graph_nx)
    end = default_timer()
    print("nx time = ", end - start)


def connected_component(file_name):
    graph = GraphAlgo()
    graph.load_from_json(file_name)
    print(file_name)
    start = default_timer()
    graph.connected_component(0)
    end = default_timer()
    print("time = ", end - start)


class MyTestCase(unittest.TestCase):

    def test_shortest_path(self):
        print("shortest path-----------------------------")
        shortest_path('../data/G_10_80_1.json')
        shortest_path('../data/G_100_800_1.json')
        shortest_path('../data/G_1000_8000_1.json')
        shortest_path('../data/G_10000_80000_1.json')
        shortest_path('../data/G_20000_160000_1.json')
        shortest_path('../data/G_30000_240000_1.json')


    def test_conenected_components(self):
        print("connected components-------------------------------")
        connected_components('../data/G_10_80_1.json')
        connected_components('../data/G_10_80_1.json')
        connected_components('../data/G_1000_8000_1.json')
        connected_components('../data/G_10000_80000_1.json')
        connected_components('../data/G_20000_160000_1.json')
        connected_components('../data/G_30000_240000_1.json')


    def test_conenected_component(self):
        print("connected component -------------------------------")
        connected_component('../data/G_10_80_1.json')
        connected_component('../data/G_100_800_1.json')
        connected_component('../data/G_1000_8000_1.json')
        connected_component('../data/G_10000_80000_1.json')
        connected_component('../data/G_20000_160000_1.json')
        connected_component('../data/G_30000_240000_1.json')


if __name__ == '__main__':
    unittest.main()
