NUM_LIMIT = 20
# have a dictionary which keeps track of the counts of each prime
# needed to make the numbers from 1 to NUM_LIMIT be a divisor of
# the smallest number.

final_num = {}


def rng():
    for num in range(2, NUM_LIMIT + 1):
        if num not in final_num:
            for p in final_num:
                count = 0
                if num % p != 0:
                    continue
                else:
                    while num % p == 0:
                        count += 1
                        num /= p
                    if final_num[p] < count:
                        final_num[p] = count
                if num == 1:
                    break
            else:
                final_num[num] = 1


rng()
res = 1
for num in final_num:
    res *= pow(num, final_num[num])
print(res)
