def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    fib = fibonacci()

    for i in range(10):
        print(f"Fib({i}) = {next(fib)}")

    new_fibo = fibonacci()

    fib_list_15 = [next(new_fibo) for _ in range(15)]
    print(fib_list_15)

if __name__ == '__main__':
    main()