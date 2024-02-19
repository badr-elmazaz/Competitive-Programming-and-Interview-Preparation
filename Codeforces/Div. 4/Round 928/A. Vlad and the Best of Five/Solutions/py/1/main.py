def main():
    t = int(input())

    while t:
        s = input()
        count_a = 0
        for char in s:
            if char == "A":
                count_a += 1
        ans = "A" if count_a > len(s) // 2 else "B"
        print(ans)

        t -= 1

if __name__ == "__main__":
    main()