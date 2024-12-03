from functools import reduce

n = int(input("Please give an int: "))

print(f"Facto of {n} calculations:")

result = reduce(lambda x, y: x * y, range(1, n + 1))

print(f"{n}! = {result}")