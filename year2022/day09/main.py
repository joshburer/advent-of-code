from year2022.utils import get_lines


def get_distance(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    dist_x = a[0] - b[0]
    dist_y = a[1] - b[1]
    return dist_x, dist_y


def get_tail_pos(head_pos, tail_pos) -> tuple[int, int]:
    dist_x, dist_y = get_distance(head_pos, tail_pos)
    if abs(dist_x) <= 1 and abs(dist_y) <= 1:
        return tail_pos
    if dist_x:
        sign = 1 if dist_x > 0 else -1
        tail_pos = tail_pos[0] + 1 * sign, tail_pos[1]
    if dist_y:
        sign = 1 if dist_y > 0 else -1
        tail_pos = tail_pos[0], tail_pos[1] + 1 * sign

    return tail_pos


def main(part=1):
    lines = get_lines(__file__)

    rope_count = 2 if part == 1 else 10
    positions = [(0, 0)] * rope_count
    visited = {positions[-1]}

    for line in lines:
        direction, units = line.split(' ')
        units = int(units)
        for i in range(units):
            if direction == "U":
                positions[0] = positions[0][0], positions[0][1] + 1
            if direction == "D":
                positions[0] = positions[0][0], positions[0][1] - 1
            if direction == "R":
                positions[0] = positions[0][0] + 1, positions[0][1]
            if direction == "L":
                positions[0] = positions[0][0] - 1, positions[0][1]

            for j in range(1, len(positions)):
                positions[j] = get_tail_pos(positions[j-1], positions[j])

            visited.add(positions[-1])

    print(f"Total visited: {len(visited)}")


if __name__ == "__main__":
    main()
    main(part=2)
