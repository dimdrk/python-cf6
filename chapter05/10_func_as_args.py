def calculator(num1, num2, operation):
    try:
        return operation(num1, num2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function taking two arguments.")
        return None

def add(n1, n2):
    return n1 + n2

def subtrack(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divine(n1, n2):
    if n2 == 0:
        raise ValueError("Division by zero is not allowed")
    return n1 / n2

def main():
    print("Addrition", calculator(5, 3, add))               # 8
    print("Subtraction:", calculator(10, 7, subtrack))      # 3
    print("Multiplication:", calculator(5, 3, multiply))    # 15
    print("Division:", calculator(10, 5, divine))           # 2.0

if __name__ == "__main__":
    main()