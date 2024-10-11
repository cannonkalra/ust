from functools import wraps
import sys
import time


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


@timeit
def is_prime_big_o_n(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


@timeit
def is_prime_big_o_root_n(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
    except Exception as e:
        print(f"Please enter an integer: error: {e}")
        sys.exit(1)

    if is_prime_big_o_root_n(n):
        print(f"{n} is prime")

    if is_prime_big_o_n(n):
        print(f"{n} is prime")
