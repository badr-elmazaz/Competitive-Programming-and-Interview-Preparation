
def main():
    string = input()

    count_ones = 0
    count_zeros = 0

    for s in string:
        if s == "1":
            count_ones  += 1
            count_zeros = 0
        else:
            count_zeros += 1
            count_ones = 0
        if count_zeros > 6 or count_ones > 6:
            break

    ans = "YES" if (count_zeros > 6 or count_ones > 6) else "NO"
    print(ans)




if __name__ == "__main__":
    main()