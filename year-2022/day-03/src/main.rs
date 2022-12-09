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
        let compartments = split_into_compartments(&backpacks);

        let duplicates_sum = sum_duplicates_priority(&compartments);
        assert_eq!(duplicates_sum, 157);

        let groups = split_into_groups(&backpacks);
        let badges_sum = sum_badges_priority(&groups);
        assert_eq!(badges_sum, 70);
    }
}

const GROUP_SIZE: usize = 3;

fn parse_content(content: &str) -> Vec<&str> {
    let mut backpacks = vec![];

    for items in content.split('\n') {
        backpacks.push(items);
    }

    return backpacks;
}

fn split_into_compartments<'a>(backpacks: &'a [&str]) -> Vec<(&'a str, &'a str)> {
    let mut compartments = vec![];

    for items in backpacks {
        let index = items.len() / 2;

        let left = &items[..index];
        let right = &items[index..];

        compartments.push((left, right));
    }

    return compartments;
}
fn split_into_groups<'a>(backpacks: &'a [&str]) -> Vec<Vec<&'a str>> {
    let mut groups = vec![];

    for chunk in backpacks.chunks(GROUP_SIZE) {
        groups.push(chunk.to_vec());
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
fn find_group_badge(group: &[&str]) -> Option<char> {
    fn _recursive_search(_group: &[&str], _look_for: char) -> Option<char> {
        let _current = _group[0];

        if _group[0].contains(_look_for) {
            if _group.len() == 1 {
                return Some(_look_for);
            } else {
                return _recursive_search(&_group[1..], _look_for);
            }
        }

        return None;
    }

    for character in group[0].chars() {
        if let Some(result) = _recursive_search(&group[1..], character) {
            return Some(result);
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

fn sum_duplicates_priority(backpacks: &[(&str, &str)]) -> i32 {
    let mut sum = 0;

    for compartments in backpacks {
        if let Some(item) = find_duplicate_item(*compartments) {
            sum += compute_priority(item);
        }
    }

    return sum;
}
fn sum_badges_priority(groups: &[Vec<&str>]) -> i32 {
    let mut sum = 0;

    for group in groups {
        if let Some(item) = find_group_badge(group) {
            sum += compute_priority(item);
        }
    }

    return sum;
}

fn main() {
    let content = include_str!("input.txt");

    let backpacks = parse_content(content);
    let compartments = split_into_compartments(&backpacks);
    let duplicates_sum = sum_duplicates_priority(&compartments);

    println!("Sum of duplicates priority: {}", duplicates_sum);

    let groups = split_into_groups(&backpacks);
    let badges_sum = sum_badges_priority(&groups);

    println!("Sum of badges priority: {}", badges_sum);
}
