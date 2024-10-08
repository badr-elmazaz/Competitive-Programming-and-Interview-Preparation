class Solution:
    def interpret(self, command: str) -> str:
        # n = len(command)
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        ans = []

        i = 0
        while i < len(command):
            curr_char = command[i]
            if curr_char == "G":
                ans.append("G")
                i += 1
            elif curr_char == "(" and command[i + 1] == ")":
                ans.append("o")
                i += 2
            else:
                ans.append("al")
                i += 4

        return "".join(ans)
