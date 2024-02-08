
def main():
    t = int(input())

    while t:
        n = int(input())
        s = input()
        f = input()

        to_place = 0
        to_remove = 0
        for s1, f1 in zip(s, f):
            if s1 == "0" and f1 == "1":
                to_place += 1
            elif s1 == "1" and f1 == "0":
                to_remove += 1

        maximum, minimum = max(to_place, to_remove), min(to_place, to_remove)
        if maximum == minimum and maximum != 0:
            ans = maximum
        else:
            ans = maximum // (minimum if minimum else 1)
        print(ans)        
        t -= 1





if __name__ == "__main__":
    main()