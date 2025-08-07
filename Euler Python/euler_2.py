LIMIT = 4000000

efs = 2
fs = {1: 1, 2: 2}
i = 3
while True:
    fs[i] = fs[i-1] + fs[i-2]
    if fs[i] > LIMIT:
        break
    elif fs[i] % 2 == 0:
        efs += fs[i]
    i += 1
print(efs)
