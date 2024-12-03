c= 'athens'
print(c.title())    # Athens

# list of cities
cities = ["london", "paris", "barcelona", "athens"]

# titled cities
cap_cities = list(map(lambda city: city.title(), cities))

print("cap cities:", cap_cities)       # ['London', 'Paris', 'Barcelona', 'Athens']

cap_cities2 = [city.title() for city in cities]
print("cap cities 2:", cap_cities2)
