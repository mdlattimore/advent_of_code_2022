import string
from day3_data import data
letters = string.ascii_letters

# Part 1
total = 0
for line in data:
    
    a = line[:len(line)// 2]
    b = line[len(line) // 2:]
    c = set(a).intersection(set(b))
    d = next(iter(c))
    value = letters.index(d) + 1
    total += value

print(total)


# Part 2
aggregate = []
total = 0

while data:
    a = data[0:3]
    aggregate.append(a)
    del data[0:3]
    

for group in aggregate:
    a = set(group[0]) & set(group[1]) & set(group[2])
    b = next(iter(a))
    value = letters.index(b) + 1
    total += value

print(total)
