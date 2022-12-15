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
        let (mut stacks, procedure) = parse_content(TEST_INPUT, 3);

        run_procudure(&mut stacks, &procedure);

        let message = get_last_crates(&stacks);
        assert_eq!(message, "CMZ");
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

    fn execute(&self, stacks: &mut [VecDeque<char>]) {
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

fn parse_content(content: &str, stacks_number: usize) -> (Vec<VecDeque<char>>, Vec<Instruction>) {
    let (stacks, procedure) = content.split_once("\n\n").unwrap();

    let stacks = parse_stacks(stacks, stacks_number);
    let procedure = parse_procedure(procedure);

    return (stacks, procedure);
}

fn run_procudure(stacks: &mut [VecDeque<char>], procedure: &Vec<Instruction>) {
    for instruction in procedure {
        instruction.execute(stacks);
    }
}

fn get_last_crates(stacks: &[VecDeque<char>]) -> String {
    let mut result = String::new();

    for stack in stacks {
        result.push(*stack.back().unwrap());
    }

    return result;
}

fn main() {
    let content = include_str!("input.txt");

    let (mut stacks, procedure) = parse_content(&content, 9);

    run_procudure(&mut stacks, &procedure);

    let message = get_last_crates(&stacks);
    println!("The message is: {}", message);
}
