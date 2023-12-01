//! Advent of Code day 24 solution in Rust.
//! Based on @dwburer's Python solution.

use std::{fs, collections::{HashSet, VecDeque, HashMap}};

#[derive(Debug, Hash, PartialEq, Eq)]
struct Blizzard {
    x: usize,
    y: usize,
    delta: (i32, i32),
}

impl Blizzard {
    fn new(x: usize, y: usize, delta: (i32, i32)) -> Blizzard {
        Blizzard {x, y, delta}
    }

    fn get_next_state(&self, h: usize, w: usize) -> Blizzard {
        let mut x = (self.x as i32 + self.delta.0) as usize;
        let mut y = (self.y as i32 + self.delta.1) as usize;

        if x <= 0 { x = w - 2 }
        if x >= w - 1 { x = 1 }
        if y <= 0 { y = h - 2 }
        if y >= h - 1 { y = 1 }

        Blizzard {x, y, delta: self.delta.clone()}
    }
}


#[derive(Debug)]
struct State {
    blizzards: HashMap<usize, HashSet<Blizzard>>,
    w: usize,
    h: usize,
    player_point: (usize, usize),
    start_point: (usize, usize),
    end_point: (usize, usize),
}


impl State {
    // fn print(&self) {
    //     println!();
    //     let mut rows = vec![vec!['.' ; self.w]; self.h];
    //     self.blizzards.iter().for_each(|blizz| rows[blizz.y][blizz.x] = '*');
    //
    //     rows.iter().for_each(|row| println!("{}", row.iter().collect::<String>()));
    // }
    
    fn get_blizz_set_for_minute(&mut self, minute: usize) -> &HashSet<Blizzard> {
        let w = self.w.clone();
        let h = self.h.clone();

        let blizzards = &mut self.blizzards;
        if let Some(blizz_set) = blizzards.get(&minute) {
            return blizz_set;
        }

        // If the state of blizzards does not exist for this minute, compute it from the
        // previous minute.
        if let Some(set_on_prev_minute) = blizzards.get(&(minute - 1)) {

            let mut new_set: HashSet<Blizzard> = HashSet::new();
            set_on_prev_minute.iter().for_each(|blizz| {
                new_set.insert(blizz.get_next_state(h, w));
            });

            self.blizzards.insert(minute, new_set);
            self.blizzards.get(&minute).unwrap()
        } else {
            panic!();
        }
    }

    fn get_next_locations(&mut self, (x, y): (usize, usize), minute: usize) -> Vec<(usize, usize)> {
        // TODO: Get next locations based on the blizzard positions gotten for a given minute.
        let blizz_lookup = self.get_blizz_set_for_minute(minute);
        let mut blizz_points: HashSet<(usize, usize)> = HashSet::new();
        blizz_lookup.iter().for_each(|blizz| { 
            blizz_points.insert((blizz.x, blizz.y)); 
        });


        let is_below_start = (x, y) == (self.start_point.0, self.start_point.1 + 1);
        let is_above_end = (x, y) == (self.end_point.0, self.end_point.1 - 1);        
        let is_in_start_or_end = (x, y) == self.start_point || (x, y) == self.end_point;
        let possible_locations = vec![
            Some((x, y)),
            if x < self.w - 2 && !is_in_start_or_end {Some((x + 1, y))} else {None},
            if x > 1 && !is_in_start_or_end {Some((x - 1, y))} else {None},
            if y < self.h - 2 || is_above_end {Some((x, y + 1))} else {None},
            if y > 1 || is_below_start {Some((x, y - 1))} else {None},
        ];

        possible_locations
            .into_iter()
            .filter(|point| point.is_some())
            .map(|point| point.unwrap())
            .filter(|point| blizz_points.get(point).is_none())
            .collect()
    }
}



fn get_lines(file_path: &str) -> Vec<String> {
    let content = fs::read_to_string(file_path).unwrap();
    content.lines().map(|line| line.to_string()).collect()
}


fn main() {
    let input = get_lines("example.txt");
    println!("{:?}", input);

    let h = input.len();
    let w = input[0].len();

    println!("H: {h} ; W: {w}");

    let start_point = (1, 0);
    let end_point = (w - 1, h);

    let mut blizzards_at_minute_0: HashSet<Blizzard> = HashSet::new();

    let mut state = State {
        blizzards: HashMap::new(), 
        w, 
        h, 
        player_point: start_point,
        start_point,
        end_point,
    };

    for (y, row) in input.iter().enumerate() {
        for (x, char) in row.chars().enumerate() {
            if let Some(blizz) = match char {
                '>' => Some(Blizzard::new(x, y, (1, 0))),
                '<' => Some(Blizzard::new(x, y, (-1, 0))),
                'v' => Some(Blizzard::new(x, y, (0, 1))),
                '^' => Some(Blizzard::new(x, y, (0, -1))),
                _ => None,
            } {
                blizzards_at_minute_0.insert(blizz);
            }
        }
    }

    //                          x    , y     , minute
    let mut moves_queue: VecDeque<((usize, usize), usize)> = VecDeque::new();

    while moves_queue.len() > 0 {  // Mock "solve" loop where things get updated.
        // state.print();
        // Update stuff
        // TODO: Update player position -- Add moves into Queue
        let (my_pos, minute) = moves_queue.pop_front().unwrap();
        if my_pos == end_point {
            println!("Eureka! at minute {minute}");
            return;
        }

        moves_queue.extend(state.get_next_locations(my_pos, minute).into_iter().map(|location| (location, minute + 1)));

        // state.blizzards.iter_mut().for_each(|blizz| blizz.update(h, w));

        // let mut input = String::new();
        // let stdin = io::stdin();
        // stdin.read_line(&mut input);
    }
}
