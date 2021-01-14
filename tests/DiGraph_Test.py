import unittest

from src.DiGraph import DiGraph



def start_Digraph() -> DiGraph:
    graph = DiGraph()
    for i in range(10):
        graph.add_node(i)
    for i in range(10):
        graph.add_edge(0, i, i)
    return graph


class DiGraphTest(unittest.TestCase):

    def test_v_size(self):
        graph = start_Digraph()
        self.assertEqual(10, graph.v_size())
        graph.remove_node(0)
        self.assertEqual(9, graph.v_size())

    def test_e_size(self):
        graph = start_Digraph()
        self.assertEqual(10, graph.e_size())
        graph.remove_node(0)
        self.assertEqual(0, graph.e_size())

    def test_add_edge(self):
        graph = start_Digraph()
        self.assertEqual(10, graph.e_size())
        graph.add_edge(0,1,0)
        self.assertEqual(10, graph.e_size())

    def test_get_mc(self):
        graph = start_Digraph()
        self.assertEqual(20, graph.get_mc())

    def test_add_node(self):
        graph = start_Digraph()
        self.assertEqual(10, graph.v_size())
        graph.add_node(0)
        self.assertEqual(10, graph.v_size())













if __name__ == '__main__':
    unittest.main()
