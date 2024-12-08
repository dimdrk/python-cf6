# yield: converts a simple function into genarator
# yield: returns a generator object


def simple_genarator():
    print("First value")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

def main():
    gen = simple_genarator()
    print(next(gen))
    print("-----------------")
    print(next(gen))
    print("-----------------")
    print(next(gen))

if __name__ == '__main__':
    main()