from typing import TypeVar

# Declare Generic Type Variable
T = TypeVar('T')

Number = TypeVar("Number", int, float)

def add_numbers(a: Number, b: Number) -> Number:
    """
    Adds two numbers (int or float) and returns the result.

    Args:
        a (Number): The first number.
        b (Number): The second number.

    Returns:
        Number: The sum of two numbers.
    """
    return a + b

def main():
    int_sum = add_numbers(10, 20)
    print(f"int_sum: {int_sum}")

    float_sum = add_numbers(5.2, 2.3)
    print(f"float_sum: {float_sum}")

    mixin_sum = add_numbers(10.2, 15)
    print(f"mixin_sum: {mixin_sum}")

    fail_sum = add_numbers("Hello", " CF6")     # works... 

if __name__ == "__main__":
    main()