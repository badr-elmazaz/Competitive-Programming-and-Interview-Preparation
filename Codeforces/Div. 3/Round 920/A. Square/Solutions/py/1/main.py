
def main():
    t = int(input())

    while t:
        x1, _ = map(int, input().split())
        x2, _ = map(int, input().split())
        x3, _ = map(int, input().split())
        x4, _ = map(int, input().split())

        x1, x2, *_ = {x1, x2, x3, x4}

        area = (x1 - x2) ** 2

        print(area)
    
        
        t -= 1




if __name__ == "__main__":
    main()