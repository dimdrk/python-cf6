def get_average(*numbers):
    if not numbers:
        return "No numbers provided."
    
    # average = sum(numbers) / len(numbers)
    # return average
    return sum(numbers) / len(numbers)

def main():
    numbers = [10, 20, 12]

    average = get_average(*numbers)     # "*" is mendatory
    print("Average:", average)

    print(get_average())

if __name__ == "__main__":
    main()