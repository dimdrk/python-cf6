students = ("Alice", "Bob", "Charlie")
# students = "Alice", "Bob", "Charlie"      # same

print(type(students))

# Iterate
for index, student in enumerate(students):
    print(f"{index}: {student}")

# Enhanced for
for student in students:
    print(student)

# first_st = students[0]
# second_st = students[1]
# third_st = students[2]

# first_st, second_st, third_st = "Alice", "Bob", "Charlie"
# first_st, second_st, third_st = students[0], students[1], students[2]
# first_st, second_st, third_st = students[0:3]
first_st, second_st, third_st = students                # unpacking

print(f"first_st: {first_st}")
print(f"second_st: {second_st}")
print(f"third_st: {third_st}")

# students[0] = "Panagiotis"      # Unmodifiable - TypeError
students = list(students)
students[0] = "Panagiotis"
students = tuple(students)

# one line change (challenge!) -> 13_demo.py

print(students)
print(type(students))

