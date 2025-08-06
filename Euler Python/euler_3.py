# find all the primes for 600851475143
# running total ;start with one, and multiply each number that evenly divides
primes = [2, 3]
curnum = 600851475143


def isPrime(num):
    if num in primes:
        return True

    for p in primes:
        if num % p == 0:
            return False
    else:
        primes.append(num)
        return True


max_prime = 0
prime = 2
while curnum > 1:
    while (curnum % prime == 0):
        curnum /= prime
        if prime > max_prime:
            max_prime = prime
    # increment prime to next prime number
    while (True):
        prime += 1
        if isPrime(prime):
            break

print(max_prime)
