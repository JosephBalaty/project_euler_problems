# find the sum of the square of the differences of the first 100 natural numbers.
# 1, 2, 3, ... 99, 100
# n(n + 1)/2

N = 100

s = N*(N+1)/2
ss = sum([i**2 for i in range(1, N + 1)])
print(int(s*s - ss))
