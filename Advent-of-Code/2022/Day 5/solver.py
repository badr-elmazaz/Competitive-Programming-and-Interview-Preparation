import itertools

def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()


def load_stacks(inputs: list[str])->list[str]:
    stacks = []

    for j in range(1, len(inputs[0]), 4):
        stacks.append([])
        for i in itertools.count(start=0):
            if( inputs[i][j].isdigit() ):
                break
            if( " "!=inputs[i][j]):
                stacks[-1].append(inputs[i][j])

    
    return [ s[::-1] for s in stacks]

def get_digits(string: str)->list:
    return string.split()

def solve1():
    inputs = get_input()
    stacks = load_stacks(inputs)
    for s in inputs:
        if "move" not in s:
            continue
        amount, _from, to = [int(x) for x in s.split() if x.isnumeric()]
        for _ in range(amount):
            stacks[to-1].append(stacks[_from-1].pop())
    ans = ""
    for s in stacks:
        ans+=s[-1]
    print("Part One:", ans)


def solve2():
    inputs = get_input()
    stacks = load_stacks(inputs)
    for s in inputs:
        if "move" not in s:
            continue
        amount, _from, to = [int(x) for x in s.split() if x.isnumeric()]
        for i in range(amount,0,-1):
            stacks[to-1].append(stacks[_from-1].pop(-i))
    ans = ""
    for s in stacks:
        ans+=s[-1]
    print("Part Two:", ans)
    


if __name__ == "__main__":
    solve1()
    solve2()