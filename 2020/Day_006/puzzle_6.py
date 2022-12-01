
# 12-06-2020

# https://adventofcode.com/2020/day/6

import pandas as pd 
import numpy as np 

# Read each line of the file into a format suitable for a matrix 
merged_sublist = []
custom_forms = []
with open('input.txt','r') as f:
    for line in f:
        # if line is not blank
        if(len(line.split())!=0):
            cf = line.split()
            # integrate into sublist
            for i in cf:
                merged_sublist.append(i)
        # if line is blank
        if(len(line.split())==0):
            # append sublist to custom_forms
            for i in merged_sublist:
                custom_forms.append(merged_sublist)
            # clear sublist object 
            merged_sublist = []

print(custom_forms)

cf_data = pd.DataFrame(custom_forms)
cf_data.drop_duplicates(inplace=True)
#cf_data.reset_index(inplace=True)
cf_data.head(20)

# count individuals 


# combined fields 
cf_data["combined_fields"] = cf_data[0].fillna('') + cf_data[1].fillna('') + cf_data[2].fillna('')  + cf_data[3].fillna('') + cf_data[4].fillna('') 

# sort each row
# count unique number of characters 
cf_data["combined_fields"] = cf_data["combined_fields"].str.replace(' ', '')
cf_data['letter_cnt']= cf_data.apply(lambda x: len(set(x["combined_fields"])),axis=1)
cf_data['letter_cnt'] = cf_data['letter_cnt'].astype(float)
cf_data

cf_data.head(20)

sum(cf_data['letter_cnt'])


###
with open("input.txt") as f:
    input = f.read().strip().split('\n\n')

def yes_answers(input, fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))
        # * acts as an unpacking operator 

input = [line.split() for line in input]

print("Part 1:", sum(yes_answers(input, set.union)))

print("Part 2:", sum(yes_answers(input, set.intersection)))



''' 
This was the first time that I had ever used the unpacking operator, *. It acts just like the ... spread operator in JavaScript. What this does is expand an iterable object (such as a list, set, or dict) into separate arguments for a function.

Here is a simple example:

def f(x,y):
  return x + y
f([1,2])  # error
f(*[1,2]) # works

The function expects two arguments, and with the * operator we can break the list [1, 2] into two arguments.

Take a look at how help(sum) and help(set.union) differ in their arguments. sum takes a single iterable parameter. set.union accepts one or more sets. In my case, I have a list of sets that I created through list comprehension. To break those into separate arguments for set.union I used the * operator.

Here is an example:

a = set([1, 2, 3])
b = set([3, 4, 5])
c = set([5, 6, 7])
u = [a, b, c]
# I want the union of all three from an array. 
set.union(u) # error
set.union(*u) # works

So for generators...these are really cool. I only learned about them recently (I am learning Python this advent).

In JavaScript I have become very fond of filter, map, and reduce. Works great, but you can run into a constraint: each function needs to fully compute before it gets passed on to the next.

So, for example, suppose you have an array a and you set up something like a.filter(x => x > 0).map(x => x * x).reduce((accumulator, value) => accumulator + value, 0) to sum the squares of positive values in your data set. This is fine, but suppose instead of reading from an in-memory array a you were reading from something slow, such as a web request. The thing you might run into is opportunity to do work filter and map as the next value fetches. filter has to complete before map gets to do anything, and map blocks until reduce gets to do anything.

Python's yield gives you an alternative to this. yield passes values as they are read from the outermost to innermost generator. This allows for all kinds of interesting efficiencies, since you don't have to fully buffer list comprehensions as intermediate calculations.

An interesting analog to this is Windows PowerShell. Native PowerShell commands can pipeline from left to right, streaming input from one cmdlet to the next before the first cmdlet terminates. This doesn't work for non-native programs, such as Windows executables.

(If anyone reading this sees that I have made a statement in error please do feel free to correct me!)
 '''



