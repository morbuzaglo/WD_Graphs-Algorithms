
from src import NodeData


class NodeData:
    __global_key = 0

    def __init__(self, weight: float, tag: float, info: str, location: tuple = None):
        if location is not None:
            self.__key = NodeData.__global_key
            NodeData.__global_key = NodeData.__global_key + 1
            self.__weight = weight
            self.__tag = tag
            self.__info = info
            self.__location = location
            self.__Neighbors = {}
            self.__Edges={}
        else:
            self.__key = NodeData.__global_key
            NodeData.__global_key = NodeData.__global_key + 1
            self.__weight = weight
            self.__tag = tag
            self.__info = info
            self.__location = (0,0,0)
            self.__Neighbors = {}
            self.__Edges={}

    def getNeis(self)->{}:
        return self.__Neighbors

    def hasNei(self, key: int)->bool:
        x = self.__Neighbors.get(key)
        if x is None:
            return False
        return True

    def addNei(self, nei: NodeData):
        self.__Neighbors.update({nei.__key: nei})

    def getKey(self)->int:

        return self.__key

    def getLoc(self)->tuple:

        return self.__location

    def setLoc(self, location: tuple):

        self.__location = location

    def getWeight(self)->float:

        return self.__weight

    def setWeight(self, weight: float):

        self.__weight = weight

    def getInfo(self)->str:

        return self.__info

    def setInfo(self, Info: str):

        self.__info = Info

    def getTag(self)->float:

        return self.__tag

    def setTag(self, tag: float):

        self.__tag = tag

    def __eq__(self, obj):
        if isinstance(obj, NodeData):
            if obj.__key == self.__key and obj.__weight == self.__weight and obj.__location == self.__location:
                return True
        return False
