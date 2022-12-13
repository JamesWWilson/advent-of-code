from utils import *
import copy

def iterate(data):

    length = 10
    rope = [[0, 0]] * length
    tail_visits = [[0, 0]]  # preset with start location to be safe

    for line in data:
        direction = line[0]
        distance = int(line[2:])
        print("Command: Go", direction, "by", distance)
        
        # update Head based on command
        if direction == "R":
            # add to x '[0]' coordinate
            for _ in range(distance,0,-1):
                rope[0] = [rope[0][0] + 1,rope[0][1] + 0] 
                for knot in range(1,length):
                    # print('check current know', rope[knot], 'to prev', rope[knot-1],knot)
                    # print(neighbors8(rope[knot - 1]))
                    if rope[knot] in neighbors8(rope[knot - 1]) or rope[knot] == rope[knot - 1]:
                        # print("no move needed for knot", knot)
                        pass
                    else:
                        rope[knot] = [rope[knot][0] + 1, rope[knot][1] + 0]
                        if rope[knot] in neighbors4(rope[knot - 1]):
                            # print("move horizontal/vertical")
                            pass
                        else:  
                            # print("diagonal move")
                            if rope[knot - 1][1] > rope[knot][1]:
                                rope[knot] = [rope[knot][0] + 0, rope[knot][1] + 1]
                            else:
                                rope[knot] = [rope[knot][0] + 0, rope[knot][1] - 1]
                    if knot == (length-1):
                        tail_visits.append(copy.deepcopy(rope[length-1])) 

        if direction == "L":
            # reduce x '[0]' coordinate
            for _ in range(distance,0,-1):
                rope[0] = [rope[0][0] - 1,rope[0][1] + 0] 
                for knot in range(1,length):
                    if rope[knot] in neighbors8(rope[knot - 1]) or rope[knot] == rope[knot - 1]:
                        # print("no tail move needed")
                        pass
                    else:
                        # if only off by one coordinate - move that way by 1
                        rope[knot] = [rope[knot][0] - 1, rope[knot][1] + 0]
                        if rope[knot] in neighbors8(rope[knot - 1]):
                            # print("move horizontal/vertical")
                            pass
                        else:  # if off by more than one coordinate, move with diagonal
                            # print("diagonal move")
                            if rope[knot - 1][1] > rope[knot][1]:
                                rope[knot] = [rope[knot][0] + 0, rope[knot][1] + 1]
                            else:
                                rope[knot] = [rope[knot][0] + 0, rope[knot][1] - 1]
                    if knot == (length-1):
                        tail_visits.append(copy.deepcopy(rope[knot])) # append tail only 
                print(rope)

        if direction == "U":
            # add to y '[1]' coordinate
            for _ in range(distance,0,-1):
                rope[0] = [rope[0][0] + 0,rope[0][1] + 1] 
                for knot in range(1,length):
                    if rope[knot] in neighbors8(rope[knot - 1]) or rope[knot] == rope[knot - 1]:
                        # print("no tail move needed")
                        pass
                    else:
                        # if only off by one coordinate - move that way by 1
                        rope[knot] = [rope[knot][0] + 0, rope[knot][1] + 1]
                        if rope[knot] in neighbors4(rope[knot - 1]):
                            # print("move horizontal/vertical")
                            pass
                        else:  # if off by more than one coordinate, move with diagonal
                            # print("diagonal move")
                            if rope[knot - 1][0] > rope[knot][0]:
                                rope[knot] = [rope[knot][0] + 1, rope[knot][1] + 0]
                            else:
                                rope[knot] = [rope[knot][0] - 1, rope[knot][1] + 0]
                    if knot == (length-1):
                        tail_visits.append(copy.deepcopy(rope[knot])) # append tail only 

            
        if direction == "D":
            # reduce  y '[1]' coordinate
            for _ in range(distance,0,-1):
                rope[0] = [rope[0][0] + 0,rope[0][1] - 1] 
                for knot in range(1,length):
                    if rope[knot] in neighbors8(rope[knot - 1]) or rope[knot] == rope[knot - 1]:
                        # print("no tail move needed")
                        pass
                    else:
                        # if only off by one coordinate - move that way by 1
                        rope[knot] = [rope[knot][0] + 0, rope[knot][1] - 1]
                        if rope[knot] in neighbors4(rope[knot - 1]):
                            # print("move horizontal/vertical")
                            pass
                        else:  # if off by more than one coordinate, move with diagonal
                            # print("diagonal move")
                            if rope[knot - 1][0] > rope[knot][0]:
                                rope[knot] = [rope[knot][0] + 1, rope[knot][1] + 0]
                            else:
                                rope[knot] = [rope[knot][0] - 1, rope[knot][1] + 0]
                    if knot == (length-1):
                        tail_visits.append(copy.deepcopy(rope[knot])) # append tail only ([-1])
        print(rope) # print rope each time

    # # final count
    print(rope)
    print(tail_visits)
    num_unique_visits = len(set(tuple(row) for row in tail_visits))
    return num_unique_visits


# TEST
test = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
test2 = ["R 5", "U 8", "L 8"]#, "D 3", "R 17", "D 10", "L 25", "R 20"]

#Command: Go L by 8

# assert iterate(test) == 13 # PART 1
# test = ["R 10","U 5","L 8","D 3"]
print(iterate(test)) #Should be 1 for PART 2
print(iterate(test2)) #Should be 36 for PART 2 - current 29 positions ... 

# SOLUTION
# print(iterate(Input("009").read().splitlines()))
