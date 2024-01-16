class Solution:
    def reverseWords(self, s: str) -> str:
        # n = len(s)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        word_stack = []
        word = []

        for char in s:
            if char == " ":
                if word:
                    word_str = "".join(word) # O(n)?
                    word_stack.append(word_str)
                    word = []
                continue
            word.append(char)

        if word:
            last_word_str = "".join(word)
            word_stack.append(last_word_str)

        return " ".join(reversed(word_stack))
        
            
        