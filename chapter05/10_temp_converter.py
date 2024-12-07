def fahrenheit_to_celcius(temp):
    return round((temp - 32) * 5 / 9, 2)

def main():
    fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]
    print("fahrenheit Temperatures:", fahrenheit_temps)

    # Convert temperatures using list comprehension
    celcius_temps_list = [fahrenheit_to_celcius(temp) for temp in fahrenheit_temps]
    print("Celcius temperatures (list comprehension):", celcius_temps_list)

    # Convert temperatures using genarator expression
    celcius_temps_gen = (fahrenheit_to_celcius(temp) for temp in fahrenheit_temps)
    print("Celcius temperatures (genarator expression):", celcius_temps_gen)
    for celcius in celcius_temps_gen:
        print(celcius, end=" ")
    print()

    print("-" * 40)

    # Attention ! 
    for celcius in celcius_temps_gen:
        print(celcius, end=" ")
    print()



if __name__ == "__main__":
    main()