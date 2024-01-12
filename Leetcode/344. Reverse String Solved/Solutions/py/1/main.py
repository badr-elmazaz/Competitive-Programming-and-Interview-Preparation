class Solution:
    def reverseString(self, s: List[str]) -> None:
        # n = len(s)
        # Time Complexity  -> O(n)
        # Space Complexity -> O(1)

        for i in range(len(s)//2):
            s[i], s[len(s) - 1 - i] = s[len(s) -1 -i], s[i]
        