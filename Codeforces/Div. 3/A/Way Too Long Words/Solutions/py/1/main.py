def main():
    strings = []
    n = int(input())

    while n:
        strings.append(input())
        n -= 1

    for s in strings:
        if len(s) > 10:
            print(f"{s[0]}{len(s) - 2}{s[-1]}")
        else:
            print(s)




if __name__ == "__main__":
    main()