numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('primes:', primes)
print('not_primes:', not_primes)
