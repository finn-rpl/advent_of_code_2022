
with open('1_puzzle_input.txt', 'r') as f:
    elves = f.read().strip('\n\n').split('\n\n')


calories = [
    sum([
            int(i) for i in e.strip('\n').split('\n')
        ])
    for e in elves
]


print(
    sum(
        sorted(calories)[-3:]
    )
)
