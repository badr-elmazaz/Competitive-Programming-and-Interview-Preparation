def main():
    n, k = map(int, input().split())

    ranges = []

    max_num = float("-inf")

    while n:
        start, end = map(int, input().split())
        ranges.append([start, end])
        max_num = max(max_num, end)
        n -= 1

    ans = 0
    while max_num > -1:
        counter = 0
        for interval in ranges:
            start, end = interval
            if start <= max_num <= end:
                counter += 1
        if counter == k:
            ans += 1


        max_num -= 1

    print(ans)


    


if __name__ == "__main__":
    main()