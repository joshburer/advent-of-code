from year2022.utils import get_lines


def main():
    lines = get_lines(__file__, demo=False)
    x_at_cycle = [1] * 242
    cycle = 1

    for line in lines:
        if line.startswith("addx"):
            _, count = line.split(' ')
            count = int(count)

            prev_cycle = cycle
            x = x_at_cycle[prev_cycle]

            cycle += 2

            x_at_cycle[prev_cycle:cycle] = [x] * (cycle - prev_cycle)
            x_at_cycle[cycle] = x + count
        else:
            cycle += 1
            x_at_cycle[cycle] = x_at_cycle[cycle-1]

    print(x_at_cycle)

    print(sum(x * x_at_cycle[x] for x in [20, 60, 100, 140, 180, 220]))

    for idx, value in enumerate(x_at_cycle[1:241]):
        if (idx + 1) % 40 == 1:
            print("")
        offset = (idx // 40) * 40
        if abs((idx - offset) - value) < 2:
            print("#", end="")
        else:
            print(".", end="")


if __name__ == "__main__":
    main()
