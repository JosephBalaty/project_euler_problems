LIMIT = 10000
total = 0
# use a set to verify if a number has been seen already.
s = set()

for num in range (2, LIMIT):
    total_d = 0
    curtotal = 0
    if num not in s:
        for d in range(1, num//2 + 1):
            if num%d == 0:
                total_d += d
        for d in range(1, total_d//2 + 1):
            if total_d%d == 0:
                curtotal += d
        if curtotal == num and num != total_d:
            print(f'Amicable number pair: {num}, {total_d}')
            total = total + total_d + num
            s.add(total_d)
            s.add(num)
    
print(total)