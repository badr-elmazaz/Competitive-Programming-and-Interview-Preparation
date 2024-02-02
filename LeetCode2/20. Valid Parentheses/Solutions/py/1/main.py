class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        for i in range(1, len(s)):
            if len(stack)>0 and (s[i] == ")" and stack[-1] == "(" or \
                    s[i] == "}" and stack[-1] == "{" or \
                    s[i] == "]" and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) < 1
        