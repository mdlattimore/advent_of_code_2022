from day5_data import scrubbed_data


# Starting stacks. See notes in day5.py for more info

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

for move in scrubbed_data:
    number = move[0]
    from_stack = move[1]
    to_stack = move[2]
    a = stacks[from_stack][-number:]   
    del stacks[from_stack][-number:]
    for value in a:
        stacks[to_stack].append(value)

    # Diagnostic    
    # print()
    # for stack in stacks:
    #     print(stack)


# Part 2 Solution
for n in stacks[1:]:
    print(n[-1])






