import numpy as np

opp_lk = ['A', 'B', 'C']
you_lk = ['X', 'Y', 'Z']

# read file
puzzle_input = np.loadtxt('2_puzzle_input.txt', delimiter=' ', dtype=str)

opp = np.empty(puzzle_input.shape[0], dtype=int)
outcomes = np.empty(puzzle_input.shape[0], dtype=int)
for lu in range(len(you_lk)):
    # A B C into numbers 0 1 2
    opp[(puzzle_input[:, 0] == opp_lk[lu])] = lu
    # X Y Z into outcomes
    outcomes[(puzzle_input[:, 1] == you_lk[lu])] = lu

# figure out what you put on a
you = np.empty(puzzle_input.shape[0], dtype=int)
# loss
you[outcomes == 0] = opp[outcomes == 0] - 1
you[you == -1] = 2
# draw
you[outcomes == 1] = opp[outcomes == 1]
# win
you[outcomes == 2] = opp[outcomes == 2] + 1
you[you == 3] = 0

score = sum(outcomes*3) + sum(you+1)

print(score)
