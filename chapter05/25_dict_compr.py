numbers = [1, 2, 3, 4, 5]

# Dictionary with keys the values of numbers and values the squared numbers.
squared_dict = { number : number ** 2 for number in numbers }

print(squared_dict)

even_squared_dict = { number : number ** 2 for number in numbers if number % 2 == 0 }
print(even_squared_dict)

def square(number):
    return number ** 2

squared_dict_2 = { number : square(number) for number in numbers }
print(squared_dict_2)