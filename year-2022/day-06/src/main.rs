mod tests {
    use super::*;

    const TEST_INPUT_1: &str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    const TEST_INPUT_2: &str = "bvwbjplbgvbhsrlpgdmjqwftvncz";
    const TEST_INPUT_3: &str = "nppdvjthqldpwncqszvftbrmjlhg";
    const TEST_INPUT_4: &str = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
    const TEST_INPUT_5: &str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    #[test]
    fn test_solution() {
        let start_marker_1 = find_start_marker(TEST_INPUT_1);
        assert_eq!(start_marker_1, 7);

        let start_marker_2 = find_start_marker(TEST_INPUT_2);
        assert_eq!(start_marker_2, 5);

        let start_marker_3 = find_start_marker(TEST_INPUT_3);
        assert_eq!(start_marker_3, 6);

        let start_marker_4 = find_start_marker(TEST_INPUT_4);
        assert_eq!(start_marker_4, 10);

        let start_marker_5 = find_start_marker(TEST_INPUT_5);
        assert_eq!(start_marker_5, 11);

    }
}

const START_MARKER_SIZE: usize = 4;

fn are_all_chars_different(chars: &[char]) -> bool {
    let mut index = 0;

    while index < (START_MARKER_SIZE - 1) {
        let mut jndex = index + 1;

        while jndex < START_MARKER_SIZE {
            if chars[index] == chars[jndex] {
                return false;
            }

            jndex += 1;
        }

        index += 1;
    }

    return true;
}

fn find_start_marker(content: &str) -> usize {
    let mut counter = 0;
    let mut start_marker: Vec<char> = vec!['\0'; START_MARKER_SIZE];

    for character in content.chars() {
        start_marker.rotate_left(1);
        start_marker[START_MARKER_SIZE - 1] = character;

        counter += 1;

        if counter >= START_MARKER_SIZE && are_all_chars_different(&start_marker) {
            break;
        }
    }

    return counter;
}

fn main() {
    let content = include_str!("input.txt");

    let start_marker = find_start_marker(content);
    println!("Start marker: {}", start_marker);
}
