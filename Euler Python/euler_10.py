# find the sum of all primes below 2 million

LIMIT = 2000001
primes = set([2])
total = 2


def isPrime(n):
    if n in primes:
        return True
    for prime in primes:
        if n % prime == 0:
            return False
    else:
        primes.add(n)
        return True


for num in range(3, LIMIT, 2):
    if isPrime(num):
        total += num
        print(num)

print(total)
