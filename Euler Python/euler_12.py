# find the first triangular number with more than 500 divisors.
#   calculate the next triangle number in the sequence.
#   find the number of divisors within a number.

# find divisors.

def findDivisors(tri_num):
    limit = pow(tri_num, 0.5)
    n = 1
    count = 0
    while n < limit:
        if tri_num % n == 0:
            count += 2
        n += 1
    if n == limit:
        count += 1
    # print(tri_num, count)
    return count


tn = 0
count = 1
while True:
    # find each consecutive triangular number,
    # and then the number of its divisors.
    tn += count
    count += 1
    divisor_nums = findDivisors(tn)
    if divisor_nums > 500:
        print(f'Final result: {tn}')
        break
