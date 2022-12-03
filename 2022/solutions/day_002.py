from utils import *

# A | X = Rock
# B | Y = Paper
# C | Z = Scisscors
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

game_dict_2a = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6,
}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
game_dict_2b = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7,
}


def extract_rounds(data):
    round = ""
    rounds = []
    for line in data:
        for char in line.strip():  # strip removes new line
            if char == " ":
                pass
            else:
                round = round + char
        rounds.append(round)
        round = ""
    return rounds


def score(dictArg, keysListArg):
    score = 0
    for list_item in keysListArg:
        if list_item in dictArg:
            score += dictArg[list_item]
    return score


# # Load input and solve
print(score(game_dict_2a, extract_rounds(Input("002").readlines())))  # solution 2a
print(score(game_dict_2b, extract_rounds(Input("002").readlines())))  # solution 2b
