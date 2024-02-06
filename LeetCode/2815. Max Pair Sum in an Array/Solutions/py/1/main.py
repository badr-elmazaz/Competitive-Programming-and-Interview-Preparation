class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        hashtable = defaultdict(list)

        for num in nums:
            max_digit = max(map(int, list(str(num))))
            if len(hashtable[max_digit]) == 0:
                hashtable[max_digit].append(num)
            elif len(hashtable[max_digit]) == 1:
                if num > hashtable[max_digit][0]:
                    hashtable[max_digit].append(num)
                else:
                    hashtable[max_digit].insert(0, num)
            elif num > hashtable[max_digit][0]:
                min_num, max_num = hashtable[max_digit]
                if num > max_num:
                    hashtable[max_digit][0], hashtable[max_digit][1] = (
                        hashtable[max_digit][1],
                        num,
                    )
                else:
                    hashtable[max_digit][0] = num

        maximum = -1
        for two_biggest_nums in hashtable.values():
            if len(two_biggest_nums) > 1:
                total = sum(two_biggest_nums)
                maximum = max(maximum, total)

        return maximum
