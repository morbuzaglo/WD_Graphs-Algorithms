import unittest

from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


def start_Digraph() -> GraphAlgo:
    graph = DiGraph()
    for i in range(10):
        graph.add_node(i)
    for i in range(10):
        graph.add_edge(0, i, i)
    graph_algo = GraphAlgo(graph)
    return graph_algo


class MyTestCase(unittest.TestCase):

    def test_load_and_save_graph(self):
        file_name = "C:\\Users\\shady\\Documents\\GitHub\\OOP---Python\\data\\G_10_80_1.json"
        new_file_name = "C:\\Users\\shady\\Documents\\GitHub\\OOP---Python\\data\\G_10_80_1_mine.json"
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertEqual(True, graph_algo.load_from_json(file_name))
        self.assertTrue(True, graph_algo.save_to_json(new_file_name))

    def test_shortest_dist_and_path(self):
        graph = GraphAlgo(DiGraph())
        graph.get_graph().add_node(66)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(66, 1, 3)
        graph.get_graph().add_edge(66, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        self.assertEqual(graph.shortest_path(66, 2)[0], 7)
        true_path = [66, 1, 2]
        answer=true_path==graph.shortest_path(66,2)[1]
        self.assertTrue(answer)
    def test_my_plot_graph(self):
        graph_algo=GraphAlgo(DiGraph())
        graph_algo.load_from_json("../data/A1")
        graph_algo.plot_graph()



if __name__ == '__main__':
    unittest.main()
