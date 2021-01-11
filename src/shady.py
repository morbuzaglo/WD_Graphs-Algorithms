from NodeData import NodeData
import copy


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






if __name__ == '__main__':
    #check_node()
    check_geolocation()
