# Puzzle 1-A 
# 12-01-2021

# Read Input Text File in 
#input = open("input.txt", "r") 
#nums = list(input.readlines())
#print(nums)
#nums.close()
import os
from enum import Enum, auto
from pprint import pprint
from typing import Generic, List, TypeVar, Union, cast

_number = '001'

class InputTypes(Enum):  # pylint: disable=too-few-public-methods
    # one solid block of text; the default
    TEXT = auto()
    # a single int
    INTEGER = auto()
    # tab-separated values.
    TSV = auto()
    # str[], split by a specified separator (default newline)
    STRSPLIT = auto()
    # int[], split by a split by a specified separator (default newline)
    INTSPLIT = auto()


InputType = Union[str, int, List[int], List[str]]

def read_input(self) -> InputType:
        with open(
            os.path.join(
                os.path.dirname(__file__), f"/day_{self.number}/input.txt"
            ),
        ) as file:
            if self.input_type is InputTypes.TEXT:
                return file.read().strip()


t = read_input()
print(t)

