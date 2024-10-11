from functools import wraps
from concurrent.futures import ProcessPoolExecutor
import time


N = 6


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start timing
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.perf_counter()  # End timing
        total_time = end_time - start_time  # Calculate elapsed time
        print(
            f"Function {func.__name__}{args} {kwargs} took {total_time:.4f} seconds, result: {result}"
        )
        return result  # Return the result of the function

    return timeit_wrapper


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@timeit
def nth_prime(n):
    counter = 0
    current_number = 1
    while counter != n:
        if is_prime(current_number):
            counter += 1
            result = current_number
        current_number += 1
    return result


@timeit
def parallel_processing(nth):
    with ProcessPoolExecutor() as executor:
        results = executor.map(nth_prime, range(nth, nth + N))
        return list(results)
    # with ThreadPoolExecutor(max_workers=N) as executor:
    #     results = executor.map(nth_prime, range(nth, nth + N))
    #     return list(results)


@timeit
def serial_processing(nth):
    return list(map(nth_prime, range(nth, nth + N)))


if __name__ == "__main__":
    nth = 90_000
    # serial_processing(nth)
    parallel_processing(nth)
