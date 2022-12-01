use std::fs;

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    fn test_sum() {
        let elves = parse_content(TEST_INPUT);
        let elves = sum_elves_calories(&elves);
        let hungriest_elf = find_hungriest_elf(&elves);

        assert_eq!(hungriest_elf, 24000);
    }
}

fn parse_content(content: &str) -> Vec<Vec<i32>> {
    let mut elves = Vec::<Vec<i32>>::new();

    for elf in content.split("\n\n") {
        let mut inventory = Vec::<i32>::new();

        for calories in elf.split("\n") {
            inventory.push(calories.parse().unwrap());
        }

        elves.push(inventory);
    }

    return elves;
}
fn sum_elves_calories(inventories: &Vec<Vec<i32>>) -> Vec<i32> {
    let mut elves = Vec::<i32>::new();

    for inventory in inventories {
        let mut total_calories = 0;

        for calories in inventory {
            total_calories += calories;
        }

        elves.push(total_calories);
    }

    return elves;
}
fn find_hungriest_elf(elves: &Vec<i32>) -> i32 {
    let mut hungriest_elf = 0;

    for elf in elves {
        if elf > &hungriest_elf {
            hungriest_elf = *elf;
        }
    }

    return hungriest_elf;
}

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the input file.");

    let elves = parse_content(&content);
    let elves = sum_elves_calories(&elves);
    let hungriest_elf = find_hungriest_elf(&elves);

    println!("{:?}", hungriest_elf);
}
