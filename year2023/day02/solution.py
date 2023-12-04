with open("final_input.txt") as file:
    lines = file.readlines()

total_ids = 0
total_powers = 0

max_contents = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for game in lines:
    # Split out the Game ID:
    id_str, game_contents = game.split(": ")
    game_id = int(id_str[5:])

    game_ok = True

    rounds = game_contents.split("; ")

    max_counts_for_game = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for game_round in rounds:
        ok = True

        for item in game_round.split(", "):
            count, color = item.split(' ')
            count = int(count)
            if count > max_contents[color.strip()]:
                ok = False

            if count > max_counts_for_game[color.strip()]:
                max_counts_for_game[color.strip()] = count

        if not ok:
            game_ok = False

    game_power = max_counts_for_game["red"] * max_counts_for_game["green"] * max_counts_for_game["blue"]
    total_powers += game_power

    if game_ok:
        total_ids += game_id


print(total_ids, total_powers)
