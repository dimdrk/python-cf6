def facto():
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    # Create a generator object for factorials
    f = facto()

    for i in range(7):
        print(f"{i}! = {next(f)}")

    print(next(f))

if __name__ == '__main__':
    main()