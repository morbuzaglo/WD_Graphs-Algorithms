import unittest
from src import NodeData



class MyTestCase(unittest.TestCase):

    def test_create_node(self):
        node1 = NodeData(5, 6, 'shady')
        #self.assertEqual(node1.getKey, 0)
        #self.assertEqual(node1.getWeight, 7)



if __name__ == '__main__':
    unittest.main()
