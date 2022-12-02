# Puzzle 1
# 12-01-2022

from utils import * 

# Sum lines in a text file and append to list when blank line appears 
def calc_calories(data):
    all_cal = []
    elf_cal = 0
    for line in data:
        if len(line) > 1: # blank line expressed as length 1 
            elf_cal = elf_cal + int(line)
        else:
            all_cal.append(elf_cal)
            elf_cal = 0
    return(all_cal)

#function to return the sum of the largest [x] items in a list 
def sum_top_x(list, x):
    top_x = sorted(list, reverse = True)[:x]
    if x > 1:
        top_x = sum(top_x)
    return(top_x)

# Load input and solve
input = Input('001').readlines()
print(sum_top_x(calc_calories(input),1)) #solution 1a
print(sum_top_x(calc_calories(input),3)) #solution 1b