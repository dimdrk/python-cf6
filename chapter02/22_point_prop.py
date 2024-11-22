import math

class Point:
    __count = 0     # class variable

    def __init__(self, x=0, y=0):
        self.__x = x                # **Before Python 3.13** _x -> protected   __x -> NameMangling _Point__x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return f"({self.__x}, {self.__y})"              # for users
    
    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"     # for programmers, when no __str__, is using __repr__
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Point):
            return self.__x < other.__x and self.__y < other.__y
        else:
            return False

    @classmethod
    def get_count(cls):
        return cls.__count
    
    # Properties
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        # if x < 0:             # can add logic
        #     self.__x = 0
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @x.setter
    def y(self, y):
        self.__y = y

def main():
    p1 = Point(10, 20)
    p2 = Point()

    p2.x = 11
    p2.y = 22

    print(p1)
    print(p2)
    print(p1 == p2)
    # print(Point.get_count())

    print(repr(p1))

    print(p1 < p2)

if __name__ == "__main__":
    main()