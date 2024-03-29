#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "A Y
B X
C Z";

    #[test]
    fn test_solution() {
        let strategy = parse_content(TEST_INPUT);
        let score_by_choices = compute_strategy_score(&strategy, compute_round_score_by_choices);

        assert_eq!(score_by_choices, 15);
    
        let score_by_result = compute_strategy_score(&strategy, compute_round_score_by_result);

        assert_eq!(score_by_result, 12);
    }
}

fn parse_content(content: &str) -> Vec<(char, char)> {
    fn _get_char(_choices: &[&str], _index: usize) -> char {
        return _choices[_index].chars().next().unwrap();
    }

    let mut strategy = vec![];

    for round in content.lines() {
        let choices: Vec<&str> = round.split(' ').collect();

        let other_choice = _get_char(&choices, 0);
        let my_choice = _get_char(&choices, 1);

        strategy.push((other_choice, my_choice));
    }

    return strategy;
}

fn compute_round_score_by_choices(round: &(char, char)) -> i32 {
    /*
     * A / X means Rock
     * B / Y means Paper
     * C / Z means Scissors
     */
    let other_choice = round.0;
    let my_choice = round.1;

    return match my_choice {
        'X' => 1 + match other_choice {
            'A' => 3,
            'B' => 0,
            'C' => 6,

            _ => panic!("The other choice is invalid!"),
        },
        'Y' => 2 + match other_choice {
            'A' => 6,
            'B' => 3,
            'C' => 0,

            _ => panic!("The other choice is invalid!"),
        },
        'Z' => 3 + match other_choice {
            'A' => 0,
            'B' => 6,
            'C' => 3,

            _ => panic!("The other choice is invalid!"),
        },

        _ => panic!("Your choice is invalid!"),
    };
}
fn compute_round_score_by_result(round: &(char, char)) -> i32 {
    /*
     * A means Rock
     * B means Paper
     * C means Scissors
     * 
     * X means you lose
     * Y means a draw
     * Z means you win
     */
    let other_choice = round.0;
    let my_choice = round.1;

    return match other_choice {
        'A' => match my_choice {
            'X' => 0 + 3,
            'Y' => 3 + 1,
            'Z' => 6 + 2,

            _ => panic!("Your choice is invalid!"),
        },
        'B' => match my_choice {
            'X' => 0 + 1,
            'Y' => 3 + 2,
            'Z' => 6 + 3,

            _ => panic!("Your choice is invalid!"),
        },
        'C' => match my_choice {
            'X' => 0 + 2,
            'Y' => 3 + 3,
            'Z' => 6 + 1,

            _ => panic!("Your choice is invalid!"),
        },

        _ => panic!("The other choice is invalid!"),
    };
}

fn compute_strategy_score(strategy: &[(char, char)], compute_fn: fn(&(char, char)) -> i32) -> i32 {
    let mut score = 0;

    for round in strategy {
        score += compute_fn(round);
    }

    return score;
}

fn main() {
    let content = include_str!("input.txt");

    let strategy = parse_content(content);
    let score_by_choices = compute_strategy_score(&strategy, compute_round_score_by_choices);

    println!("Score by choices: {}", score_by_choices);

    let score_by_result = compute_strategy_score(&strategy, compute_round_score_by_result);

    println!("Score by result: {}", score_by_result);
}
