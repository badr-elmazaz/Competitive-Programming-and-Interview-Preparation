class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # time  -> O(n)
        # space -> O(1)
        
        left_count = 0
        right_count = 0
        vowels = "aeiou"

        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                left_count += 1

            if s[len(s)-1-i].lower() in vowels:
                right_count += 1

        return left_count == right_count
