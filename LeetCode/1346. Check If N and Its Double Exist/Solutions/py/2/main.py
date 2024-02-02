class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # n = len(arr)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        hashset = set()

        for num in arr:
            if num * 2 in hashset or (num & 1 == 0 and num // 2 in hashset):
                return True
            hashset.add(num)
        return False