def my_add(a: int, b: int, c: int = 0) -> int:
    """
    Calculate the sum of two or three integers.

    Parameters:
        a (int): The first number to add.
        b (int): The second number to add.
        c (int, optional): The third number to add, defaults to 0 if not provided.

    Returns:
        int: The sum of provided numbers
    """    
    return a + b + c

def my_add2(a: int = 0, b: int = 0, c: int = 0) -> int:
    return a + b + c

def main():
    print(f"my_add(10, 20): {my_add(10, 20)}")
    print(f"my_add(10, 20, 30): {my_add(10, 20, 30)}")

    print(my_add2())
    print(my_add2(100))
    print(my_add2(100, 200))


    print(my_add2(c=100))


if __name__ == "__main__":
    main()