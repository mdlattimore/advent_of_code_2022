from day1_data import data

# Part 1

totals = []
for entry in data:
    new = entry.split("\n")
    totals.append(new)

new_totals = []
for entry in totals:
    new_totals.append([int(i) for i in entry])

sums = []
for n in new_totals:
    sums.append(sum(n))

# Solution for Part 1
print(max(sums))

# Part 2

sums.sort()

# Solution for Part 2
print(sum(sums[-3:]))
