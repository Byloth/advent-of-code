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

fn collect_row(forest: &[Vec<u32>], x: usize) -> Vec<u32> {
    return forest.iter()
                 .map(move |row| row[x])
                 .collect();
}
fn range_iter(start: usize, end: usize) -> impl Iterator<Item = usize> {
    let range: Box<dyn Iterator<Item = usize>> = if start < end {
        Box::new(start + 1..end)
    } else {
        Box::new((end..start).rev())
    };

    return range;
}

fn get_forest_size(forest: &[Vec<u32>]) -> (usize, usize) {
    return (forest[0].len(), forest.len());
}
fn is_edge_tree(x: usize, y: usize, width: usize, length: usize) -> bool {
    if x == 0 || x == (width - 1) {
        return true;
    }
    if y == 0 || y == (length - 1) {
        return true;
    }

    return false;
}

fn get_max_tree_height(trees: &[u32], start: usize, end: usize) -> u32 {
    let mut max_height = 0;

    for index in range_iter(start, end) {
        let height = trees[index];

        if height > max_height {
            max_height = height;
        }
    }

    return max_height;
}
fn get_view_distance(trees: &[u32], start: usize, end: usize) -> u32 {
    let tree_height = trees[start];

    let mut view_distance = 0;
    for index in range_iter(start, end) {
        view_distance += 1;

        if tree_height <= trees[index] {
            break;
        }
    }

    return view_distance;
}

fn is_tree_visible(forest: &[Vec<u32>], x: usize, y: usize, width: usize, length: usize) -> bool {
    if is_edge_tree(x, y, width, length) {
        return true;
    }

    let tree_height = forest[y][x];
    if tree_height > get_max_tree_height(&collect_row(forest, x), y, 0) {
        return true;
    }
    if tree_height > get_max_tree_height(&collect_row(forest, x), y, length) {
        return true;
    }
    if tree_height > get_max_tree_height(&forest[y], x, 0) {
        return true;
    }
    if tree_height > get_max_tree_height(&forest[y], x, width) {
        return true;
    }

    return false;
}
fn count_visible_trees(forest: &[Vec<u32>]) -> usize {
    let (width, length) = get_forest_size(forest);

    let mut count = 0;

    for y in 0..length {
        for x in 0..width {
            if is_tree_visible(forest, x, y, width, length) {
                count += 1;
            }
        }
    }

    return count;
}

fn compute_scenic_score(forest: &[Vec<u32>], x: usize, y: usize, width: usize, length: usize) -> u32 {
    if is_edge_tree(x, y, width, length) {
        return 0;
    }

    let width = forest[0].len();
    let length = forest.len();

    let top_view_distance = get_view_distance(&collect_row(forest, x), y, 0);
    let bottom_view_distance = get_view_distance(&collect_row(forest, x), y, length);
    let left_view_distance = get_view_distance(&forest[y], x, 0);
    let right_view_distance = get_view_distance(&forest[y], x, width);

    return top_view_distance * bottom_view_distance * left_view_distance * right_view_distance;
}
fn get_highest_scenic_score(forest: &[Vec<u32>]) -> u32 {
    let (width, length) = get_forest_size(forest);

    let mut highest_score = 0;

    for y in 0..length {
        for x in 0..width {
            let score = compute_scenic_score(forest, x, y, width, length);

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
