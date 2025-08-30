# create a hashmap that has the letters associated with a number
# based on its digit's place

LIMIT = 1001
numberstrings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11 : "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15 : "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19 : "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "onethousand"
}

finaltotal = 0
# need to add an "and" in 100s.
for num in range(1, LIMIT):
    total = 0
    if num >= 1000:
        total += len(numberstrings[num])
        print(f'{numberstrings[num]} ', end="")
    elif num >= 100:
        curnum = num//100
        tensnum = num%100 - num%10
        total += len(numberstrings[curnum])
        total += len(numberstrings[100])

        print(f'{numberstrings[curnum]} {numberstrings[100]} ', end="")
        if tensnum > 0 or num%10 > 0:
            total += len("and")
            print(f'and ', end="")
        
        if num%100 > 10 and num%100 < 20:
                total += len(numberstrings[num%100])
                print(f'{numberstrings[num%100]} ', end="")
        else:
            if tensnum > 0:
                total += len(numberstrings[tensnum])
                print(f'{numberstrings[tensnum]} ', end="")
            
            if num%10 > 0:
                total += len(numberstrings[num%10])
                print(f'{numberstrings[num%10]} ', end="")    

    elif num > 20:
        curnum = num - num%10
        total += len(numberstrings[curnum])
        print(f'{numberstrings[curnum]} ', end="") 
        if num%10 > 0:
            total += len(numberstrings[num%10])
            print(f'{numberstrings[num%10]} ', end="") 
    else:
        total += len(numberstrings[num])
        print(f'{numberstrings[num]} ', end="") 
    print(num, total)
    finaltotal += total

print(f'Final total: {finaltotal}')