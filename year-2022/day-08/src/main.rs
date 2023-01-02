#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "30373
25512
65332
33549
35390";

    #[test]
    fn test_solution() {
        let forest = parse_content(TEST_INPUT);
        let visible_trees = count_visible_trees(&forest);

        assert_eq!(visible_trees, 21);
    }
}

fn parse_content(content: &str) -> Vec<Vec<u32>> {
    return content.lines()
                  .map(|line| {
                      line.chars()
                          .map(|c| c.to_digit(10).unwrap())
                          .collect::<Vec<u32>>()
                  })
                  .collect::<Vec<Vec<u32>>>();
}

fn max_tree_height_on_x(forest: &[Vec<u32>], x: usize, start: usize, end: usize) -> u32 {
    let mut max_height = 0;

    for y in start..end {
        if forest[y][x] > max_height {
            max_height = forest[y][x];
        }
    }

    return max_height;
}
fn max_tree_height_on_y(forest: &[Vec<u32>], y: usize, start: usize, end: usize) -> u32 {
    let mut max_height = 0;

    for x in start..end {
        if forest[y][x] > max_height {
            max_height = forest[y][x];
        }
    }

    return max_height;
}

fn is_tree_visible(forest: &[Vec<u32>], x: usize, y: usize) -> bool {
    let width = forest[0].len();
    let length = forest.len();

    if x == 0 || x == (width - 1) {
        return true;
    }
    if y == 0 || y == (length - 1) {
        return true;
    }

    let tree_height = forest[y][x];

    if tree_height > max_tree_height_on_x(forest, x, 0, y) {
        return true;
    }
    if tree_height > max_tree_height_on_x(forest, x, y + 1, length) {
        return true;
    }
    if tree_height > max_tree_height_on_y(forest, y, 0, x) {
        return true;
    }
    if tree_height > max_tree_height_on_y(forest, y, x + 1, width) {
        return true;
    }

    return false;
}
fn count_visible_trees(forest: &[Vec<u32>]) -> usize {
    let width = forest[0].len();
    let length = forest.len();

    let mut count = 0;

    for y in 0..length {
        for x in 0..width {
            if is_tree_visible(forest, x, y) {
                count += 1;
            }
        }
    }

    return count;
}

fn main() {
    let content = include_str!("input.txt");
    let forest = parse_content(content);
    let visible_trees = count_visible_trees(&forest);

    println!("Visible trees: {}", visible_trees);
}
