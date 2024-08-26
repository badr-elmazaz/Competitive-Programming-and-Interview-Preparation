class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

        num_words = 0
        ans = []

        for char in s:
            if char == " ":
                num_words += 1
                if num_words == k:
                    break
            ans.append(char)

        return "".join(ans)

