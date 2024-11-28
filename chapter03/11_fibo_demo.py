def main():
    try:
        num = int(input("Please insert a positive int: "))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number.")
        return
    
    a = 0
    b = 1

    for i in range(2, num + 1):
        temp = a
        a = b
        b = temp + a
    
    print(f"The {num}th of Fibo is: {b}")
    
if __name__ == "__main__":
    main()