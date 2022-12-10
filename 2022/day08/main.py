def main():
    with open("demo_input.txt", "r") as f:
        lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))

    trees = [[int(l) for l in line] for line in lines]
    # Can now use trees[row][col] to get values
    print(trees)


if __name__ == "__main__":
    main()