from day2_data import guide_matrix

A = 'rock1'
B = 'paper1'
C = 'scissors1'
X = 'rock2'
Y = 'paper2'
Z = 'scissors2'

# Part 1
score = 0
plays = 0
for play in guide_matrix:
    if play == "A X":
        score += 3 + 1
        plays += 1
    elif play == "A Y":
        score += 6 + 2
        plays += 1
    elif play == "A Z":
        score += 0 + 3
        plays += 1
    elif play == "B X":
        score += 0 + 1
        plays += 1
    elif play == "B Y":
        score += 3 + 2
        plays += 1
    elif play == "B Z":
        score += 6 + 3
        plays += 1
    elif play == "C X":
        score += 6 + 1
        plays += 1
    elif play == "C Y":
        score += 0 + 2
        plays += 1
    elif play == "C Z":
        score += 3 + 3
        plays += 1

print(score)


# Part 2
score = 0
for play in guide_matrix:
    if play[0] == "A" and play[-1] == "X":
        score += 3
    elif play[0] == "A" and play[-1] == "Y":
        score += 4
    elif play[0] == "A" and play[-1] == "Z":
        score += 8
    elif play[0] == "B" and play[-1] == "X":
        score += 1
    elif play[0] == "B" and play[-1] == "Y":
        score += 5
    elif play[0] == "B" and play[-1] == "Z":
        score += 9
    elif play[0] == "C" and play[-1] == "X":
        score += 2
    elif play[0] == "C" and play[-1] == "Y":
        score += 6
    elif play[0] == "C" and play[-1] == "Z":
        score += 7

print(score)
