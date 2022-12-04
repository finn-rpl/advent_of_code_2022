
with open('puzzle_input.txt', 'r') as f:
    rows = f.read().strip('\n').split('\n')

ranges = [[p.split('-') for p in r.split(',')] for r in rows]

full_contain = 0

for r in ranges:
    if int(r[1][0]) <= int(r[0][0]) <= int(r[1][1]) or int(r[1][0]) <= int(r[0][1]) <= int(r[1][1]) or \
            int(r[0][0]) <= int(r[1][0]) <= int(r[0][1]) or int(r[0][0]) <= int(r[1][1]) <= int(r[0][1]):
        full_contain += 1

print(full_contain)
