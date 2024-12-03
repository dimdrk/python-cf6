# lamba expretions
# Example: power of a number
# Parameters:
# base (int): The base number to be raised to a power
# exp (int): The expontent idication the power to which the based is raised
# Returns
# The results of raising the 'base' to power of 'exp' (base ^ exp) --> base ** power
def my_pow(base, exp):
    return base ** exp

power_to = lambda base, exp: base ** exp

def main():
    print(my_pow(2, 2))     # 4
    print(power_to(2, 2))   # 4

    print(power_to(2, 10))  # 1024
if __name__ == "__main__":
    main()