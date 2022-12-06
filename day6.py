from day6_data import data

# Function to evaluate whether a list of characters constitutes a set. Compares length of the list to length of a set of that list. If equal, list constitutes a set.
def isset(n):
    if len(n) == len(set(n)):
        return True
    else:
        return False

# Part 1
start = 0
stop = 4
while True:
    if isset(data[start: stop]):
        print(f"Part 1 answer: {stop}")
        break
    else:
        start += 1
        stop += 1
        continue

# Part 2
start1 = 0
stop1 = 14
while True:
    if isset(data[start1: stop1]):
        print(f"Part 2 answer: {stop1}")
        break
    else:
        start1 += 1
        stop1 += 1
        continue

