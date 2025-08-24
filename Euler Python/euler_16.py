result = pow(2, 1000)
strresult = str(result)
digitsum = 0
for num in strresult:
    digitsum += int(num)
print(digitsum)