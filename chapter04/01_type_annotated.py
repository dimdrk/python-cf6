def my_add(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers and returns the result.
    
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.

    Returns:
        int | float: The sum of a and b.
    """
    # if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
    if not (isinstance(a, int | float) and isinstance(b, int | float)):
        raise TypeError("Both a and b must be integers or floats")
    return a + b

def main():
    # Testing my_add functions
    print(my_add(10, 20))
    print(my_add(3.14, 1.617))
    print(my_add(10, 15.2))
    print(my_add(17.3, 3))

    try:
        print((my_add("Hello", " Friends!")))
    except TypeError as e:
        print(e)

    print("---------------------------------------")
    print("Annotations:", my_add.__annotations__)
    print("Docs:", my_add.__doc__)
    print("---------------------------------------")
    help(my_add)
    print("---------------------------------------")
    help(print)

if __name__ == "__main__":
    main()