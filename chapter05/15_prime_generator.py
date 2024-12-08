def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def main():
    primes = prime_generator()

    for _ in range(25):
        print(next(primes))

if __name__ == '__main__':
    main()