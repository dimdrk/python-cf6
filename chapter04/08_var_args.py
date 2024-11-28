def my_add(*args: int) -> int:
    """
    Calculate the sum of an arbitrary number of integers.

    Parameters:
        *args (int): A variable-length argument list of integers

    Returns:
        int: The sum of provided integers.
    """
    return sum(args)

def my_average(*args: int) -> float:
    """
    Calculate the average of an arbitrary number of integers.

    Parameters:
        *args (int): A variable-length argument list of integers

    Returns:
        float:  The average of provided integers. 
                Returns 0 if no agruments are provided to void dicision by 0.
    """
    if not args:
        return 0
    return sum(args) / len(args)

def main():
    ages = [27, 35, 38, 18, 22, 26]
    
    print("Average age:", my_average(*ages))
    print("Average age:", my_average(30, 15))


if __name__ == "__main__":
    main()
