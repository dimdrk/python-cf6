a = True
b = False

print(f"Type of a: {type(a)}, value of a: {a}")
print(f"Type of b: {type(b)}, value of a: {b}")

result = a or b

print(result)

### Out of the box! Deep dive! ###
print("True + true: ", True + True)     # = 2  (True = 1, False = 0)
print(True * 5)                         # = 5