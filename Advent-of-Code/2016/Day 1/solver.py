import os
from collections import defaultdict

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs = inputs[0].split(", ")
    
    current_compass = "N"
    current_position = (0,0)
    
    
    for command in inputs:
        x,y = current_position
        movement = int(command[1:])
        
        if "R" in command and current_compass == "N" or "L" in command and current_compass == "S":
            current_compass = "E"
            x+=movement
        elif "R" in command and current_compass == "S" or "L" in command and current_compass == "N":
            current_compass = "W"
            x-=movement
        elif "R" in command and current_compass == "W" or "L" in command and current_compass == "E":
            current_compass = "N"
            y+=movement
        elif "R" in command and current_compass == "E" or "L" in command and current_compass == "W":
            current_compass = "S"
            y-=movement
                
        current_position = (x,y)
    
    x,y = current_position
    solution = abs(x)+abs(y)   
    
    print("Solution Part 1:", solution)

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs = inputs[0].split(", ")
    
    current_compass = "N"
    current_position = (0,0)
    
    positions = defaultdict(lambda: 0)
    
    
    for command in inputs:
        x,y = current_position
        previous_x = x
        previous_y = y
        movement = int(command[1:])
        
        exit = False
        
        if "R" in command and current_compass == "N" or "L" in command and current_compass == "S":
            current_compass = "E"
            x+=movement
        elif "R" in command and current_compass == "S" or "L" in command and current_compass == "N":
            current_compass = "W"
            x-=movement
        elif "R" in command and current_compass == "W" or "L" in command and current_compass == "E":
            current_compass = "N"
            y+=movement
        elif "R" in command and current_compass == "E" or "L" in command and current_compass == "W":
            current_compass = "S"
            y-=movement
            
        if previous_x == x:
            if previous_y > y:
                for i in range(previous_y-1, y-1, -1):
                    positions[(x, i)] +=1
                    if positions[(x, i)] == 2:
                        current_position = (x,i)
                        exit = True
                        break
            else:
                for i in range(previous_y+1, y+1):
                    positions[(x, i)] +=1
                    if positions[(x, i)] == 2:
                        current_position = (x,i)
                        exit = True
                        break
        else:
            if previous_x > x:
                for i in range(previous_x-1, x-1, -1):
                    positions[(i, y)] +=1
                    if positions[(i, y)] ==2:
                        current_position = (i, y)
                        exit = True
                        break
            else:
                for i in range(previous_x+1, x+1):
                    positions[(i, y)] +=1
                    if positions[(i, y)] == 2:
                        current_position = (i, y)
                        exit = True
                        break
        if exit:
            break
                
        current_position = (x,y)
    
    x,y = current_position
    solution = abs(x)+abs(y)   
    
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()