# 12-02-2020

# https://adventofcode.com/2020/day/2

import pandas as pd
import numpy as np

# Import Data 
passwords = pd.read_csv("input.txt", sep=":",header=None,names=["policy","password"])
passwords.head()

# Split Policy into [at_least,at_most,letter]
passwords['at_least'] = passwords['policy'].str.split('-').str[0].astype(int) # remove anything after :
passwords['at_most'] = passwords['policy'].str.split('-').str[1].str.split(' ').str[0].astype(int)  # remove anything after :
passwords['letter'] = passwords['policy'].str.split('-').str[1].str.split(' ').str[1] # remove anything after :
passwords.head()

# Count times letter is found in password 
passwords['letter_count'] = passwords.apply(lambda x: x['password'].count(x['letter']), axis=1).astype(int)

# Determine if pass or not
passwords['pass_flg'] = passwords.apply(lambda x: (x['letter_count'] >= x['at_least']) & (x['letter_count'] <= x['at_most']), axis=1)

# Count Passes 
#passwords['pass_flg'].count()

pass_cnt = passwords.groupby(['pass_flg']).password.agg(['count']).reset_index()
pass_cnt
#   pass_flg  count
# 0    False    472
# 1     True    528

### PART 2 - only one match of letter on one of two indexes 

# THESE DONT WORK LOL 
# passwords['check_one'] = passwords["password"].str.slice(start = 1, stop = 2)
# passwords['check_one'] = passwords.apply(lambda x: x['password'].str.slice(start = x['at_least'], stop = (x['at_least'] + 1) ), axis=1)
# passwords['check_one'] = passwords["password"].apply(lambda x: slice(x['at_least'],(x['at_least'] + 1)))
# passwords['check_one'] = passwords['password'].str.slice(start = passwords['at_least'], stop = (passwords['at_least'] + 1) )
# passwords['check_one'] = passwords['password'].str[passwords['at_least'], (passwords['at_least'] + 1)]

passwords['check_one'] = passwords.apply(lambda x: x['password'][ x['at_least']:(x['at_least'] + 1) ] , axis=1)
passwords['check_two'] = passwords.apply(lambda x: x['password'][ x['at_most']:(x['at_most'] + 1) ] , axis=1)
passwords.head()


passwords['pass_flg2'] = passwords.apply(lambda x: (((x['letter'] == x['check_one']) | (x['letter'] == x['check_two'])) & (x['check_one'] != x['check_two'])) , axis=1)
passwords.head()

pass_cnt2 = passwords.groupby(['pass_flg2']).password.agg(['count']).reset_index()
pass_cnt2

#    pass_flg2  count
# 0      False    503
# 1       True    497

