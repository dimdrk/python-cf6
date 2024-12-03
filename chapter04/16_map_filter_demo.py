# List of cities
cities = ["london", "paris", "barcelona", "athens", "casablanka"]

# Filter city names (longer than 5 characters)
long_cities = list(filter(lambda city: len(city) > 5, cities))

print(f"long cities: {long_cities}")

# Capitalized cities
cap_cities = list(map(lambda city: city.title(), cities))

print(f"cap cities: {cap_cities}")

# Capitalized all long (more than 5 characters) cities
cap_long_cities = list(map(lambda city: city.title(), long_cities))
long_cap_cities = list(filter(lambda city: len(city) > 5, cap_cities))

cap_length_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

print("Map and Filter together:")
print(cap_length_cities)