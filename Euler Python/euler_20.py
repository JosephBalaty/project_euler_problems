
total = 1
s = 0
for n in range(2, 101):
    total *= n
total = str(total)
for n in total:
    s += int(n)

print(s)