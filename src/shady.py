from NodeData import NodeData
from GeoLocation import GeoLocation


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
        geo1=GeoLocation(1, 2, 3)
        geo2=GeoLocation("1.1,2.2,3.3")
        geo3=GeoLocation(geo1)
        s="1.1,2.2,3.3"
        pos=s.split(',')
        x=pos.pop()
        node1 = NodeData(5, 6, 'shady',geo1)
        print(node1.getLoc())
        node1.setLoc(geo2)
        print(geo3.gety())
       # print(pos)



if __name__ == '__main__':
    #check_node()
    check_geolocation()
