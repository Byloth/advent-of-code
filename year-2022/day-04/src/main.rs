#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";

    #[test]
    fn test_solution() {
        let schedules = parse_content(TEST_INPUT);
        let redundant_schedules = count_redundant_schedules(&schedules);

        assert_eq!(redundant_schedules, 2);
    }
}

fn parse_content(content: &str) -> Vec<((i32, i32), (i32, i32))> {
    let mut result = vec![];

    for line in content.lines() {
        let mut pairs = line.split(',');

        let mut left_pair = pairs.next().unwrap().split('-');
        let mut right_pair = pairs.next().unwrap().split('-');

        result.push((
            (
                left_pair.next().unwrap()
                         .parse().unwrap(),
                left_pair.next().unwrap()
                         .parse().unwrap()
            ),
            (
                right_pair.next().unwrap()
                          .parse().unwrap(),
                right_pair.next().unwrap()
                          .parse().unwrap()
            )
        ));
    }

    return result;
}

fn is_schedule_redundant(schedule: &((i32, i32), (i32, i32))) -> bool {
    let (left, right) = schedule;

    if left.0 <= right.0 && left.1 >= right.1 {
        return true;
    }
    if right.0 <= left.0 && right.1 >= left.1 {
        return true;
    }

    return false;
}
fn count_redundant_schedules(schedules: &Vec<((i32, i32), (i32, i32))>) -> i32 {
    let mut result = 0;

    for schedule in schedules {
        if is_schedule_redundant(schedule) {
            result += 1;
        }
    }

    return result;
}

fn main() {
    let content = include_str!("input.txt");

    let schedules = parse_content(content);
    let redundant_schedules = count_redundant_schedules(&schedules);

    println!("Redundant schedules: {}", redundant_schedules);
}
