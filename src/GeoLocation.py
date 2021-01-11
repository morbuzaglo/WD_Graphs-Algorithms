from src import GeoLocation

class GeoLocation:

    """
    This class is responsible to represents the set coordinates applicable on
    nodes in a (directional) weighted graph.
    """

    def __init__(self, x: float = None, y: float = None, z: float = None):
            self.__x = x
            self.__y = y
            self.__z = z

    def setx(self, x: float):
        self.__x=x

    def sety(self, y: float):
        self.__y=y

    def setz(self, z: float):
        self.__z=z

    def getx(self) -> float:
        """
        This function is responsible to return the X coordinate associated with this location.
        @:return the X coordinate associated with this location.
        """
        return self.__x

    def gety(self) -> float:
        """
        This function is responsible to return the Y coordinate associated with this location.
        @:return the Y coordinate associated with this location.
        """
        return self.__y

    def getz(self) -> float:
        """
        This function is responsible to return the Z coordinate associated with this location.
        @:return the Z coordinate associated with this location.
        """
        return self.__z

    def __str__(self):
        """
        This function is responsible to return the coordinates in a string format.
        @return the coordinates in a string format.
        """
        return "X: %f, Y: %f, Z: %f" % (self.__x, self.__y, self.__z)

    def __repr__(self):
        return str(self)