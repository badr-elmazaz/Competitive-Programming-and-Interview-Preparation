def main():
    t = int(input())

    while t:
        n = int(input())
        last_one_row = -1
        ans = "TRIANGLE"
        for _ in range(n):
            count_one_row = 0
            for bit in input():
                if bit == "1":
                    count_one_row += 1
            if count_one_row == last_one_row and count_one_row > 0:
                ans = "SQUARE"
            last_one_row = count_one_row

        print(ans)


        t -= 1

if __name__ == "__main__":
    main()