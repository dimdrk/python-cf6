# Populate list
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add
fruits.append("Berry")
print("Afrer adding Berry:", fruits)

# Add 2 or more items at the end of the list
fruits.extend(["Grapes", "Fig"])
print("Afrer adding grapes and fig:", fruits)

# insert 1 item in a specific position
fruits.insert(1, "Coconut")
print("Afrer insert coconut at pos 1 (2nd element):", fruits)

# update
fruits[0] = "Melon"
print("After update element at pos 0:", fruits)

# update two elements
fruits[1:3] = ["A", "B"]            # fruits[1:3] = ["A", "B", "C", "D"] -> updates 2 and adds 2 more (no error) 
print("List after update 2 elements", fruits)

#fruits[0] = [1, 2, 3, 4]
#print(fruits)


# Delete
removed_item = fruits.pop(1)
print(f"Removed_item: {removed_item}")
print(fruits)

new_removed_item = fruits.remove("Melon")
print(f"new_removed_item: {new_removed_item}")
print(fruits)

# remove a fantastic item
#fruits.remove("exotic_fruit")   # ValueError
#print(fruits)

if new_removed_item in fruits:
    print(f"{new_removed_item} removed.")
else:
    print(f"{new_removed_item} doesn't exist.")

# Search
pos = fruits.index("Berry")
print(f"In position: {pos} exists {fruits[pos]}")