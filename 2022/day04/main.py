def main(part=1):
    with open('input.txt', 'r') as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    pairs = [[[int(y) for y in x.split('-')] for x in line.split(',')] for line in lines]

    total = 0
    for pair in pairs:
        first, second = pair
        first = set(range(first[0], first[1] + 1))
        second = set(range(second[0], second[1] + 1))

        if part == 1:
            if len(first.intersection(second)) in {len(first), len(second)}:
                total += 1
        else:
            if len(first.intersection(second)):
                total += 1
    print(total)

if __name__ == "__main__":
    main()
    main(part=2)
