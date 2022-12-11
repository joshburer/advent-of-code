from year2022.utils import get_lines


def main():
    lines = get_lines(__file__)

    elves = [0]
    elf = 0
    for line in lines:
        if line.isnumeric():
            elves[elf] += int(line)
        else:
            elf += 1
            elves.append(0)

    # Part 1: Get the elf with the most calories.
    print(max(elves))

    # Part 2: Get the top three, and sum them.
    elves.sort()
    print(sum(elves[-3:]))


if __name__ == "__main__":
    main()
