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
        let redundant_schedules = schedules.iter()
                                                  .filter(|pair| pair.is_redundant())
                                                  .count();

        assert_eq!(redundant_schedules, 2);

        let overlapping_schedules = schedules.iter()
                                                    .filter(|pair| pair.is_overlapping())
                                                    .count();

        assert_eq!(overlapping_schedules, 4);
    }
}

#[derive(Debug)]
struct Schedule {
    start: i32,
    end: i32
}
impl Schedule {
    fn from_str(value: &str) -> Self {
        let (start, end) = value.split_once('-').unwrap();

        return Self {
            start: start.parse().unwrap(),
            end: end.parse().unwrap()
        };
    }

    fn contains(&self, other: &Schedule) -> bool {
        return self.start <= other.start && other.end <= self.end;
    }
    fn overlaps(&self, other: &Schedule) -> bool {
        return self.start <= other.start && other.start <= self.end;
    }
}

#[derive(Debug)]
struct SchedulePair {
    left: Schedule,
    right: Schedule
}
impl SchedulePair {
    fn from_str(value: &str) -> Self {
        let pairs = value.split_once(',').unwrap();

        return Self {
            left: Schedule::from_str(pairs.0),
            right: Schedule::from_str(pairs.1)
        };
    }

    fn is_overlapping(&self) -> bool {
        return self.left.overlaps(&self.right) || self.right.overlaps(&self.left);
    }
    fn is_redundant(&self) -> bool {
        return self.left.contains(&self.right) || self.right.contains(&self.left);
    }
}

fn parse_content(content: &str) -> Vec<SchedulePair> {
    return content.lines()
                  .map(SchedulePair::from_str)
                  .collect();
}

fn main() {
    let content = include_str!("input.txt");

    let schedules = parse_content(content);
    let redundant_schedules = schedules.iter()
                                              .filter(|pair| pair.is_redundant())
                                              .count();

    println!("Redundant schedules: {}", redundant_schedules);

    let overlapping_schedules = schedules.iter()
                                                .filter(|pair| pair.is_overlapping())
                                                .count();

    println!("Overlapping schedules: {}", overlapping_schedules);
}
