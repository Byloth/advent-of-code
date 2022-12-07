#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "A Y
B X
C Z";

    #[test]
    fn test_sum() {
        let strategy = parse_content(TEST_INPUT);
        let score = compute_strategy_score_1(&strategy);

        assert_eq!(score, 15);
    
        let score = compute_strategy_score_2(&strategy);

        assert_eq!(score, 12);
    }
}

fn parse_content(content: &str) -> Vec<(char, char)> {
    let mut strategy = vec![];

    for round in content.split('\n') {
        let choices: Vec<&str> = round.split(' ').collect();

        let other_choice = choices[0].chars().next().unwrap();
        let my_choice = choices[1].chars().next().unwrap();

        strategy.push((other_choice, my_choice));
    }

    return strategy;
}

fn compute_round_score_1(round: &(char, char)) -> i32 {
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
fn compute_strategy_score_1(strategy: &Vec<(char, char)>) -> i32 {
    let mut score = 0;

    for round in strategy {
        score += compute_round_score_1(&round);
    }

    return score;
}

fn compute_round_score_2(round: &(char, char)) -> i32 {
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
fn compute_strategy_score_2(strategy: &Vec<(char, char)>) -> i32 {
    let mut score = 0;

    for round in strategy {
        score += compute_round_score_2(&round);
    }

    return score;
}

fn main() {
    let content = include_str!("input.txt");

    let strategy = parse_content(content);
    let score = compute_strategy_score_1(&strategy);

    println!("Score #1: {}", score);

    let score = compute_strategy_score_2(&strategy);

    println!("Score #2: {}", score);
}
