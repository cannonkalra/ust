def is_prime(n):
    factors = 0
    for i in range(2, n):
        if n % i == 0:
            factors += 1
            return False
    if factors == 0:
        return True
    return False


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
