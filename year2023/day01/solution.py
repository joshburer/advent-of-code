words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("src/input/final_input.txt") as file:
    lines = file.readlines()

    total = 0
    for line in lines:
        first = 0
        last = 0

        found_first = False
        found_last = False
        for idx, char in enumerate(line):
            if found_first:
                # print(f"breaking with found {first} in {line}")
                break

            if char.isnumeric():
                first = int(char)
                break

            for key in words.keys():
                substr = line[idx: idx + len(key)]
                if substr == key:
                    # print(f"Found {substr}")
                    first = words[key]
                    found_first = True
                    break

        for idx, char in enumerate(reversed(line)):
            if found_last:
                print(f"breaking with found {last} in {line}")
                break

            if char.isnumeric():
                last = int(char)
                break

            for key in words.keys():

                substr = line[::-1][idx: idx + len(key)]
                print(substr)
                if substr == key[::-1]:
                    print(f"Found {substr}")
                    last = words[key]
                    found_last = True
                    break

        total += first * 10 + last

    print(total)
