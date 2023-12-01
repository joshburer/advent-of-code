use std::fs;

fn main() {
    let input = fs::read_to_string("src/demo_input.txt").unwrap();
    let mut totals: Vec<u32> = Vec::new();

    let nums = input
        .lines()
        .map(|line| line.parse::<u32>().unwrap_or_else(|_| 0));

    nums.fold(0, |acc, e| {
        if e == 0 {
            totals.push(acc);
            return 0;
        }
        acc + e
    });

    totals.sort();
    totals.iter().rev().take(3).for_each(|e| println!("{e}"));
}
