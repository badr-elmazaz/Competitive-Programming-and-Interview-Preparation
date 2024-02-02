import math

def main():
    # n = num of services
    # t = total second of a round

    n, t = map(int, input().split())

    checks = map(int, input().split())
    
    total = sum(checks)

    workers = math.ceil(total / t)

    print(workers)



if __name__ == "__main__":
    main()