import time

def get_time(n):
    start_time = time.perf_counter()  # time.time()     # perf_counter() -> more accurate
    # Make some calculations
    resut = sum(range(n))
    end_time = time.perf_counter()

    print(f"My function took {end_time - start_time: .6f} seconds to run.")
    return resut

def main():
    print(get_time(1_000_000))

if __name__ == '__main__':
    main()