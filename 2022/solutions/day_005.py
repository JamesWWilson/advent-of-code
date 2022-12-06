from utils import *


def move_crates(data, version: int):
    # set variables
    box_list = []
    move_box = []
    num_stacks = 0  # PASS VARIABLE OUT

    # first separate content by what it contains
    for line in data:
        if contains_number(line) == False:
            if line == "":
                pass
            else:
                box_list.append(line)
        else:
            if num_stacks == 0:
                num_stacks = largestNumber(line)
            else:
                move_box.append(line)

    # create and fill stacks
    stacks = [[] for i in range(num_stacks)]
    for item in box_list:
        for cnt in range(num_stacks):
            box_index = 4 * cnt + 1
            if item[box_index] == " ":
                continue
            stacks[cnt].append(item[box_index])

    class stack:
        boxes = []

        def __init__(self):
            self.boxes = stacks

        def move_v1(self, amount, starting_stack, ending_stack):
            movers = self.boxes[starting_stack - 1][:amount][::-1]
            self.boxes[starting_stack - 1] = self.boxes[starting_stack - 1][amount:]
            self.boxes[ending_stack - 1] = movers + self.boxes[ending_stack - 1]

        def move_v2(self, amount, starting_stack, ending_stack):
            movers = self.boxes[starting_stack - 1][:amount]
            self.boxes[starting_stack - 1] = self.boxes[starting_stack - 1][amount:]
            self.boxes[ending_stack - 1] = movers + self.boxes[ending_stack - 1]

        def print_top_cargo(self):
            for stack in self.boxes:
                print(stack[0], end="")
            print("\n")

    # Initialize cargo object and call move function based on each command
    cargo = stack()
    for action in move_box:
        parts = action.split(" ")
        parts[5] = parts[5][0]
        if version == 1:
            cargo.move_v1(int(parts[1]), int(parts[3]), int(parts[5]))
        elif version == 2:
            cargo.move_v2(int(parts[1]), int(parts[3]), int(parts[5]))
        else:
            print("error: no version stated")

    cargo.print_top_cargo()


## TEST
test = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

# Part 1
move_crates(test, 1)  # CMZ
move_crates(Input("005").read().splitlines(), 1)

# Part 2
move_crates(test, 2)  # MCD
move_crates(Input("005").read().splitlines(), 2)

# NOTES
# Some code re-interpreted from Reddit User u/temanuel38
# Helpful Stackoverflow: https://stackoverflow.com/questions/4012340/colon-in-python-list-index
