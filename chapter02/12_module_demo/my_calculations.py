num1 = 100

def my_add_function(n, m):
    return n + m

def main():
    print("Value of num1:", num1)
    result = my_add_function(50, 75)
    print("Result:", result)
    print(__name__) # ?__main__?

if __name__ == "__main__":  # __name__ != __main__ when the module is imported
    main()