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
product = products.popitem()
print(product)
print(type(product))

key, value = products.popitem()
print(f"{key} : {value}")
print(products)