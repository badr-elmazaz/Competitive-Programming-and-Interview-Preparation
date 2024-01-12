class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time  -> O(n)
        # space -> O(n)

        left_product = [1]
        right_product = [1]

        for i in range(1, len(nums)):
            left_product.append(left_product[-1] * nums[i - 1])
            right_product.append(right_product[-1] * nums[len(nums)  - i])

        answer = []

        for i in range(len(left_product)):
            left_num = left_product[i]
            right_num = right_product[len(right_product) - 1 - i]
            answer.append(left_num * right_num)

        return answer


        