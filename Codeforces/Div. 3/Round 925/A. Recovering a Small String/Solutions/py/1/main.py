def main():
    t = int(input())

    nums = []

    for i in range(1, 27):
        for _ in range(3):
            nums.append(i)

    ans = []

    while t:
        n = int(input())
        # 3sum
        for i in range(len(nums) - 2):
            x = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                y = nums[left]
                z = nums[right]
                total = x + y + z

                if total > n:
                    right -= 1
                elif total < n:
                    left += 1
                else:
                    a = chr(ord("a") + x - 1)
                    b = chr(ord("a") + y - 1)
                    c = chr(ord("a") + z - 1)
                    ans.append(a + b + c)
                    break
            else:
                continue
            break

        t -= 1

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
