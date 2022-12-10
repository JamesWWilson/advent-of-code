from utils import *
import copy


def iterate(data):
    Head = [0, 0]  # x,y
    Tail = [0, 0]
    tail_visits = [[0, 0]]  # preset with start location to be safe

    for line in data:
        direction = line[0]
        distance = int(line[2:])
        # print("Command: Go", direction, "by", distance)

        # update Head based on command
        if direction == "R":
            # add to x '[0]' coordinate
            while distance > 0:
                Head[0] += 1  # add to x '[0]' coordinate
                if Tail in neighbors8(Head) or Tail == Head:
                    # print("no tail move needed")
                    pass
                else:
                    # if only off by one coordinate - move that way by 1
                    Tail[0] += 1
                    if Tail in neighbors4(Head):
                        # print("move horizontal/vertical")
                        pass
                    else:  # if off by more than one coordinate, move with diagonal
                        # print("diagonal move")
                        if Head[1] > Tail[1]:
                            Tail[1] += 1
                        else:
                            Tail[1] -= 1
                distance -= 1
                tail_visits.append(copy.deepcopy(Tail))
                # print("visits", tail_visits)

        if direction == "L":
            # reduce  x '[0]' coordinate
            while distance > 0:
                Head[0] -= 1
                if Tail in neighbors8(Head) or Tail == Head:
                    # print("no move needed")
                    pass
                else:
                    # if only off by one coordinate - move that way by 1
                    Tail[0] -= 1
                    if Tail in neighbors4(Head):
                        # print("move horizontal/vertical")
                        pass
                    else:  # if off by more than one coordinate, move with diagonal
                        # print("diagonal move")
                        if Head[1] > Tail[1]:
                            Tail[1] += 1
                        else:
                            Tail[1] -= 1
                distance -= 1
                tail_visits.append(copy.deepcopy(Tail))
                # print('visits',tail_visits)

        if direction == "U":
            # add to y '[1]' coordinate
            while distance > 0:
                Head[1] += 1
                if Tail in neighbors8(Head) or Tail == Head:
                    # print("no update neeeded")
                    pass
                else:
                    # if only off by one coordinate - move that way by 1
                    Tail[1] += 1
                    if Tail in neighbors4(Head):
                        # print("move horizontal/vertical")
                        pass
                    else:  # if off by more than one coordinate, move with diagonal
                        # print("diagonal")
                        if Head[0] > Tail[0]:
                            Tail[0] += 1
                        else:
                            Tail[0] -= 1
                distance -= 1
                tail_visits.append(copy.deepcopy(Tail))
                # print('visits',tail_visits)

        if direction == "D":
            # reduce  y '[1]' coordinate
            while distance > 0:
                Head[1] -= 1
                if Tail in neighbors8(Head) or Tail == Head:
                    # print("no update neeeded")
                    pass
                else:
                    # if only off by one coordinate - move that way by 1
                    Tail[1] -= 1
                    if Tail in neighbors4(Head):
                        # print("move horizontal/vertical")
                        pass
                    else:  # if off by more than one coordinate, move with diagonal
                        # print("move diagonal")
                        if Head[0] > Tail[0]:
                            Tail[0] += 1
                        else:
                            Tail[0] -= 1
                distance -= 1
                tail_visits.append(copy.deepcopy(Tail))
                # print('visits',tail_visits)

        # print("New Head Position", Head)
        # print("New Tail Position", Tail)

    # final count
    num_unique_visits = len(set(tuple(row) for row in tail_visits))
    return num_unique_visits


# TEST
test = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]

assert iterate(test) == 13


# SOLUTION
print(iterate(Input("009").read().splitlines()))
