import numpy as np

opp_lk = ['A', 'B', 'C']
you_lk = ['X', 'Y', 'Z']

# read file
puzzle_input = np.loadtxt('2_puzzle_input.txt', delimiter=' ', dtype=str)

# Y X Z into numbers 0 1 2
opp = np.empty(puzzle_input.shape[0], dtype=int)
you = np.empty(puzzle_input.shape[0], dtype=int)
for lu in range(len(you_lk)):
    opp[(puzzle_input[:, 0] == opp_lk[lu])] = lu
    you[(puzzle_input[:, 1] == you_lk[lu])] = lu

# figure out scores
x = np.subtract(opp, you)
score = sum(you+1) + sum((x == 0)*3) + sum(((x == -1) + (x == 2))*6)

print(score)
