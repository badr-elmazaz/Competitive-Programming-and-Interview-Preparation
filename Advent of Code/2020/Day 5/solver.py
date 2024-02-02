
__author__ = "El Mazaz Badr"


import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()
  

    
def find_value(string: str, is_row: bool) -> int:
    if is_row:
        MAX = 128
        chr = "F"
    else:
        MAX = 8
        chr = "L"
    start = 0
    end = MAX - 1
    for s in string:
        mid = (end+start)//2
        if s==chr:
            end=mid
        else:
            start=mid+1
    mid = (end+start)//2
    return mid
        
def get_row(string_row: str) -> int:
    return find_value(string_row, True)

def get_column(string_col: str) -> int:
    return find_value(string_col, False)
    
def get_seat_id(string: str) -> int:
    string_row = string[:7]
    string_col = string[7:]
    row = get_row(string_row)    
    col = get_column(string_col)
    return (row * 8 + col)

def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    for s in inputs:
        solution = max(get_seat_id(s), solution)
    
    
    print("Solution Part 1:", solution)

        

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    # getting all the ids
    seat_ids = [get_seat_id(x) for x in inputs]
    # sorting all the ids
    seat_ids.sort()
    # all ids are like n, n+1, n+2 ... our id is the one that does't exists in this sequence
    for i in range(len(seat_ids)-1):
        if seat_ids[i+1]-seat_ids[i] != 1:
            solution = seat_ids[i]+1
            break
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()