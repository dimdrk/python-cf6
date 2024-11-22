# Falsy - Truthy Values
# 0, 0.0, 0j, "", [], {}, (), set(), False, None

empty_dict = {}         # <class 'dict'>
print(type(empty_dict))

# 0 < a < 10
a = 5

if a > 0 and a < 10:
    print("Valid num")

if 0 < a < 10:
    print("Valid num.")

# Challenge
students = ("Alice", "Bob", "Charlie")

students = tuple(["Dimitris"] + list(students)[1:])
print(students)

# enumarate()
students = ["Alice", "Bob", "Charlie", "David"]

for index, value in enumerate(students, start=100):
    print(f"{index} : {value}")

# 100 : Alice
# 101 : Bob
# 102 : Charlie
# 103 : David