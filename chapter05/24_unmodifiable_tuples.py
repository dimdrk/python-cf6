def main():
    g = 1, 2, 3, 5
    print(f"Type of g: {type(g)}")

    my_tuple = (1, 2, [3, "CF6"], "Hello")

    try:
        my_tuple[2] = 100
    except TypeError as e:
        print("Error", e)

    my_tuple[2][0] = 300
    print("Modified tuple:", my_tuple)

if __name__ == '__main__':
    main()