#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k";

    #[test]
    fn test_solution() {
        let file_system = init_file_system(TEST_INPUT);
        let sizes = compute_file_system_sizes(&file_system);

        let smaller_sizes: u32 = sizes.iter()
                                      .filter(|&&size| size < 100000)
                                      .sum();

        assert_eq!(smaller_sizes, 94853 + 584);

        let used_size = sizes[0];
        let space_left = DISK_SIZE - used_size;
        let size_to_free = REQUIRED_SIZE - space_left;

        let &smaller_dir: &u32 = sizes.iter()
                                      .filter(|&&size| size >= size_to_free)
                                      .min()
                                      .unwrap();

        assert_eq!(smaller_dir, 24933642);
    }
}

const DISK_SIZE: u32 = 70000000;
const REQUIRED_SIZE: u32 = 30000000;

struct File {
    name: String,
    size: u32
}
struct Directory {
    name: String,
    parent: usize,
    children: Vec<usize>,
    files: Vec<File>
}

impl Directory {
    fn root() -> Directory {
        return Self {
            name: String::from("/"),
            parent: 0,
            children: vec![],
            files: vec![]
        };
    }
}

fn init_file_system(content: &str) -> Vec<Directory> {
    let mut cwd = 0;
    let mut file_system: Vec<Directory> = vec![];
    
    file_system.push(Directory::root());

    for execution in content.split("$ ") {
        let lines: Vec<&str> = execution.lines().collect();

        if lines.len() == 0 {
            continue;
        }
        else if lines.len() == 1 {
            let (command, params) = lines[0].split_once(' ').unwrap();

            match command {
                "cd" => {
                    match params {
                        "/" => cwd = 0,
                        ".." => cwd = file_system[cwd].parent,
                        _ => cwd = *file_system[cwd].children.iter()
                                                             .find(|&&child| file_system[child].name == params)
                                                             .unwrap()
                    }
                },
                _ => panic!("{}: command not found", command)
            }
        }
        else {
            let command = lines[0];

            match command {
                "ls" => {
                    let mut details = lines.iter();

                    details.next();
                    for detail in details {
                        let (size, name) = detail.split_once(' ').unwrap();
                        
                        match size {
                            "dir" => {
                                let index = file_system.len();

                                file_system.push(Directory {
                                    name: String::from(name),
                                    parent: cwd,
                                    children: vec![],
                                    files: vec![]
                                });

                                file_system[cwd].children.push(index);
                            },
                            _ => {
                                let size: u32 = size.parse().unwrap();

                                file_system[cwd].files.push(File {
                                    name: String::from(name),
                                    size: size
                                });
                            }
                        }
                    }
                },
                _ => panic!("{}: command not found", command)
            }
        }
    }

    return file_system;
}
fn compute_file_system_sizes(file_system: &Vec<Directory>) -> Vec<u32> {
    fn _compute_dir_size(_fs: &Vec<Directory>, _dir: usize) -> u32 {
        let mut size = 0;

        size += _fs[_dir].children.iter()
                                  .map(|&child| _compute_dir_size(_fs, child))
                                  .sum::<u32>();

        size += _fs[_dir].files.iter()
                               .map(|file| file.size)
                               .sum::<u32>();
        return size;
    }

    let mut sizes: Vec<u32> = vec![];

    for index in 0..file_system.len() {
        /*
         * FIXME: Do not compute multiple times the directory sizes!
         */

        sizes.push(_compute_dir_size(file_system, index));
    }

    return sizes;
}

fn main() {
    let content = include_str!("input.txt");
    let file_system = init_file_system(content);
    let sizes = compute_file_system_sizes(&file_system);

    let smaller_sizes: u32 = sizes.iter()
                                  .filter(|&&size| size < 100000)
                                  .sum();

    println!("Sum of all smaller directories: {}", smaller_sizes);

    let used_size = sizes[0];
    let space_left = DISK_SIZE - used_size;
    let size_to_free = REQUIRED_SIZE - space_left;

    let &smaller_dir: &u32 = sizes.iter()
                                  .filter(|&&size| size >= size_to_free)
                                  .min()
                                  .unwrap();

    println!("Smaller directory between the greatests: {}", smaller_dir);
}
