list_of_ints = [1, 2, 3, 4, 5, 6, 7]

# Use a list comprehension to square each number in the list
squared_list_compr = [number**2 for number in list_of_ints]

print(f"squared_list_compr: {squared_list_compr}")

# Use map with a lambda to sqaure the nums of the list
squared_list_map = list(map(lambda number: number**2, list_of_ints))

print(f"squared_list_map: {squared_list_map}")

def squared_function(num):
    return num ** 2

# list compr with named function and if condition
filtered_nums_list = [squared_function(num) for num in list_of_ints if num % 2 == 0]

print(f"filtered_nums_list: {filtered_nums_list}")

# Using map and filter
filtered_squared_map_list = list(map(lambda num: num ** 2, filter(lambda x: x % 2 == 0, list_of_ints)))
#filtered_squared_map_list = list(squared_function, filter(lambda x: x % 2 == 0, list_of_ints)))
print(f"filtered_squared_map_list: {filtered_squared_map_list}")