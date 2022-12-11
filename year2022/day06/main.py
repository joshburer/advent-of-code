def main(part=1):
    with open('day06/input.txt', 'r') as f:
        data = f.read()

    n = 4 if part == 1 else 14

    last_n = data[:n]
    for i, l in enumerate(data):
        last_n = last_n[1:] + l
        if len(set(last_n)) == n:
            print(i + 1, l, last_n)
            break


if __name__ == "__main__":
    main()
    main(part=2)