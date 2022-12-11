import os


def get_lines(file, demo=False):
    input_name = "demo_input.txt" if demo else "input.txt"
    with open(os.path.join(os.path.dirname(file), input_name)) as f:
        return [line.replace("\n", "") for line in f.readlines()]
