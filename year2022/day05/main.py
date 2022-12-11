from year2022.utils import get_lines


def main(part=1):
    lines = get_lines(__file__)

    # Extract numbers from lines.
    number_lines = []
    for idx, line in enumerate(lines):
        numbers = [int(x) for x in filter(lambda x: bool(x), line.split(' ')) if x.isnumeric()]
        if numbers:
            number_lines.append((idx, numbers))

    # The first line with numbers enumerates the stacks.
    number_line_idx, number_line =  number_lines[0]
    stack_count = len(number_line)
    stacks = []
    for _ in range(stack_count):
        stacks.append([])

    # Fill the stacks with items. Go by column.
    for idx, stack in enumerate(stacks):
        for stack_line in lines[:number_line_idx]:
            char = stack_line[idx * 4 + 1]
            if char.isalpha():
                stack.append(char)

    # Reverse the stacks.
    stacks = [stack[::-1] for stack in stacks]

    # Handle the number lines that specify the move operations.
    for line in number_lines[1:]:
        move_count, from_stack, to_stack = line[1]
        from_stack = stacks[from_stack - 1]
        to_stack = stacks[to_stack - 1]

        if part == 1:
            for _ in range(move_count):
               to_stack.append(from_stack.pop())
        else:
            to_stack += from_stack[-move_count:]
            from_stack[::] = from_stack[:-move_count]

    print("".join([stack[-1] for stack in stacks]))


if __name__ == "__main__":
    main()
    main(part=2)
