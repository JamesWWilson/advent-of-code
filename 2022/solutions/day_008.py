from utils import *


def make_trees(data):
    trees = []
    l = 0
    for line in data:
        trees.append([])
        for t in range(0, len(line)):
            # create list that stores the tree size and flag if its visible
            if int(line[t]) == 0:
                t_data = [0.1, 0, 0, 0, 0, 0]
            else:
                t_data = [int(line[t]), 0, 0, 0, 0, 0]
            trees[l].append(t_data)
        l += 1
    width = len(trees[0])
    height = l
    # print(width, height)
    return (trees, width, height)


def search_left(trees, width, height):
    # left to the right
    left = [0] * width
    for w in range(0, width):
        for h in range(0, height):
            # part 1
            if trees[w][h][0] > left[w]:
                left[w] = trees[w][h][0]
                trees[w][h][1] += 1

            prev = trees[w][h][0]

    return trees


def search_up(trees, width, height):
    # bottom left up
    up = [0] * height
    for w in range(width - 1, -1, -1):
        for h in range(0, height):
            # part 1
            if trees[w][h][0] > up[h]:
                up[h] = trees[w][h][0]
                trees[w][h][1] += 1
            # print("status post", up)

    return trees


def search_down(trees, width, height):
    # top right down
    down = [0] * height
    for w in range(0, width):
        for h in range(height - 1, -1, -1):
            # part 1
            if trees[w][h][0] > down[h]:
                down[h] = trees[w][h][0]
                trees[w][h][1] += 1

    return trees


def search_right(trees, width, height):
    ## top right to right
    right = [0] * width
    for w in range(width - 1, -1, -1):
        for h in range(height - 1, -1, -1):
            # part 1
            if trees[w][h][0] > right[w]:
                right[w] = trees[w][h][0]
                trees[w][h][1] += 1

    return trees


def num_visible(trees, width, height):
    visible = 0
    for w in range(0, width):
        for h in range(0, height):
            if trees[w][h][1] > 0:
                visible += 1
    return visible


def score_trees(trees, width, height):
    for i in range(0, width):
        for j in range(0, height):
            # for each square in block
            # print("main_sq", i, j)
            # use height and look LEFT
            for l in range(1, height):
                if j - l >= 0:
                    if trees[i][j - l][0] < trees[i][j][0]:
                        trees[i][j][2] += 1
                    else:
                        trees[i][j][2] += 1
                        break

            # use height and look RIGHT
            for r in range(1, height):
                if j + r < height:
                    if trees[i][j + r][0] < trees[i][j][0]:
                        trees[i][j][3] += 1
                    else:
                        trees[i][j][3] += 1
                        break

            # use width look UP
            for u in range(1, height):
                if i - u >= 0:

                    if trees[i - u][j][0] < trees[i][j][0]:
                        trees[i][j][4] += 1
                    else:
                        trees[i][j][4] += 1
                        break

            # use width look DOWN
            for d in range(1, height):
                if i + d < width:
                    if trees[i + d][j][0] < trees[i][j][0]:
                        trees[i][j][5] += 1
                    else:
                        trees[i][j][5] += 1
                        break
    return trees


def quality_score(trees, width, height):
    max_score = 0
    for w in range(0, width):
        for h in range(0, height):
            score = trees[w][h][2] * trees[w][h][3] * trees[w][h][4] * trees[w][h][5]
            if score > max_score:
                max_score = score
    return max_score


def part1(input):
    trees_obj = make_trees(input)
    trees = trees_obj[0]
    width = trees_obj[1]
    height = trees_obj[2]

    trees = search_left(trees, width, height)
    trees = search_up(trees, width, height)
    trees = search_right(trees, width, height)
    trees = search_down(trees, width, height)
    total = num_visible(trees, width, height)
    trees = score_trees(trees, width, height)
    return total


def part2(input):
    trees_obj = make_trees(input)
    trees = trees_obj[0]
    width = trees_obj[1]
    height = trees_obj[2]

    trees = search_left(trees, width, height)
    trees = search_up(trees, width, height)
    trees = search_right(trees, width, height)
    trees = search_down(trees, width, height)

    trees = score_trees(trees, width, height)
    max_score = quality_score(trees, width, height)

    return max_score


# TEST
test = ["30373", "25512", "65332", "33549", "35390"]
assert part1(test) == 21
assert part2(test) == 8


# SOLUTION
print(part1(Input("008").read().splitlines()))  # part 1 = 1807
print(part2(Input("008").read().splitlines()))  # part 2 = 480000
