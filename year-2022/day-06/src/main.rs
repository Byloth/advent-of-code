#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT_1: &str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    const TEST_INPUT_2: &str = "bvwbjplbgvbhsrlpgdmjqwftvncz";
    const TEST_INPUT_3: &str = "nppdvjthqldpwncqszvftbrmjlhg";
    const TEST_INPUT_4: &str = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
    const TEST_INPUT_5: &str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    #[test]
    fn test_solution() {
        assert_eq!(find_start_marker(TEST_INPUT_1, 4), 7);
        assert_eq!(find_start_marker(TEST_INPUT_1, 14), 19);

        assert_eq!(find_start_marker(TEST_INPUT_2, 4), 5);
        assert_eq!(find_start_marker(TEST_INPUT_2, 14), 23);

        assert_eq!(find_start_marker(TEST_INPUT_3, 4), 6);
        assert_eq!(find_start_marker(TEST_INPUT_3, 14), 23);

        assert_eq!(find_start_marker(TEST_INPUT_4, 4), 10);
        assert_eq!(find_start_marker(TEST_INPUT_4, 14), 29);

        assert_eq!(find_start_marker(TEST_INPUT_5, 4), 11);
        assert_eq!(find_start_marker(TEST_INPUT_5, 14), 26);

    }
}

fn are_all_chars_different(chars: &[char], size: usize) -> bool {
    let mut index = 0;

    while index < (size - 1) {
        let mut jndex = index + 1;

        while jndex < size {
            if chars[index] == chars[jndex] {
                return false;
            }

            jndex += 1;
        }

        index += 1;
    }

    return true;
}

fn find_start_marker(content: &str, size: usize) -> usize {
    let mut counter = 0;
    let mut start_marker: Vec<char> = vec!['\0'; size];

    for character in content.chars() {
        start_marker.rotate_left(1);
        start_marker[size - 1] = character;

        counter += 1;

        if counter >= size && are_all_chars_different(&start_marker, size) {
            break;
        }
    }

    return counter;
}

fn main() {
    let content = include_str!("input.txt");

    let start_marker_4 = find_start_marker(content, 4);
    println!("Start marker with size 4: {}", start_marker_4);

    let start_marker_14 = find_start_marker(content, 14);
    println!("Start marker with size 14: {}", start_marker_14);
}
