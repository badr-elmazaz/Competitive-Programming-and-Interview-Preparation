class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)


        missing_nums = []
        n = len(nums) + 1

        # array as hashtable, try to store two values in one

        for i in range(len(nums)):
            current_real_num = nums[i] % n
            next_hash_position = nums[current_real_num - 1] 

            # to handle duplicates, 'hash collision'
            if next_hash_position > n:
                continue

            nums[current_real_num - 1] = next_hash_position + current_real_num * n

        # get values where each num should be stay and check if it is a zero, if yes it means that number is missing
        # (current number index + 1)
        for i in range(len(nums)):
            nums[i] //= n

            # check if it is zero
            if not nums[i]:
                missing_nums.append(i + 1)

        return missing_nums