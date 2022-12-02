
with open('2_puzzle_input.txt', 'r') as f:
    rounds = f.read().strip('\n').split('\n')

beats = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

draws = {
    'A': 'X',
    'B': 'Y',
    "C": 'Z'
}

results = {
    'X': 1,
    "Y": 2,
    "Z": 3
}

score = 0

for r in rounds:
    opp, you = r.strip(' ').split(' ')
    print(opp + you)
    if beats[opp] == you:
        score += results[you]
    elif draws[opp] == you:
        score += results[you] + 3
    else:
        score += results[you] + 6


print(score)
