def main():
    total_problems = 0
    n = int(input())

    while n:
        problem = input()
        counter = 0
        for s in problem:
            if s == "1":
                counter += 1
        if counter >= 2:
            total_problems += 1

        n -= 1

    print(total_problems)




if __name__ == "__main__":
    main()