import sys
import time


def is_prime_big_o_n(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


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

    t0 = time.time()
    res = is_prime_big_o_root_n(n)
    t1 = time.time()
    print(f"is_prime_big_o_root_n took {t1-t0} seconds")

    t0 = time.time()
    res = is_prime_big_o_n(n)
    t1 = time.time()
    print(f"is_prime_big_o_n took {t1-t0} seconds")

    if res:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
