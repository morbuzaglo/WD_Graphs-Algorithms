import copy
from src.GraphAlgo import GraphAlgo


from src.DiGraph import DiGraph





def check_graph():
    g = DiGraph()
    algo=GraphAlgo(g)

    g.add_node(0, (2.0, 3.0,9))
    g.add_node(1, (1.0, 7.0,9))
    g.add_node(2, (2.0, 6.0,9))
    g.add_node(3, (6.0, 6.0,9))

    g.add_edge(0, 1, 6.0)
    g.add_edge(0, 2, 6.0)
    g.add_edge(0, 3, 6.0)
    g.add_edge(1, 0, 6.0)

    print(g.get_all_e())

    #print("0 is removed? = ", g.remove_node(0))

    print(g.get_all_e())
    print(g.get_all_v())

    print("mc = ", g.get_mc())
    algo.save_to_json("this.JSON")
    algo.load_from_json("this.JSON")
    algo.save_to_json("this1.JSON")






if __name__ == '__main__':
    #check_node()
    #check_geolocation()
    check_graph()
