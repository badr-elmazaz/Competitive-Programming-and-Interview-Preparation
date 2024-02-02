class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.lower().isalnum():
                string += char.lower()
        
        for i in range(len(string)//2):
            if string[i] != string[len(string)-1-i]:
                return False

        return True