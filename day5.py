from day5_data import scrubbed_data

# Starting stacks

one = "Q M G C L".split()
two = "R D L C T F H G".split()
three = "V J F N M T W R".split()
four = "J F D V Q P".split()
five = "N F M S L B T".split()
six = "R N V H C D P".split()
seven = "H C T".split()
eight = "G S J V Z N H P".split()
nine = "Z F H G".split()

stacks = [[], one, two, three, four, five, six, seven, eight, nine]

move_num = 0
for move in scrubbed_data:
    for i in range(move[0]):
        a = stacks[move[1]].pop()
        stacks[move[2]].append(a)
        print()
    move_num += 1
    for stack in stacks:
        print(stack)
    print(move_num)

# Part 1 Solution
for n in stacks[1:]:
    print(n[-1])






