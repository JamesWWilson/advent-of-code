from utils import *

# find first packet_length characters that are all different
def signal_marker(data, packet_length: int):
    signal = []
    marker = 0
    for i in range(0, len(data)):
        if i < packet_length:
            signal.append(data[i])
        else:
            signal.append(data[i])
            signal = signal[1:]
            if len(set(signal)) == packet_length:
                marker = i + 1  # add 1 to match list
                break
    return marker


# Part 1
assert signal_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
assert signal_marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
assert signal_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
assert signal_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

print(signal_marker(Input("006").read(), 4))

# Part 2
assert signal_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert signal_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert signal_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
assert signal_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
assert signal_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

print(signal_marker(Input("006").read(), 14))  # part 2
