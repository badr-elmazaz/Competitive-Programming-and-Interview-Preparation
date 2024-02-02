import os
import re

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()
    
def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs_formatted = "".join(inputs).split("\n\n")
    inputs_formatted = [s.replace("\n", " ").split(" ") for s in inputs_formatted]
    inputs_formatted = [{x.split(":")[0]:x.split(":")[1] for x in s if "cid:" not in x} for s in inputs_formatted]
    solution = sum([1 for s in inputs_formatted if len(s.keys())==7])
    
    print("Solution Part 1:", solution)

def is_valid(s: str) -> bool:
    k, v = s.split(":")
    k = k.strip()
    v = v.strip()
    if k == "byr":
        return 1920 <= int(v) <= 2002
    elif k == "iyr":
        return 2010 <= int(v) <= 2020
    elif k == "eyr":
        return 2020 <= int(v) <= 2030
    elif k == "hgt":
        if v.endswith("cm"):
            v = int(v.replace("cm", ""))
            return 150 <= int(v) <= 193
        elif v.endswith("in"):
            v = int(v.replace("in", ""))
            return 59 <= int(v) <= 76
    elif k == "hcl":
        pattern = r"^#[0-9a-f]{6,6}$"
        return re.match(pattern, v)
    elif k == "ecl":
        return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif k == "pid":
        pattern = r"^[0-9]{9,9}$"
        return re.match(pattern, v)
    elif k == "cid":
        return False
    return False
        

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    inputs_formatted = "".join(inputs).split("\n\n")
    inputs_formatted = [s.replace("\n", " ").split(" ") for s in inputs_formatted]
    inputs_formatted = [{x.split(":")[0]:x.split(":")[1] for x in s if is_valid(x)} for s in inputs_formatted]
    solution = sum([1 for s in inputs_formatted if len(s.keys())==7])
        
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()