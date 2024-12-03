def fibo(n: int) -> int:
    # base cases: fibo(0) = 0, fibo(1) = 1
    if n in (0,1): return n
    # Recursive case: fibo(n) = fibo(n - 1) + fibo(n - 2)
    return fibo(n - 1) + fibo(n - 2)

def main():
    n = int(input("Enter a positive integer to find its fibo: "))
    print(f"fibo{n} = {fibo(n)}")


if __name__ == "__main__":
    main()