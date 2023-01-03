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

        let highest_scenic_score = get_highest_scenic_score(&forest);
        assert_eq!(highest_scenic_score, 8);
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

fn get_max_x_tree_height(forest: &[Vec<u32>], x: usize, start: usize, end: usize) -> u32 {
    let mut max_height = 0;

    for y in start..end {
        if forest[y][x] > max_height {
            max_height = forest[y][x];
        }
    }

    return max_height;
}
fn get_max_y_tree_height(forest: &[Vec<u32>], y: usize, start: usize, end: usize) -> u32 {
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

    if tree_height > get_max_x_tree_height(forest, x, 0, y) {
        return true;
    }
    if tree_height > get_max_x_tree_height(forest, x, y + 1, length) {
        return true;
    }
    if tree_height > get_max_y_tree_height(forest, y, 0, x) {
        return true;
    }
    if tree_height > get_max_y_tree_height(forest, y, x + 1, width) {
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

fn get_x_view_distance(forest: &[Vec<u32>], y: usize, start: usize, end: usize) -> u32 {
    let tree_height = forest[y][start];

    let range;
    if start < end {
        range = ((start + 1)..end).collect::<Vec<usize>>();
    }
    else {
        range = (end..start).rev().collect::<Vec<usize>>();
    }

    let mut view_distance = 0;
    for x in range {
        view_distance += 1;

        if tree_height <= forest[y][x] {
            break;
        }
    }

    return view_distance;
}
fn get_y_view_distance(forest: &[Vec<u32>], x: usize, start: usize, end: usize) -> u32 {
    let tree_height = forest[start][x];

    let range;
    if start < end {
        range = ((start + 1)..end).collect::<Vec<usize>>();
    }
    else {
        range = (end..start).rev().collect::<Vec<usize>>();
    }

    let mut view_distance = 0;
    for y in range {
        view_distance += 1;

        if tree_height <= forest[y][x] {
            break;
        }
    }

    return view_distance;
}

fn compute_scenic_score(forest: &[Vec<u32>], x: usize, y: usize) -> u32 {
    let width = forest[0].len();
    let length = forest.len();

    if x == 0 || x == (width - 1) {
        return 0;
    }
    if y == 0 || y == (length - 1) {
        return 0;
    }

    let top_view_distance = get_x_view_distance(forest, y, x, 0);
    let bottom_view_distance = get_x_view_distance(forest, y, x, width);
    let left_view_distance = get_y_view_distance(forest, x, y, 0);
    let right_view_distance = get_y_view_distance(forest, x, y, length);

    return top_view_distance * bottom_view_distance * left_view_distance * right_view_distance;
}
fn get_highest_scenic_score(forest: &[Vec<u32>]) -> u32 {
    let width = forest[0].len();
    let length = forest.len();

    let mut highest_score = 0;

    for y in 0..length {
        for x in 0..width {
            let score = compute_scenic_score(forest, x, y);

            if score > highest_score {
                highest_score = score;
            }
        }
    }

    return highest_score;
}

fn main() {
    let content = include_str!("input.txt");
    let forest = parse_content(content);

    let visible_trees = count_visible_trees(&forest);
    println!("Visible trees: {}", visible_trees);

    let highest_scenic_score = get_highest_scenic_score(&forest);
    println!("Highest scenic score: {}", highest_scenic_score);
}
