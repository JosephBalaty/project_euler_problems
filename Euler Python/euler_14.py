# find the longest collatz sequence for a number that starts
# under 1 million
#   go through each number, starting from 1, and go through the sequence
#   recording the longest number until you reach 2 million.

n = 1
LIMIT = 1000000
# LIMIT = 14
max_seq = 0
max_num = 1

while n < LIMIT:
    curnum = n
    curseq = 0
    while curnum != 1:
        if curnum % 2 == 0:
            curnum /= 2
        elif curnum % 2 == 1:
            curnum = 3*curnum + 1
        curseq += 1
    if curseq > max_seq:
        max_seq = curseq
        max_num = n
    n += 1

print(f'Maximum sequence is: {max_seq}\nNumber is: {max_num}')
