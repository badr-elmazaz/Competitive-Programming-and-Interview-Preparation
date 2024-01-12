def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()



def solve1():
    s = get_input()[0]
    ans=0
    for i in range(len(s)):
        sub=s[i]
        for j in range(1, 5):
            if (i+j>=len(s)):
                continue
            if( s[i+j] in sub ):
                break
            sub+=s[i+j]
        else:
            ans=i+4
            break
    print("Part 1:", ans)


def solve2():
    s = get_input()[0]
    ans=0
    for i in range(len(s)):
        sub=s[i]
        for j in range(1, 15):
            if (i+j>=len(s)):
                continue
            if( s[i+j] in sub ):
                break
            sub+=s[i+j]
        else:
            ans=i+14
            break
    print("Part 2:", ans)



if __name__ == "__main__":
    solve1()
    solve2()