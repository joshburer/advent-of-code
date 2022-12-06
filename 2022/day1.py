def main():
    with open("day1.txt", "r") as f:
        text = f.read()

    elves = [0]
    elf = 0
    for line in text.splitlines():
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