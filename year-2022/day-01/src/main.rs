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
    fn test_solution() {
        let elves = parse_content(TEST_INPUT);
        let mut elves = sum_elves_calories(&elves);
        let elves = sort_elves(&mut elves);
    
        assert_eq!(elves[0], 24000);
    
        let top_3_hungriest = elves[0] + elves[1] + elves[2];

        assert_eq!(top_3_hungriest, 45000);
    }
}

fn parse_content(content: &str) -> Vec<Vec<i32>> {
    let mut elves = vec![];

    for elf in content.split("\n\n") {
        let mut inventory = vec![];

        for calories in elf.split('\n') {
            inventory.push(calories.parse().unwrap());
        }

        elves.push(inventory);
    }

    return elves;
}
fn sum_elves_calories(inventories: &Vec<Vec<i32>>) -> Vec<i32> {
    let mut elves = vec![];

    for inventory in inventories {
        let mut total_calories = 0;

        for calories in inventory {
            total_calories += calories;
        }

        elves.push(total_calories);
    }

    return elves;
}
fn sort_elves(elves: &mut Vec<i32>) -> &mut Vec<i32> {
    elves.sort();
    elves.reverse();

    return elves;
}

fn main() {
    let content = include_str!("input.txt");

    let elves = parse_content(content);
    let mut elves = sum_elves_calories(&elves);
    let elves = sort_elves(&mut elves);

    println!("Hungriest: {}", elves[0]);

    let top_3_hungriest = elves[0] + elves[1] + elves[2];

    println!("Sum of the Top 3 hungriest: {}", top_3_hungriest);
}
