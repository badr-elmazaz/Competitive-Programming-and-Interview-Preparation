import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()

def is_abba(string: str) -> bool:
    for i in range(0, len(string)-1):
        this_char = string[i]
        next_char = string[i+1]
        if this_char == next_char:
            if i-1>=0 and i+2<len(string) and string[i-1] == string[i+2] and string[i-1] != this_char:
                return True
    return False

def extract_abas(string: str) -> list[str]:
    abas = []
    for i in range(0, len(string)):
        if i==len(string)-3:
            break
        this_char = string[i]
        next_char = string[i+1]
        next_next_char = string[i+2]
        if this_char == next_next_char and next_char != this_char:
            abas.append(string[i:i+3])
    return abas


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    for ipv7 in inputs:
        ipv7=ipv7.strip()
        first_split = ipv7.split("]")
        in_square = []
        out_square = []
        out_square.append(first_split[-1])
        first_split = first_split[:-1]
        for x in first_split:
            out, in_ = x.split("[")
            in_square.append(in_)
            out_square.append(out)
        valid = True
        for s in in_square:
            if is_abba(s):
                valid = False
                break
        if valid:
            valid = False
            for s in out_square:
                if is_abba(s):
                    valid = True
                    break
        if valid:
            solution+=1
            
    
    print("Solution Part 1:", solution)

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    for ipv7 in inputs:
        ipv7=ipv7.strip()
        first_split = ipv7.split("]")
        in_square = []
        out_square = []
        out_square.append(first_split[-1])
        first_split = first_split[:-1]
        for x in first_split:
            out, in_ = x.split("[")
            in_square.append(in_)
            out_square.append(out)
            
        valid = True
        for out in out_square:
            abas = extract_abas(out)
            if not abas:
                continue
            print(abas)
            for aba in abas:
                is_there = False
                for in_ in in_square:
                    if aba[1]+aba[0]+aba[1] in in_:
                        is_there = True
                        break
                if not is_there:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            solution+=1
                
        
        #print(out_square, in_square)
    
    print("Solution Part 2:", solution)


    

def main():
    #solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()