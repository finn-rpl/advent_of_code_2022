
with open('3_puzzle_input.txt', 'r') as f:
    sacks = f.read().strip('\n').split('\n')

prio_sum = 0

for s in sacks:
    c1 = s[:int(len(s)/2)]
    c2 = s[int(len(s)/2):]
    for i in c1:
        if i in c2:
            io = ord(i)
            if io > 96:
                prio_sum += io - 96
            else:
                prio_sum += io - 38
            break

print(prio_sum)

