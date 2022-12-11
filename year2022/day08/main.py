from year2022.utils import get_lines


def main():
    lines = get_lines(__file__)

    trees = [[  # Up,    Down,  Left,  Right
        (int(l), [False, False, False, False]) for l in line
    ] for line in lines]
    # Can now use trees[row][col][0] to get values

    # Go by column
    for col in range(len(trees[0])):
        highest_from_top = -1

        for row in range(len(trees)):
            curr = trees[row][col]
            val = curr[0]
            if val > highest_from_top:
                highest_from_top = val
                curr[1][0] = True

        highest_from_bottom = -1

        for row in range(len(trees) - 1, -1, -1):
            curr = trees[row][col]
            val = curr[0]
            if val > highest_from_bottom:
                highest_from_bottom = val
                curr[1][1] = True

    # Go by row
    for row in trees:
        highest_from_left = -1

        for col in range(len(row)):
            curr = row[col]
            val = curr[0]
            if val > highest_from_left:
                highest_from_left = val
                curr[1][2] = True

        highest_from_right = -1

        for col in range(len(row) - 1, -1, -1):
            curr = row[col]
            val = curr[0]
            if val > highest_from_right:
                highest_from_right = val
                curr[1][3] = True

    print(sum([sum([1 for col in row if any(col[1])]) for row in trees]))


if __name__ == "__main__":
    main()
