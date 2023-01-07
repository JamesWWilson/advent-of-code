from utils import *
import copy
from time import sleep
from tqdm import tqdm

input_test = Input("011_test").read().splitlines()
input = Input("011").read().splitlines()


class Monkey:
    def __init__(self, name):
        self.name: str = name
        self.items: list = []
        self.item_function: int = 0
        self.item_equation: str = "+"
        self.test_divisor: int = 1
        self.pass_action: list = []
        self.inspection_counter: int = (
            0  # used to count number of items reviewed by monkey
        )

    def __repr__(self):
        return self.name

    def see(self):
        return [
            self.name,
            self.items,
            self.item_function,
            self.item_equation,
            self.test_divisor,
            self.pass_action,
        ]

    def see_inspection_counter(self):
        return self.inspection_counter

    def see_test_divisor(self):
        return self.test_divisor

    # operating functions
    def add_item(self, item):
        self.items.append(item)

    def update_item_function(self, input):
        self.item_function = input

    def update_item_equation(self, input):
        self.item_equation = input

    def update_test_divisor(self, input):
        self.test_divisor = input

    def update_pass_action(self, action):
        self.pass_action.append(action)

    def inspect_items(self, barrel, divisor):
        for i in self.items:
            self.inspection_counter += 1
            # can clean this up by decomposing on the i to just set over self.item_function
            if divisor == 3:
                if self.item_function != 0:
                    if self.item_equation == "+":
                        i_new = math.floor((i + self.item_function) // divisor)
                    elif self.item_equation == "*":
                        i_new = math.floor((i * self.item_function) // divisor)
                    else:
                        i_new = "error"
                else:
                    if self.item_equation == "+":
                        i_new = math.floor((i + i) // divisor)
                    elif self.item_equation == "*":
                        i_new = math.floor((i * i) // divisor)
                    else:
                        i_new = "error"
            else:
                if self.item_function != 0:
                    if self.item_equation == "+":
                        i_new = math.floor((i + self.item_function) % divisor)
                    elif self.item_equation == "*":
                        i_new = math.floor((i * self.item_function) % divisor)
                    else:
                        i_new = "error"
                else:
                    if self.item_equation == "+":
                        i_new = math.floor((i + i) % divisor)
                    elif self.item_equation == "*":
                        i_new = math.floor((i * i) % divisor)
                    else:
                        i_new = "error"

            # check if i_new is divisible by test_divisor
            if (i_new % self.test_divisor) == 0:
                # TRUE, move to monkey [0]
                pass_item(barrel, self.pass_action[0], i_new)
            else:
                # FALSE, move to monkey [1]
                pass_item(barrel, self.pass_action[1], i_new)
        self.items = []


def pass_item(barrel, monkey_num, item):
    barrel[monkey_num].add_item(item)


def create_monkeys(data):
    barrel = []
    for line in data:
        print(line.strip())
        if len(line) > 0:
            if line.strip()[0] == "M":
                # define monkey object
                m_name = re.findall(r"\d+", line)[0]
                current_monkey = Monkey(name=m_name)
            elif line.strip()[0] == "S":
                # append to current monkey
                items = re.findall(r"\d+", line)
                for i in items:
                    current_monkey.add_item(int(i))
            elif line.strip()[0] == "O":
                # set item_function
                print(re.findall(r"\d+", line))
                if len(re.findall(r"\d+", line)) > 0:
                    value_fnc = int(re.findall(r"\d+", line)[0])
                    current_monkey.update_item_function(value_fnc)
                if len(re.findall(r"\+|\*", line)) > 0:
                    value_eq = re.findall(r"\+|\*", line)[0]
                    current_monkey.update_item_equation(value_eq)
            elif line.strip()[0] == "T":
                # set test_divisor
                value = int(re.findall(r"\d+", line)[0])
                current_monkey.update_test_divisor(value)
            elif line.strip()[0:7] == "If true":
                # set '0' in pass action
                value = int(re.findall(r"\d+", line)[0])
                current_monkey.update_pass_action(value)
            elif line.strip()[0:8] == "If false":
                # set '1' in pass action
                value = int(re.findall(r"\d+", line)[0])
                current_monkey.update_pass_action(value)
        else:
            # append monkeys to list
            barrel.append(copy.deepcopy(current_monkey))
    # for i in barrel:
    #     print(i.see())
    return barrel


def monkey_business(round_cnt, divisor):
    barrel = create_monkeys(input)
    # calculate common multiple of monkey divisors
    if divisor == "common_modulo":
        common_mod = 1
        for m in barrel:
            common_mod *= m.see_test_divisor()
        divisor = common_mod

    for _ in tqdm(range(0, round_cnt)):
        for m in barrel:
            m.inspect_items(barrel, divisor)
        sleep(0.01)

    # return max monkey buisness
    mbiz = []
    for m in barrel:
        mbiz.append(m.see_inspection_counter())
    mbiz1 = max(mbiz)
    mbiz.remove(mbiz1)
    mbiz2 = max(mbiz)
    print(mbiz1 * mbiz2)


monkey_business(round_cnt=20, divisor=3)
monkey_business(round_cnt=10000, divisor="common_modulo")
