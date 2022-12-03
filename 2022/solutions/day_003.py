from utils import *
import string


def content_dict():
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    contents = {}
    letters = string.ascii_lowercase + string.ascii_uppercase
    for i in range(1, 53):  # needs to be 1-53 to capture 'Z'
        contents[letters[i - 1]] = i
    return contents


def sum_keyed_list(ListArg, dictArg):
    sum = 0
    for letter in ListArg:
        sum += dictArg.get(letter)
    return sum


def rucksack_match(data):
    matches = []
    for line in data:
        sect1 = line[slice(0, len(line) // 2)]
        sect2 = line[slice(len(line) // 2, len(line))]
        for j in sect1:
            if j in sect2:
                matches.append(j)
                break
    return matches


def badge_match(data):
    matches = []
    for i in range(0, len(data), 3):
        for j in data[i]:
            if j in data[i + 1] and j in data[i + 2]:
                matches.append(j)
                break
    return matches


print(
    sum_keyed_list(rucksack_match(Input("003").read().splitlines()), content_dict())
)  # solution 3a

print(
    sum_keyed_list(badge_match(Input("003").read().splitlines()), content_dict())
)  # solution 3b
