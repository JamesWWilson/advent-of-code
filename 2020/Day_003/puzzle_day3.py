
# 12-03-2020

# https://adventofcode.com/2020/day/3

import pandas as pd
import numpy as np

def chr_split(word): 
    return [char for char in word]  
      
raw = []
# Read each line of the file into a format suitable for a matrix 
with open('input.txt','r') as f:
    for line in f:
        print(chr_split(str(line.split())[2:-2]))
        raw.append(chr_split(str(line.split())[2:-2]))

data = pd.DataFrame(raw)
# encode to numeric 
# # replace all '.' as 0 and all '#' as 1 
data = data.replace('.',0)
data = data.replace('#',1)
data.head()
data.shape 

#  extend data to make a complete dataset 
for _ in range(8):
    data = pd.concat([data, data], axis=1)

data.head()
data.shape 

# convert to matrix 
A = np.array(data.values,dtype=float)
A 

# count on slopes
num_rows = A.shape[0]
num_cols = A.shape[1]

# slope of right 3 down 1 
slope_x = [1,1,1,1,2] # down 1
slope_y = [1,3,5,7,1] # right 3 

# TREEES
ALL_TREES = []

# iterate through slopes 
for j in range(0,5): 
    #set trees to empty 
    trees = []
    # iterate down the slope 
    for i in range(0,num_rows):
        # static variables
        start_x = 0
        start_y = 0
        # update next iterators 
        next_x = start_x + slope_x[j] * i
        next_y = start_y + slope_y[j] * i
        # evaluate val 
        val = A[next_x,next_y]
        # catch index errors!!! 


        print(i, "iterator for", val, "value")
        # append val to list
        trees.append(val)
    print(sum(trees))
    ALL_TREES.append(sum(trees))

# HOW MANY TREES ??? 
print(ALL_TREES)

# 67*211*77*89*37





