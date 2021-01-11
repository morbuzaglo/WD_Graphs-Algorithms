from NodeData import NodeData
import copy

from src.DiGraph import DiGraph


def check_node():
    node1 = NodeData(5, 6, 'shady')
    x=node1.getKey()
    print(node1.getKey())
    print(node1.getWeight())
    node2 = NodeData(5, 6, 'shady')
    node3 = NodeData(5, 6, 'shady')
    node4 = NodeData(5, 6, 'shady')
    node1.addNei(node2)
    node1.addNei(node3)
    node1.addNei(node3)
    print(node2.getKey())
    print(node1.getNeis())
    print(node1.hasNei(node4.getKey()))
    print(node1.getNeis())


def check_geolocation():
    node1 = NodeData(5, 6, 'shady',(0,1,2))
    node2=NodeData(5, 6, 'shady')
    print(node1.getLoc())
    print(node2.getLoc())
    node2.setLoc((2,7.5,9))
    print(node2.getLoc())


def check_graph():
    g = DiGraph()

    g.add_node(0, (2.0, 3.0))
    g.add_node(1, (1.0, 7.0))
    g.add_node(2, (2.0, 6.0))
    g.add_node(3, (6.0, 6.0))

    g.add_edge(0, 1, 6.0)
    g.add_edge(0, 2, 6.0)
    g.add_edge(0, 3, 6.0)
    g.add_edge(1, 0, 6.0)

    print(g.get_all_e())

    print("0 is removed? = ", g.remove_node(0))

    print(g.get_all_e())
    print(g.get_all_v())

    print("mc = ", g.get_mc())





if __name__ == '__main__':
    #check_node()
    #check_geolocation()
    check_graph()
