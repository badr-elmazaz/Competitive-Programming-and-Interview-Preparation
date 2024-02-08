
def main():
    t = int(input())

    while t:
        n = int(input())
        s = input()
        
        
        second_black_idx = -1
        first_black_idx = -1

        for i, color in enumerate(s):
            if color == "B":
                first_black_idx = i
                break
        
        for i, color in enumerate(reversed(s)):
            if color == "B":
                second_black_idx = len(s) - 1 - i
                break

        length = 0 if first_black_idx == -1 else (second_black_idx - first_black_idx + 1)

        print(length)

        

        
        t -= 1





if __name__ == "__main__":
    main()