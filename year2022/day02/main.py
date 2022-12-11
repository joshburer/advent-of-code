from year2022.utils import get_lines


def main(part=1):
    lines = get_lines(__file__)

    # Dict matching my moves to ABC moves
    to_ABC = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    shape_scores = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
    }

    # Dict of which moves beat other moves:
    move_beats = {
        "A": "C",
        "B": "A",
        "C": "B",
    }
    # Reverse it so we can get the move to beat a certain move.
    move_to_beat = {y: x for x, y in move_beats.items()}

    total_score = 0
    for round in lines:
        opponent_move = round[0]
        my_move = round[2]

        # Evaluate the meaning of the "XYZ" notation.
        if part == 1:
            my_move = to_ABC[my_move]
        elif part == 2:
            # Change the decision of which move is mine.
            if my_move == "X":
                my_move = move_beats[opponent_move]
            elif my_move == "Y":
                my_move = opponent_move
            else:
                my_move = move_to_beat[opponent_move]

        # Compute the score.
        my_score = shape_scores[my_move]

        total_score += my_score
        if opponent_move == my_move:
            total_score += 3
        elif move_beats[opponent_move] == my_move:
            total_score += 0
        else:
            total_score += 6

    print(total_score)


if __name__ == "__main__":
    main(part=1)
    main(part=2)
