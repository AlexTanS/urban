numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for n in numbers:
    is_prime = True
    if n == 0 or n == 1:
        continue
    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)

print(primes)
print(not_primes)
