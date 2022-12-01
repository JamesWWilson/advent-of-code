
# 12-05-2020

# https://adventofcode.com/2020/day/5

import pandas as pd 
import math as mth

## apply function to frame 
raw=[]
with open('input.txt','r') as f:
    for line in f:
        for i in line.split():
            raw.append(i)

seats = pd.DataFrame(raw, columns={"tik_info"})

#0: 0123|4567
#1: 0123|4567
#2: 0123|4567
#...
#127: 0123|4567

## FIND ROWS FUNCTION 
def find_row(tickets = pd.DataFrame()):
    # static variables (i) 
    row_numbers=[]
    mn = 0
    mx = tickets.size
    ticket_row = range(0,7)
    for i in range(mn,mx):
        # static variable (j)
        row_num = 0
        low = 0 
        high = 127
        for j in ticket_row:
            #print(low,"/",high)
            mid = ((high + low)/ 2) 
            # if last i set to row_num 
            if j == max(ticket_row):
                #keep high
                if tickets[i][j] == 'F': row_num = low
                # keep low 
                elif tickets[i][j] == 'B': row_num = high
                else: print("type 1 error")
            else:
                #keep range < mid
                if tickets[i][j] == 'F': high = mth.floor(mid)
                #keep range > mid
                elif tickets[i][j] == 'B': low = mth.ceil(mid)
                else: print("type 2 error")
        row_numbers.append(row_num)
    return(row_numbers)

row_output = find_row(tickets = seats["tik_info"])
row_output

def find_seat(tickets = pd.DataFrame()):
    print("start")
    # static variables (i)
    seat_numbers=[]
    mn = 0
    mx = tickets.size
    ticket_seat = range(7,10) # last three characters 
    for i in range(mn,mx):
        # static variable (j)
        seat_num = 0
        low = 0 
        high = 7
        for j in ticket_seat:
            #print(low,"/",high)
            mid = ((high + low)/ 2) 
            # if last i set to seat_num 
            if j == max(ticket_seat):
                #keep high
                if tickets[i][j] == 'L': seat_num = low
                # keep low 
                elif tickets[i][j] == 'R': seat_num = high
                else: print("type 1 error")
            else:
                #keep range < mid
                if tickets[i][j] == 'L': high = mth.floor(mid)
                #keep range > mid
                elif tickets[i][j] == 'R': low = mth.ceil(mid)
                else: print("type 2 error")
        seat_numbers.append(seat_num)
    return(seat_numbers)

seat_output = find_seat(tickets = seats["tik_info"])
seat_output

# Convert to list 
seating_map = {row_output[i]: seat_output[i] for i in range(0,len(row_output))}
seating_map = list(seating_map.items())
seating_map

# find max board pass 
max_board_pass=0
board_passes=[]
mn = 0
mx = len(row_output)

for i in range(mn,mx):
    board_pass = ((row_output[i] * 8) + seat_output[i])
    print(board_pass)
    if (board_pass > max_board_pass):
        max_board_pass = board_pass
    board_passes.append(board_pass)

print(max_board_pass)

## PART 2 ---
board_passes = board_passes.sort()

for i in range(1, len(board_passes)-1):
    md = board_passes[i]
    mx = board_passes[i+1]

    if( ((md+1) != mx) ):
        print(md)

