def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b         # a <- b && b <- a+b
    return b

def main():
    try:
        num = int(input("Please insert a positive int: "))
        if num < 0:
            raise ValueError
    except ValueError:
        print("Invalid number.")
        return
    
    result = fibonacci(num)
    
    print(f"The {num}th of Fibo is: {result}")

if __name__ == "__main__":
    main()