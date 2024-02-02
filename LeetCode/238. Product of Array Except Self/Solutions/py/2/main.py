class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time  -> O(n)
        # space -> O(1)

        answer = [1]
        for i in range(1, len(nums)):
            answer.append(answer[-1] * nums[i - 1])

        right_product = 1

        for i in range(len(answer)-2, -1, -1):
            answer[i] = answer[i] * nums[i + 1] * right_product
            right_product *= nums[i + 1]

        return answer


        