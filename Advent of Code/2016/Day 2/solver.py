import os
from collections import defaultdict

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    keypad = {
        (0,0): "1", (0,1): "2", (0,2): "3",
        (1,0): "4", (1,1): "5", (1,2): "6",
        (2,0): "7", (2,1): "8", (2,2): "9"
    }
    
    current_position= (1,1)
    MIN_ROW = 0
    MIN_COL = 0
    MAX_ROW = 2
    MAX_COL = 2
    
    pin = []
    
    for full_command in inputs:
        for command in full_command:
            x,y = current_position
            if command == "\n":
                break
            if command == "D" and x<MAX_ROW:
                x+=1
            elif command == "U" and x>MIN_ROW:
                x-=1
            elif command == "R" and y<MAX_COL:
                y+=1
            elif command == "L" and y>MIN_COL:
                y-=1
            
            current_position = (x,y)
        pin.append(keypad[current_position])
        
    solution = "".join(pin)
    
    print("Solution Part 1:", solution)

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    keypad = {
        (0,0): "X", (0,1): "X", (0,2): "1", (0,3): "X", (0,4): "X",
        (1,0): "X", (1,1): "2", (1,2): "3", (1,3): "4", (1,4): "X",
        (2,0): "5", (2,1): "6", (2,2): "7", (2,3): "8", (2,4): "9",
        (3,0): "X", (3,1): "A", (3,2): "B", (3,3): "C", (3,4): "X",
        (4,0): "X", (4,1): "X", (4,2): "D", (4,3): "X", (4,4): "X"
    }
    
    current_position= (2,0)
    MIN_ROW = 0
    MIN_COL = 0
    MAX_ROW = 4
    MAX_COL = 4
    
    pin = []
    
    for full_command in inputs:
        for command in full_command:
            x,y = current_position
            if command == "\n":
                break
            if command == "D" and x<MAX_ROW and keypad[(x+1, y)] != "X":
                x+=1
            elif command == "U" and x>MIN_ROW and keypad[(x-1, y)] != "X":
                x-=1
            elif command == "R" and y<MAX_COL and keypad[(x, y+1)] != "X":
                y+=1
            elif command == "L" and y>MIN_COL and keypad[(x, y-1)] != "X":
                y-=1
            
            current_position = (x,y)
        pin.append(keypad[current_position])
        
    solution = "".join(pin)
    
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()