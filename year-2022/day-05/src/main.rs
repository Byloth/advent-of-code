use std::collections::VecDeque;

use regex::{ Captures, Regex };

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    fn test_solution() {
        let (stacks, procedure) = TEST_INPUT.split_once("\n\n").unwrap();

        let procedure = parse_procedure(procedure);
        let mut lifo_stacks = parse_stacks(stacks, 3);

        procedure.iter().for_each(|instruction| instruction.execute_lifo(&mut lifo_stacks));

        let lifo_message = compose_message(&lifo_stacks);
        assert_eq!(lifo_message, "CMZ");

        let mut fifo_stacks = parse_stacks(stacks, 3);
    
        procedure.iter().for_each(|instruction| instruction.execute_fifo(&mut fifo_stacks));
    
        let fifo_message = compose_message(&fifo_stacks);
        assert_eq!(fifo_message, "MCD");
    }
}

const CRATE_SPACING: usize = 4;

#[derive(Debug)]
struct Instruction {
    size: usize,
    from: usize,
    to: usize
}
impl Instruction {
    fn from_str(value: &str) -> Self {
        fn _get_match(_captures: &Captures, _index: usize) -> usize {
            return _captures.get(_index).unwrap().as_str().parse().unwrap();
        }

        let regex = Regex::new(r"^move (\d+) from (\d+) to (\d+)$").unwrap();
        let captures = regex.captures(value).unwrap();

        return Self {
            size: _get_match(&captures, 1),
            from: _get_match(&captures, 2) - 1,
            to: _get_match(&captures, 3) - 1
        };
    }

    fn execute_fifo(&self, stacks: &mut [VecDeque<char>]) {
        let index = stacks[self.from].len() - self.size;

        for _ in 0..self.size {
            let value = stacks[self.from].remove(index).unwrap();

            stacks[self.to].push_back(value);
        }
    }
    fn execute_lifo(&self, stacks: &mut [VecDeque<char>]) {
        for _ in 0..self.size {
            let value = stacks[self.from].pop_back().unwrap();

            stacks[self.to].push_back(value);
        }
    }
}

fn parse_stacks(value: &str, size: usize) -> Vec<VecDeque<char>> {
    let mut stacks = vec![VecDeque::<char>::new(); size];
    let mut lines = value.lines().peekable();

    while let Some(line) = lines.next() {
        if lines.peek().is_none() {
            break;
        }

        let mut chars = line.chars();

        chars.next();
        for (stack_index, crate_char) in chars.step_by(CRATE_SPACING).enumerate() {
            if crate_char != ' ' {
                stacks[stack_index].push_front(crate_char);
            }
        }
    }

    return stacks;
}
fn parse_procedure(value: &str) -> Vec<Instruction> {
    return value.lines()
                .map(Instruction::from_str)
                .collect();
}

fn compose_message(stacks: &[VecDeque<char>]) -> String {
    let mut result = String::new();

    for stack in stacks {
        result.push(*stack.back().unwrap());
    }

    return result;
}

fn main() {
    let content = include_str!("input.txt");

    let (stacks, procedure) = content.split_once("\n\n").unwrap();

    let procedure = parse_procedure(procedure);
    let mut lifo_stacks = parse_stacks(stacks, 9);

    procedure.iter().for_each(|instruction| instruction.execute_lifo(&mut lifo_stacks));

    let lifo_message = compose_message(&lifo_stacks);
    println!("The LI-FO message is: {}", lifo_message);

    let mut fifo_stacks = parse_stacks(stacks, 9);

    procedure.iter().for_each(|instruction| instruction.execute_fifo(&mut fifo_stacks));

    let fifo_message = compose_message(&fifo_stacks);
    println!("The FI-FO message is: {}", fifo_message);
}
