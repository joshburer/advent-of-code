use std::collections::HashMap;
use std::fs;

#[derive(PartialEq, Eq, Hash, Debug, Clone, Copy)]
enum Moves {
    Rock,
    Paper,
    Scissors,
}

use Moves::{Paper, Rock, Scissors};

/// Converts an input move into "Rock, Paper, Scissors."
/// For part 2, this should not be used for "X", "Y", "Z" inputs.
fn convert(input: &str) -> Moves {
    match input {
        "A" | "X" => Rock,
        "B" | "Y" => Paper,
        "C" | "Z" => Scissors,
        _ => unreachable!(),
    }
}

const WINS_AGAINST: [(Moves, Moves); 3] = [
    (Rock, Scissors), 
    (Paper, Rock), 
    (Scissors, Paper)
];

fn get_wins_against_hashmap() -> HashMap<Moves, Moves> {
    HashMap::from(WINS_AGAINST)
}

fn get_loses_against_hashmap() -> HashMap<Moves, Moves> {
    HashMap::from(WINS_AGAINST.map(|(a, b)| (b, a)))
}

fn game_score(my_move: &Moves, opponent_move: &Moves) -> u32 {
    // I win.
    if get_wins_against_hashmap().get(my_move).unwrap() == opponent_move {
        return 6;
    }

    // Tie.
    if my_move == opponent_move {
        return 3;
    }

    // Lose.
    0
}

/// Get the move for a desired outcome against an opponents move.
fn get_my(xyz: &str, opponent_move: &Moves) -> Moves {
    if xyz == "X" {
        return *get_wins_against_hashmap().get(opponent_move).unwrap();
    }

    if xyz == "Y" {
        return *opponent_move;
    }

    *get_loses_against_hashmap().get(opponent_move).unwrap()
}

fn main() {
    let contents = fs::read_to_string("src/input.txt").unwrap();
    let lines: Vec<&str> = contents.lines().collect();

    let pairs: Vec<(&str, &str)> = lines
        .iter()
        .map(|s| s.split(" ").collect::<Vec<&str>>())
        .map(|p| (p[0], p[1]))
        .collect();

    let point_table = HashMap::from([(Rock, 1), (Paper, 2), (Scissors, 3)]);

    let mut total = 0;
    for pair in pairs {
        let (raw_op, raw_my) = pair;
        let opponent_move = convert(raw_op);
        let my_move = get_my(raw_my, &opponent_move);

        println!("{:?}", (opponent_move, my_move));

        let choice_points = point_table.get(&my_move).unwrap();
        let outcome_points = game_score(&my_move, &opponent_move);

        total += choice_points + outcome_points
    }

    println!("{:?}", total);
}
