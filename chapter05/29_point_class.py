class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y + other)
        else:
            raise TypeError(f"Unsupported operand types for '+'")
        
    def __radd__(self, other):
        return self.__add__(other)
        
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print("p1 + p2 =", p1 + p2)                     # p1 + p2 = (4, 6)
    print("p1 + 10 =", p1 + 10)                     # p1 + 10 = (11, 12)
    print("Sum([p1, p2]) =", sum([p1, p2]))         # Sum([p1, p2]) = (4, 6)   (without radd -> TypeError!)
    print("p1 == Point(1, 2):", p1 == Point(1, 2))  # p1 == Point(1, 2): True
    print("p1 == 'Hello':", p1 == 'Helllo')         # p1 == 'Hello': False

    print("p1.x =", p1.x)                           # p1.x = 1
    p1.x = 100
    print(p1)                                       # (100, 2)

    print("10 + p1 =", 10 + p1)                     # 10 + p1 = (110, 12)  (without radd -> TypeError!)


if __name__ == '__main__':
    main()