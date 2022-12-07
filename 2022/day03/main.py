def main(part=1):
    with open("2022/day03/input.txt", "r") as f:
        lines = f.readlines()

    lines = [line.replace('\n', '') for line in lines]

    def char_to_priority(char: str) -> int:
        """Convert a single character to the corresponding value:

        1-26 for lowercase letters, 27-52 for uppercase letters.
        """
        priority = 0
        val = ord(char)
        if ord('a') <= val <= ord('z'):
            priority = val - ord('a') + 1
        elif ord('A') <= val <= ord('Z'):
            priority = val - ord('A') + 27

        return priority

    total = 0
    if part == 1:
        # Every line has one character common to both halves of the string.
        for line in lines:
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]
            intersection = set(first_half) & set(second_half)
            item = intersection.pop()
            total += char_to_priority(item)
    else:
        # Every 3 lines have 1 character common to all three.
        groups = []
        for i, line in enumerate(lines):  # Make a list of groups of 3 lines.
            if (i+1) % 3 == 0 and not i < 2:
                groups.append(lines[i-2:i+1])

        for group in groups:
            intersection = set(group[0]) & set(group[1]) & set(group[2])
            total += char_to_priority(intersection.pop())

    print(total)


if __name__ == "__main__":
    main()
    main(part=2)