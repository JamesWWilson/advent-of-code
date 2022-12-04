from utils import *


def solution_4a(data):
    fully_contain_cnt = 0
    check = []
    for line in data:
        elements = list(map(int, re.findall(r"\d+", line)))
        if (elements[0] <= elements[2] and elements[1] >= elements[3]) or (
            elements[2] <= elements[0] and elements[3] >= elements[1]
        ):
            fully_contain_cnt += 1
            check.append(elements)
    return fully_contain_cnt


def solution_4b(data):
    overlap_cnt = 0
    for line in data:
        elements = list(map(int, re.findall(r"\d+", line)))
        if (
            (elements[0] <= elements[2] and elements[1] >= elements[3])
            or (elements[2] <= elements[0] and elements[3] >= elements[1])
            or (elements[0] <= elements[2] and elements[1] >= elements[2])
            or (elements[3] >= elements[1] and elements[2] <= elements[1])
            or (elements[3] >= elements[0] and elements[2] <= elements[0])
            or (elements[0] == elements[2])
            or (elements[0] == elements[3])
            or (elements[1] == elements[2])
            or (elements[1] == elements[3])
        ):
            overlap_cnt += 1
    return overlap_cnt


# Testing
assert solution_4a(["51-88,52-87"]) == 1
assert (
    solution_4a(["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]) == 2
)
assert (
    solution_4b(["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]) == 4
)

assert solution_4b(["22-64,9-23"]) == 1


# Solutions
print(solution_4a(Input("004").read().splitlines()))
print(solution_4b(Input("004").read().splitlines()))
