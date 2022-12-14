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
        let redundant_schedules = count_redundant_schedules(&schedules, is_schedule_redundant);

        assert_eq!(redundant_schedules, 2);

        let overlapping_schedules = count_redundant_schedules(&schedules, is_schedule_overlapping);

        assert_eq!(overlapping_schedules, 4);
    }
}

type Schedule = (i32, i32);
type SchedulePair = (Schedule, Schedule);

fn parse_content(content: &str) -> Vec<SchedulePair> {
    let mut result: Vec<SchedulePair> = vec![];

    for line in content.lines() {
        let pairs = line.split_once(',').unwrap();

        let left_pair = pairs.0.split_once('-').unwrap();
        let right_pair = pairs.1.split_once('-').unwrap();

        result.push((
            (left_pair.0.parse().unwrap(), left_pair.1.parse().unwrap()),
            (right_pair.0.parse().unwrap(), right_pair.1.parse().unwrap())
        ));
    }

    return result;
}

fn is_schedule_redundant(schedule: &SchedulePair) -> bool {
    let (left, right) = schedule;

    if left.0 <= right.0 && left.1 >= right.1 {
        return true;
    }
    if right.0 <= left.0 && right.1 >= left.1 {
        return true;
    }

    return false;
}
fn is_schedule_overlapping(schedule: &SchedulePair) -> bool {
    let (left, right) = schedule;

    if left.0 <= right.0 && left.1 >= right.0 {
        return true;
    }
    if right.0 <= left.0 && right.1 >= left.0 {
        return true;
    }

    return false;
}

fn count_redundant_schedules(schedules: &Vec<SchedulePair>, check_fn: fn(&SchedulePair) -> bool) -> i32 {
    let mut result = 0;

    for schedule in schedules {
        if check_fn(schedule) {
            result += 1;
        }
    }

    return result;
}

fn main() {
    let content = include_str!("input.txt");

    let schedules = parse_content(content);
    let redundant_schedules = count_redundant_schedules(&schedules, is_schedule_redundant);

    println!("Redundant schedules: {}", redundant_schedules);

    let overlapping_schedules = count_redundant_schedules(&schedules, is_schedule_overlapping);

    println!("Overlapping schedules: {}", overlapping_schedules);
}
