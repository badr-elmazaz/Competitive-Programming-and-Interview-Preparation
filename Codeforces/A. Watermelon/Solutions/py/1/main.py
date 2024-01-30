
def main():
    w = int(input())

    ans = "YES" if (w & 1 == 0 and w != 2) else "NO"

    print(ans)




if __name__ == "__main__":
    main()