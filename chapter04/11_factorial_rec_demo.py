def factorial(n: int) -> int:
    if n < 0: return 0
    if n in (0,1): return 1
    return n * factorial(n - 1)

def main():
    n = int(input("Enter a positive integer to find its factorial: "))
    print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()