class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time  -> O(n)
        # space -> O(1)
        # Floyd’s Cycle Finding Algorithm

        slow = nums[0]
        fast = nums[0]   

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break

        slow = nums[0]

        while True:
            if (slow == fast):
                return fast

            slow = nums[slow]
            fast = nums[fast]