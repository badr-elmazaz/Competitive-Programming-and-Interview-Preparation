def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()




def solve1():
    inputs = get_input()

    total = 0

    signal_cicles = list(range(20, 221, 40))

    current_cycle = 0
    X = 1
    for input in inputs:
        if current_cycle in signal_cicles:
            total+=current_cycle*X
        if "add" in input:
            current_cycle+=1
            if current_cycle in signal_cicles:
                total+=current_cycle*X
            current_cycle+=1
            X+=int(input.split()[1].strip())
        else:
            current_cycle+=1

    print("Part 1:", total)








if __name__ == "__main__":
    solve1()