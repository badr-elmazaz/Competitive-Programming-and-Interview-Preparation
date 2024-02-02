import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return [int(x[:-1]) for x in f.readlines()]


def solve_part_one():
    TARGET = 2020
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs_set = set(inputs) 
    solution: int     
    for n in inputs_set:
        if TARGET-n in inputs_set:
            solution = n*(TARGET-n)
            break
    print("Solution Part 1:", solution)

def solve_part_two():
    TARGET = 2020
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs_set = set(inputs) 
    solution: int     
    for n in inputs_set:
        new_target = TARGET-n
        for m in inputs_set:
            if new_target-m in inputs_set:
                solution = n * (new_target-m) * m
                break
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()