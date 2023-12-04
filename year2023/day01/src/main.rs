use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() -> std::io::Result<()> {
    let f = File::open("src/input/final_input.txt")?;
    let lines = BufReader::new(f).lines();

    let mut total = 0;

    for line in lines {
        let line = line?;
        let mut first_digit: usize = 0;
        let mut last_digit: usize = 0;

        for i in 0..line.len() {
            let c: char = line.as_bytes()[i] as char;
            print!("{}", c);
        }

        // Part 1: First char last char
        for char in line.chars() {
            if char.is_numeric() {
                first_digit = char.to_digit(10).unwrap() as usize;
                break;
            }
        }

        for char in line.chars().rev() {
            if char.is_numeric() {
                last_digit = char.to_digit(10).unwrap() as usize;
                break;
            }
        }



        let sum = first_digit * 10 + last_digit;
        println!("{}", first_digit * 10 + last_digit);
        total += sum;
    }

    println!("Total: {}", total);

    Ok(())
}
