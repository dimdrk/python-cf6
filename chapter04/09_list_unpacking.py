# Populate a list
my_list = [1, 2, 3, 4, 5]

# Simple unpacking all of the elements
a, b, c, d, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Using the _ as placeholder (for unused elements)
a1, _, c1, _, e1 = my_list

print(f"Unpacked values after skipping some values: a={a1}, c={c1}, e={e1}")

# Unpacking the first element, capturing the rest (in a list)
a2, *rest = my_list
print(f"First element: a2={a2}, Remaining elements: rest={rest}")

# Unpacking last element, capturing the rest (in a list)
*start, z = my_list
print(f"Last element: z={z}, Remaining elements: start={start}")

# Unpacking the first and the last element, the rest capturing in a list
first, *middle, last = my_list
print(f"First element: first={first}, Middle elements: middle={middle}, Last element: last={last}")

try:
    a, b, c, d, e = my_list
    print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")
except ValueError as ve:
    print("Error:", ve)

my_list = [1, 2]    # = [1] -> raises error
# Unpacking 1st and 2nd element, capturing the rest elements in a list
a1, b1, *rest = my_list
print(a1, b1, rest)     # 1, 2, []