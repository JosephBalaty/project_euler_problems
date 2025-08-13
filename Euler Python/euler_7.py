# find the 10,001st prime number.
# check if each number is prime or not. if so, increment the
# prime number counter, until the 10,000st prime number
# is found
COUNT = 10001
num = 2
primes = set()
c = 0
while True:
    for p in primes:
        if num % p == 0:
            break
    else:
        primes.add(num)
        c += 1
        if c == COUNT:
            print(num)
            break
    num += 1
