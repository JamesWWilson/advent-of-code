from utils import *

# # Sum lines in a text file and append to list when blank line appears
def calibration_value(data):
    overall_total = 0 
    for line in data:
        first_digit = None
        last_digit = None

        # Iterate through each character in the string
        for char in line:
            # Check if the character is a digit
            if char.isdigit():
                # If first_digit is not set yet, set it
                if first_digit is None:
                    first_digit = char
                # Update last_digit with the current character in each iteration
                last_digit = char
     
        line_total = int(first_digit + last_digit)
        overall_total += line_total

    return overall_total


# # function to return the sum of the largest [x] items in a list
# def sum_top_x(list, x):
#     top_x = sorted(list, reverse=True)[:x]
#     if x > 1:
#         top_x = sum(top_x)
#     return top_x



# Load input and solve
input = Input("001").readlines()
print(input)  # solution 1a


print(calibration_value(input))  # solution 1a
# print(sum_top_x(calc_calories(input), 3))  # solution 1b


# 1rxfour4xjzdfgqsixmjvvzfnh6m
# zvcfive2eight5hghsix19
# 44two1
# 3nxlmh448two899