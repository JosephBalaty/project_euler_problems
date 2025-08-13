# find a pythagorean triplet in which a+b+c = 1000
# return a*b*c

# brute force
# go through each n^3 loop testing each combination of a, b, and c that equals 1000 and
# satisfies the relationship of the pythagorean theorem.

LIMIT = 998
FLOOR = 1


def pyth():
    for i in range(FLOOR, LIMIT):
        for j in range(i + 1, LIMIT):
            for k in range(j + 1, LIMIT):
                if i + j + k == LIMIT + 2:
                    if i**2 + j**2 == k**2:
                        return i*j*k


print(pyth())
