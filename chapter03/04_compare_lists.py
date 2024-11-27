def compare_lists(list1, list2):

    print(f"{list1} is {list2}: {list1 is list2}")  # compares the Id
    print(f"{list1} == {list2}: {list1 == list2}")  # compares the Values


def main():
    my_list = [1, 2 ,3]
    your_list = [1, 2, 3]

    compare_lists(my_list, your_list)

if __name__ == "__main__":
    main()