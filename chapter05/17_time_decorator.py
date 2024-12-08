import time

def timer_decorator(func):
    def inner_function(*args, **kwargs):
        start_time = time.perf_counter()

        # Make some calculations
        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return inner_function

def sum_function(n):
    return sum(range(n))

# Decorate the sum_function manually
sum_function = timer_decorator(sum_function)
print(sum_function(1_000_000))

@timer_decorator
def average_function(n):
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_function(100))

@timer_decorator
def reverse_string(s):
    return "".join(reversed(s))

print(reverse_string("Coding Factory"))