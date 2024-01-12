def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()

def solve1():
    inputs = get_input()
    all_positions = set()

    head = tail = (0,0)
    all_positions.add(tail)

    for current_move in inputs:
        move = int(current_move.split()[-1])
        # if tail is not in the same head's row
        
        if "U" in current_move:
            print("U")
            for _ in range(move):
                head = (head[0]+1, head[1])
                if head == tail:
                    previous_head = head
                    continue
                if tail[1]==head[1]:
                    tail = (head[0]-1, head[1])
                    print("tail", tail)
                    all_positions.add(tail)
                elif abs(head[0]-tail[0])==2:
                    tail = previous_head
                    print("tail", tail)
                    all_positions.add(tail)
                previous_head = head

        elif "D" in current_move:
            print("D")
            for _ in range(move):
                head = (head[0]-1, head[1])
                if head == tail:
                    previous_head = head
                    continue
                if tail[1]==head[1]:
                    tail = (head[0]+1, head[1])
                    print("tail", tail)
                    all_positions.add(tail)
                elif abs(head[0]-tail[0])==2:
                    tail = previous_head
                    print("tail", tail)
                    all_positions.add(tail)
                previous_head = head

        elif "R" in current_move:
            print("R")
            for _ in range(move):
                head = (head[0], head[1]+1)
                if head == tail:
                    previous_head = head
                    continue
                if tail[0]==head[0]:
                    tail = (head[0], head[1]-1)
                    print("tail", tail)
                    all_positions.add(tail)
                elif abs(head[1]-tail[1])==2:
                    tail = previous_head
                    print("tail", tail)
                    all_positions.add(tail)
                previous_head = head

        else:
            print("L")
            for _ in range(move):
                head = (head[0], head[1]-1)
                if head == tail:
                    previous_head = head
                    continue
                if tail[0]==head[0]:
                    tail = (head[0], head[1]+1)
                    print("tail", tail)
                    all_positions.add(tail)
                elif abs(head[1]-tail[1])==2:
                    tail = previous_head
                    print("tail", tail)
                    all_positions.add(tail)
                previous_head = head
        
                
    print("Part 1:", len(all_positions))




if __name__ == "__main__":
    solve1()