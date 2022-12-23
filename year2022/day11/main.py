from year2022.utils import get_lines


def main(part=1):
    lines = get_lines(__file__, demo=True)

    monkeys = {}

    for i in range(0, len(lines), 7):
        monkeys[i // 7] = {
            "items": eval(f"[{lines[i + 1][18:]}]"),
            "operation": eval(f"lambda old: {lines[i+2][18:]}"),
            "test_divisible_by": int(lines[i + 3][21:]),
            "true_throw_to": int(lines[i + 4][-1]),
            "false_throw_to": int(lines[i + 5][-1]),
            "total_inspections": 0
        }

    for game_round in range(20 if part == 1 else 10_000):
        print(f"{game_round=}")
        for num, monkey in monkeys.items():
            new_items = [*monkey['items']]
            for item in monkey['items']:
                monkey["total_inspections"] += 1
                item = monkey['operation'](item)
                if part == 1:
                    item = item // 3
                if item % monkey["test_divisible_by"] == 0:
                    new_items.pop(0)
                    monkeys[monkey["true_throw_to"]]["items"].append(item)
                else:
                    new_items.pop(0)
                    monkeys[monkey["false_throw_to"]]["items"].append(item)
            monkey['items'] = new_items

    print(monkeys)

    highest_2 = [x["total_inspections"] for _, x in monkeys.items()]
    highest_2.sort()
    print(highest_2[-2:])


if __name__ == "__main__":
    main(part=1)
