
with open('3_puzzle_input.txt', 'r') as f:
    sacks = f.read().strip('\n').split('\n')


prio_sum = 0

for s in range(int(len(sacks)/3)):
    s1 = sacks[s*3]
    s2 = sacks[(s*3)+1]
    s3 = sacks[(s*3)+2]
    for i in s1:
        if i in s2 and i in s3:
            io = ord(i)
            if io > 96:
                prio_sum += io - 96
            else:
                prio_sum += io - 38
            break

print(prio_sum)

