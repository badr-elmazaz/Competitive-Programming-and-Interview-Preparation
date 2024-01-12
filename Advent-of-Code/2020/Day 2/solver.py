import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return [x[:-1] for x in f.readlines()]


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0     
    for s in inputs:
        s_splitted = s.split(" ")
        char = s_splitted[1][:-1]
        range_left = int(s_splitted[0].split("-")[0])
        range_right = int(s_splitted[0].split("-")[1])
        if range_left <= s_splitted[2].count(char) <= range_right:
            solution+=1
    print("Solution Part 1:", solution)

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0     
    for s in inputs:
        s_splitted = s.split(" ")
        char = s_splitted[1][:-1]
        range_left = int(s_splitted[0].split("-")[0])
        range_right = int(s_splitted[0].split("-")[1])
        # using XOR logic
        if range_right-1 <= len(s_splitted[2])-1 and (s_splitted[2][range_left-1] == char) ^ (s_splitted[2][range_right-1] == char):
            solution+=1
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()