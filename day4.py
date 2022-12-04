from day4_data import data

data2 = [w.split(',') for w in data]

# Part 1 and Setup
dummy = []
for n in data2:
    inter = []
    for i in n:
        i = i.split('-')
        inter.append((int(i[0]), int(i[-1])))
    dummy.append(inter)


final = []
for i0 in dummy:
    inter3 = []
    for i1 in i0:
        inter3.append([w for w in range(i1[0], i1[-1] + 1)])
    final.append(inter3)


pairs = 0
for pair in final:
    if set(pair[0]).issubset(set(pair[1])) or set(pair[1]).issubset(set(pair[0])):
        pairs += 1
# Answer to Part 1
print(pairs)

# Part 2
pairs2 = 0
for pair in final:
    if set(pair[0]) & set(pair[1]):
        pairs2 += 1
# Answer to Part 2
print(pairs2)