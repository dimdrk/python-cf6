# Populate a list
ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

print("\nIterating with index and value:")
for index, value in enumerate(ages):    # (index, value) -> Πλιάδες
    print(f"Index: {index}, Value: {value}")

print("\nIterate with enchanced for")
for age in ages:
    print(age, end=" ")
print()