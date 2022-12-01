# Puzzle 1-A 
# 12-01-2020

# Read Input Text File in 
day1_input = open("day1_input.txt", "r") 
day1_nums = list(day1_input.readlines())
print(day1_nums)
day1_input.close()

# convert to list, clean, and make integers 
nums = []	  
for l in day1_nums:
    nums.append(int(l.replace("\n", "")))

# determine which two integers match using algorithm 
print(list(nums))

# first sort the data 
def insertion_sort(v):
    n = len(v)
    for i in range(1, n):
        j = i
        while j >= 1 and v[j-1] > v[j]:  
            v[j], v[j-1] = v[j-1], v[j]
            j -= 1
        print("i={}, {}".format(i, v))
    return(v)

insertion_sort(nums)  

# find the match and print it 
def match_2_2020(v):
    match_val = 2020
    # length of list 
    n = len(v)
    # iterate through list 
    for i in range(0,n):
        # index through matches 
        for k in range(1,n-i):
            # iterate through next items in list 
            j = i + k
            # while j iterator is less than or equal to end of list
            if(v[i] + v[j] == match_val):
                print(v[i], "plus" , v[j], "equals 2020!")
                print(v[i], "times", v[j],  "equals", v[i]*v[j])
                return(None)
    print("i={}".format(i))

match_2_2020(nums)

# determine multiple of match 

# timer on algorithm 
# %lprun -f insertion_sort insertion_sort(a)

def match_3_2020(v):
    match_val = 2020
    # length of list 
    n = len(v)
    # iterate through list 
    for i in range(0,n):
        # index through matches 
        for k in range(1,n-i-1):
            # iterate through next items in list 
            for l in range(2,n-i-2):
                j_one = i + k
                j_two = i + l
                # while j iterator is less than or equal to end of list
                #while j <= n:
                if((v[i] + v[j_one] + v[j_two]) == match_val):
                    #print(v[i], "plus" , v[j_one], "plus", v[j_two], "equals 2020!")
                    #print(v[i], "times", v[j_one], "plus", v[j_two], "equals", v[i]*v[j_one]*[j_two])
                    #return(None)
                    return(v[i],v[j_one],v[j_two])
        #print("i={}".format(i))

match_3_2020(nums)
