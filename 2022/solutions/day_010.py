from utils import *

def register_calculation(data):
    register = 1  # start at one
    cycle = 0
    checkpoints = [20, 60, 100, 140, 180, 220]
    signal_strength_sum = 0
    signal_strengths_repo = []

    def cycle_click_1():
        nonlocal cycle,signal_strength_sum
        cycle += 1
        if cycle in checkpoints:
            new_value = cycle * register
            signal_strength_sum += new_value
            signal_strengths_repo.append(new_value)

    for line in data:
        if line == "noop":
            cycle_click_1()
        else:
            cycle_click_1()
            cycle_click_1()
            register += int(line[4:])

    return(signal_strength_sum)


def record_and_print_pixels(data):
    pixel_matrix = [[], [], [], [], [], [], []]

    register = 1  # start at one
    cycle = 0  # can start at zero or one but need to configure cycle increase to match
    line_counter = 0

    def cycle_click_2():
        nonlocal cycle, line_counter

        if (cycle) % 40 == 0:
            line_counter += 1
        if cycle % 40 in [register - 1, register, register + 1]:
            pixel_matrix[line_counter].append("#")
        else:
            pixel_matrix[line_counter].append(".")
        cycle += 1

    for line in data:
        if line == "noop":
            cycle_click_2()
        else:
            cycle_click_2()
            cycle_click_2()
            register += int(line[4:])

    for output in pixel_matrix:
        print(output)


real_input = Input("010").read().splitlines()
test_input = Input("010_test").read().splitlines()

# TEST
assert register_calculation(test_input) == 13140

# Part 1 
print(register_calculation(real_input))
# Part 2
record_and_print_pixels(real_input)
