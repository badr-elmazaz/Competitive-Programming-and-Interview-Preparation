
__author__ = "El Mazaz Badr"


import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    questions = set()
    
    for s in inputs:
        s=s.replace("\n", "")
        if s=="":
            solution += len(questions)
            questions = set()
        else:
            questions.update({x for x in s})
    solution += len(questions)
        
    
    print("Solution Part 1:", solution)

        

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    # starting with first string to create a set, to avoid to start with an empty set, that will always return empty set with interesction
    # the idea is to intersect the strings 
    questions = {x for x in inputs[0].replace("\n", "")}
        
    for i in range(1, len(inputs)):
        s = inputs[i]
        s=s.replace("\n", "")
        # if previous string was a new line then restart with a new set 
        if inputs[i-1]=="\n":
            questions = {x for x in s.replace("\n", "")}
        # if current string is the new line char then the group of people is finished, update the solution
        if s=="":
            solution += len(questions)
        # otherwise intersect the current set with the next one
        else:
            questions = questions.intersection({x for x in s})
    solution += len(questions)
        
    
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()