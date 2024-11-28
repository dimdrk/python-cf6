from typing import List, Any

my_list = [1, 2, "Hello", [3, 4, 5]]

def append_to_list(li: List[Any], element: Any) -> None:
    """
    Appends an element to the provided list.

    Parameters:
        li (List[Any]): The list which the element will be appended.
        element (Any): The element to append to the list.
    """
    li.append(element)

def main():
    append_to_list(my_list, "CF6")
    print(my_list)

if __name__ == "__main__":
    main()