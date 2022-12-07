#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    fn test_solution() {
        let backpacks = parse_content(TEST_INPUT);

        let result = sum_priorities(&backpacks);
        assert_eq!(result, 157);
    }
}

const GROUP_SIZE: usize = 3;

fn parse_content(content: &str) -> Vec<(&str, &str)> {
    let mut backpacks = vec![];

    for items in content.split("\n") {
        let index = items.len() / 2;

        let left = &items[..index];
        let right = &items[index..];

        backpacks.push((left, right));
    }

    return backpacks;
}

fn split_into_groups(backpacks: &Vec<(&str, &str)>) -> Vec<&[&(&str, &str)]> {
    let length = backpacks.len();
    let mut groups = vec![];

    for index in (0..length).step_by(GROUP_SIZE) {
        let group = &backpacks[index..index + GROUP_SIZE];
    
        groups.push(group);
    }

    return groups;
}

fn find_duplicate_item(backpack: (&str, &str)) -> Option<char> {
    for item in backpack.0.chars() {
        if backpack.1.contains(item) {
            return Some(item);
        }
    }
    
    return None;
}

fn compute_priority(item: char) -> i32 {
    let ascii_value = item as i32;

    if ascii_value >= 97 {
        return ascii_value - 96;
    }

    return ascii_value - 38;
}
fn sum_priorities(backpacks: &Vec<(&str, &str)>) -> i32 {
    let mut sum = 0;

    for backpack in backpacks {
        if let Some(item) = find_duplicate_item(*backpack) {
            sum += compute_priority(item);
        }
    }

    return sum;
}

fn main() {
    let content = include_str!("input.txt");

    let backpacks = parse_content(content);
    let priorities_sum = sum_priorities(&backpacks);

    println!("Sum of priorities: {}", priorities_sum);
}
