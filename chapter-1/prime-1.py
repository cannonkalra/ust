def prime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")


prime(24104567)
