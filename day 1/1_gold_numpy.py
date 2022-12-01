import numpy as np

with open('1_puzzle_input.txt', 'r') as f:
    calories = [
        np.sum([
            int(i) for i in e.strip('\n').split('\n')
        ])
        for e in f.read().strip('\n\n').split('\n\n')
    ]

print(np.sum(np.sort(calories)[-3:]))
