from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i], carry = digits[i]-10, 1
            else:
                carry = 0
                break
        
        # this is bad because it creates a new list and copies all the elements so Time Complexity is O(n)
        # if carry == 1: 
            # digits.insert(0, 1) 
            
        if carry == 1: 
            digits[0] = 1
            digits.append(0)

        return digits