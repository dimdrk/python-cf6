from collections import deque

def display_garage(garage: deque) -> None:
    """
    Dispalys the current state of the garage.

    Params:
        garage (deque): The deque representation of the garage.
    
    Returns:
        None
    """
    if garage:
        print("Current cars in the garage:")
        for i, car in enumerate(garage, 1):
            print(f"{1}. {car}")
    else:
        print("\nGarage is empty.")
    
def add_car_to_garage(garage: deque, max_capacity: int) -> None:
    """
    Add a car to the garage if there is free space.

    Params:
        garage (deque): The deque representing the garage.
        max_capacity (int): The maximum number of the cars the garage can hold.

    Returns:
        None
    """
    if len(garage) < max_capacity:
        car_name = input("Enter the id of the car: ")
        garage.append(car_name)
        print(f"{car_name} has entered the garage.")
    else:
        print("The garage is full! Cannot add more cars.")

def remove_car_from_garage(garage: deque) -> None:
    """
    Removes the first car from the garage if it is not empty.

    Params:
        garage (deque): The deque represents the garage.

    Returns:
        None
    """
    if garage:
        car_left = garage.popleft()
        print(f"{car_left} left from the garage.")
    else:
        print("Garage is empty! No cars to remove!")

def main():
    garage = deque()
    max_capacity = 5

    while True:
        print("\nOptions")
        print("1. Add a car to the garage.")
        print("2. Remove the first car from the garage.")
        print("3. Display the garage state.")
        print("4. Exit.")

        try:
            choice = int(input("Please give your choice (1-4): "))
        except ValueError:
            print("Invalid input.")
            continue

        match choice:
            case 1:
                add_car_to_garage(garage, max_capacity)
            case 2:
                remove_car_from_garage(garage)
            case 3:
                display_garage(garage)
            case 4:
                print("Goodbye")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()