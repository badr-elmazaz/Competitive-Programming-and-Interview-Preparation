import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return [x[:-1] for x in f.readlines()]

def solve(right: int, down: int) -> int:
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    ROW_LEN = len(inputs[0])
    current_position = 0
    for i in range(0, len(inputs), down):
        if inputs[i][current_position%(ROW_LEN)] == "#":
            solution+=1
        current_position += right
        
    return solution

def solve_part_one():
    solution = solve(3, 1)
    print("Solution Part 1:", solution)

def solve_part_two():
    solution = solve(1,1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2)
        
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()