import random

random_numbers = []

# use for loop to generate 10 random integers
for _ in range(10):                             # when "i" not used in for-  by convention replaced with "_"
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

# last even number of the list
for num in random_numbers:
    if num % 2 == 0:
        even = num
    
print(f"The last item of the list: {num}")
print(f"The last 'even' item of the list: {even}")