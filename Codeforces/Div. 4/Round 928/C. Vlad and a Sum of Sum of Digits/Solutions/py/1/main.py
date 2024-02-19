def main():
    t = int(input())

    while t:

        n = input()
        

        a, b = n[0:-1], n[-1]
        print("n", n, "a", a, "b", b)
        a = int(a)



        b = int(b)
        
        print(a, b)

        ans = 45 + 10 * (a - 1) + b + 1

        print(ans)
        


        t -= 1

if __name__ == "__main__":
    main()