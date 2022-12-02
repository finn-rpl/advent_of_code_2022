
with open('2_puzzle_input.txt', 'r') as f:
    rounds = f.read().strip('\n').split('\n')

loses = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

draws = {
    'A': 'X',
    'B': 'Y',
    "C": 'Z'
}

wins = {
    'A': 'Y',
    'B': 'Z',
    "C": 'X'
}

results = {
    'X': 1,
    "Y": 2,
    "Z": 3
}

score = 0

for r in rounds:
    opp, you = r.strip(' ').split(' ')
    if you == 'X':
        you = loses[opp]
        score += results[you]
    elif you == 'Y':
        you = draws[opp]
        score += results[you] + 3
    else:
        you = wins[opp]
        score += results[you] + 6


print(score)
