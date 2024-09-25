def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
