class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in range(1, len(s)):
            current_bracket = s[i]
            if not pairs.get(current_bracket):
                stack.append(s[i])
            elif len(stack) > 0 and pairs.get(current_bracket) == stack[-1]:
                stack.pop()
            else:
                return False
                
        return len(stack) < 1
        