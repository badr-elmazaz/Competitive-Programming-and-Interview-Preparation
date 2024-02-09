def main():
    t = int(input())

    while t:
        n = int(input())
        s = input()
        f = input()

        to_add = 0
        to_remove = 0
        for s1, f1 in zip(s, f):
            if s1 == "0" and f1 == "1":
                to_add += 1
            elif s1 == "1" and f1 == "0":
                to_remove += 1

        ans = max(to_add, to_remove)
        print(ans)

        t -= 1


if __name__ == "__main__":
    main()
