from dataclasses import dataclass
from typing import Optional
import sys

def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()

@dataclass
class Dir:
    children: Optional[list["Dir"]]
    
    name: str
    size: int
    parent: Optional["Dir"] = None


def get_size_and_dirs(chunk: list[str]):
    dirs = []
    size = 0
    i = 0
    for c in chunk:
        i+=1
        if c.startswith("$ cd"):
            break
        if c.startswith("dir"):
            dirs.append(c.split()[1])
        elif not c.startswith("$ ls"):
            try:
                size+=int(c.split()[0])
            except:
                print(c)
                sys.exit(1)
                
        
    return dirs, size, i

def find_dirs_best_size(LIMIT: int, dirs: list):
    #order dirs by size:
    sorted_dirs = sorted(dirs, key=lambda d: d.size)
    best = 0 
    for i in range(len(sorted_dirs)):
        sum=sorted_dirs[i].size
        for j in range(i, len(sorted_dirs)):
            if sum+sorted_dirs[j].size>LIMIT:
                break
            sum+=sorted_dirs[j].size
        if LIMIT-sum < LIMIT-best:
            print("sum", sum, "best", best)
            best = sum

    return best


def solve1():
    LIMIT = 100_000
    inputs = get_input()
    dirs = []
    for i in range(len(inputs)):
        if i>=len(inputs):
            break
        if inputs[i].startswith("$ cd"):
            if ".." in inputs[i]:
                # go back
                pass
            else:
                children_dirs, size, index_refresh = get_size_and_dirs(inputs[i+1:])
                if size <= LIMIT:
                    current_dir = Dir(name = inputs[i].split()[-1], size=size, children=children_dirs)
                    dirs.append(current_dir)
                i+=index_refresh
    best_size = find_dirs_best_size(LIMIT, dirs)
    print("Quiz 1: ", best_size)
    


if __name__ == "__main__":
    solve1()
