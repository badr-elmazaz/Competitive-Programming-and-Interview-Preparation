
def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()


def get_range_length(r: list):
    return r[1]-r[0]

def is_fully_in_it(range1, range2):
    # is full range1 in range2?
    if( range1[0]>=range2[0] and range1[1]<=range2[1] ):
        return True
    return False


def solve1():
    inputs = get_input()
    ans = 0
    for i in inputs:
        first_range = [int(x) for x in i.split(",")[0].split("-")]
        second_range = [int(x) for x in i.split(",")[1].split("-")]
        first_range_length = get_range_length(first_range)
        second_range_length = get_range_length(second_range)
        if( first_range_length > second_range_length ):
            if is_fully_in_it(second_range, first_range):
                ans+=1
        else:
            if is_fully_in_it(first_range, second_range):
                ans+=1

    print(ans)

def is_in_it(range1, range2):
    # is full or partially range1 in range2?
    if( range1[0]>=range2[0] and range1[0]<=range2[1] or range1[1]>=range2[0] and range1[1]<=range2[1] ):
        return True
    return False


def solve2():
    inputs = get_input()
    ans = 0
    for i in inputs:
        first_range = [int(x) for x in i.split(",")[0].split("-")]
        second_range = [int(x) for x in i.split(",")[1].split("-")]
        first_range_length = get_range_length(first_range)
        second_range_length = get_range_length(second_range)
        if( first_range_length > second_range_length ):
            if is_in_it(second_range, first_range):
                ans+=1
        else:
            if is_in_it(first_range, second_range):
                ans+=1

    print(ans)
        


if __name__ == "__main__":
    solve1()
    solve2()