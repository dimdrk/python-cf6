# Popoulate dictionary (dict)
products = {
    1: "apples",
    2: "bananas",
    3: "honey",
    4: "melons"
}

print("Initial products: ", products)

# Insert a new product
products[15] = "oranges"
print("Products after insertion:", products)

# Get the product with id: 3
print(products[3])

# Update
products[2] = "milk"
print("Products after update:", products)

# Delete
# del products[100]             # if not found -> keyError                
# print("Products after deletion:", products)

removed_product = products.pop(100, "Not found")       # products.pop(100) -> keyError
print(f"Removed product: {removed_product}")
print("Products after deletion:", products)

# popitem() remove 'last item
# product = products.popitem()
# print(product)
# print(type(product))

key, value = products.popitem()
print(f"{key} : {value}")
print(products)

key_to_check = 2

if key_to_check in products:
    print(f"{key_to_check} exists.")
else:
    print(f"{key_to_check} doesn't exist.")

#Get keys from a dictionary
for key in products.keys():
    print(key)

#Get values from a dictionary
for value in products.values():
    print(value)

#iterate a dictionary
for key in products.keys():
    print(f"{key} : {products[key]}")

print("--------------------------")
for key, value in products.items():
    print(f"{key} : {value}")