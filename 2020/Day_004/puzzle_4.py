# 12-04-202

# https://adventofcode.com/2020/day/4

import pandas as pd 
import numpy as np 

# Read each line of the file into a format suitable for a matrix 
merged_sublist = []
passports = []
with open('input.txt','r') as f:
    for line in f:
        # if line is not blank
        if(len(line.split())!=0):
            #print(1)
            pp = line.split()
            # integrate into sublist
            #for i in zip(pp, merged_sublist):
            for i in pp:
                merged_sublist.append(i)
        # if line is blank
        if(len(line.split())==0):
            #print(0)
            # append sublist to passports
            for i in merged_sublist:
                passports.append(merged_sublist)
            # clear sublist object 
            merged_sublist = []

print(passports)

# Set to data table 
pp_data = pd.DataFrame(passports)
pp_data.drop_duplicates(inplace=True)
pp_data.head(20)

# combined fields 
pp_data["combined_fields"] = pp_data[0].fillna('') + " " + pp_data[1].fillna('') + " " + pp_data[2].fillna('') + " "  + pp_data[3].fillna('') + " " + pp_data[4].fillna('') + " "  + pp_data[5].fillna('') + " "  + pp_data[6].fillna('') + " " + pp_data[7].fillna('')
# subset to just combined field 
pp_data = pd.DataFrame(pp_data["combined_fields"])

# check if field(s) are present
# required fields 
pp_data["byr"] = pp_data["combined_fields"].str.contains('byr', regex=False) 
pp_data["iyr"] = pp_data["combined_fields"].str.contains('iyr', regex=False)
pp_data["eyr"] = pp_data["combined_fields"].str.contains('eyr', regex=False)
pp_data["hgt"] = pp_data["combined_fields"].str.contains('hgt', regex=False)
pp_data["hcl"] = pp_data["combined_fields"].str.contains('hcl', regex=False)
pp_data["ecl"] = pp_data["combined_fields"].str.contains('ecl', regex=False)
pp_data["pid"] = pp_data["combined_fields"].str.contains('pid', regex=False)

# non-required fields 
pp_data["cid"] = pp_data["combined_fields"].str.contains('cid', regex=False)

# review overall matches
pp_data["pass_flg"] = np.where(((pp_data["ecl"]==True) & (pp_data["pid"]==True) & (pp_data["eyr"]==True) & (pp_data["hcl"]==True) & 
        (pp_data["byr"]==True) & (pp_data["iyr"]==True) & (pp_data["hgt"]==True)), 1, 0)

# Review matches 
sum(pp_data.pass_flg)

# PART 2 -- more detailed review
# extract contents 
# Birth Year 
pp_data["byr_text"] = pp_data["combined_fields"].str.extract(r'[byr]{3}\:([0-9]{4})').astype(float)
# Issue Year 
pp_data["iyr_text"] = pp_data["combined_fields"].str.extract(r'[iyr]{3}\:([0-9]{4})').astype(float)
# Exp Year
pp_data["eyr_text"] = pp_data["combined_fields"].str.extract(r'[eyr]{3}\:([0-9]{4})').astype(float)
# Height 
pp_data["hgt_text"] = pp_data["combined_fields"].str.extract(r'[hgt]{3}\:([0-9]{1,5}[a-z]{1,4})')
## DECOMPOSE HGT variables; i.e. hgt num / hgt type 
pp_data["hgt_num"] = pp_data["combined_fields"].str.extract(r'[hgt]{3}\:([0-9]{1,5})[a-z]{1,4}').astype(float)
pp_data["hgt_type"] = pp_data["combined_fields"].str.extract(r'[hgt]{3}\:[0-9]{1,5}([a-z]{1,4})')
# Hair Color 
pp_data["hcl_text"] = pp_data["combined_fields"].str.extract(r'[hcl]{3}\:(\#[A-z0-9]{1,10})')
# Eye Color 
pp_data["ecl_text"] = pp_data["combined_fields"].str.extract(r'[ecl]{3}\:([a-z]{2,4})')
# Pass Port ID 
pp_data["pid_text"] = pp_data["combined_fields"].str.extract(r'[pid]{3}\:([0-9]{6,12})')

# Evaluate fields

# BYR Eval
pp_data["byr_flag"] = np.where(((pp_data["byr_text"] >= 1920) & (pp_data["byr_text"] <= 2002)),True,False)
# IYR Eval
pp_data["iyr_flag"] = np.where(((pp_data["iyr_text"] >= 2010) & (pp_data["iyr_text"] <= 2020)),True,False)
# EYR Eval 
pp_data["eyr_flag"] = np.where(((pp_data["eyr_text"] >= 2020) & (pp_data["eyr_text"] <= 2030)),True,False)
# HGT Eval 
pp_data["hgt_flag"] = np.where((((pp_data["hgt_type"] == "cm") & (pp_data["hgt_num"] >= 150) & (pp_data["hgt_num"] <= 193)) | 
((pp_data["hgt_type"] == "in") & (pp_data["hgt_num"] >= 59) & (pp_data["hgt_num"] <= 76))),True,False)
# HCL Eval
pp_data["hcl_flag"] = np.where(((pp_data["hcl_text"].str.startswith("#")==True) & (pp_data["hcl_text"].str.len() == 7)),True,False)
# EVL Eval
pp_data["ecl_flag"] = np.where(pp_data["ecl_text"].isin(["amb","blu","brn","gry","grn","hzl","oth"]),True,False)
# PID Eval
pp_data["pid_flag"] = np.where((pp_data["pid_text"].str.len() == 9),True,False)


# Review 
pp_data.dtypes
pp_data.head()
print(pp_data)


pp_data["pass_flg2"] = np.where(((pp_data["byr_flag"]==True) & (pp_data["iyr_flag"]==True) & (pp_data["eyr_flag"]==True) & (pp_data["hgt_flag"]==True) & 
        (pp_data["hcl_flag"]==True) & (pp_data["ecl_flag"]==True) & (pp_data["pid_flag"]==True)), 1, 0)


sum(pp_data.pass_flg2)




