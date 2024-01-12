class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # time  -> O(max(n, m)) , n=len(a), m=len(b)
        # space -> O(max(n, m)) , n=len(a), m=len(b)
        carry = 0
        
        sum_bin = ""
        
        max_bin, min_bin = (a, b) if len(a) > len(b) else (b, a)
        
        max_bin_index = len(max_bin)-1
        min_bin_index = len(min_bin)-1
        
        while max_bin_index >= 0:
            
            if min_bin_index < 0:
                current_min_bin_bit = 0
            else:
                current_min_bin_bit = min_bin[min_bin_index]
                
            current_max_bin_bit = max_bin[max_bin_index]
            
            decimal_sum = int(current_max_bin_bit) + int(current_min_bin_bit) + carry
            
            if decimal_sum == 0:
                sum_bin = "0"+sum_bin
                carry = 0
            
            elif decimal_sum == 1:
                sum_bin = "1"+sum_bin
                carry = 0
                
            elif decimal_sum == 2:
                sum_bin = "0"+sum_bin
                carry = 1
                
            else:
                sum_bin = "1"+sum_bin
                carry = 1
                
            max_bin_index -= 1
            min_bin_index -= 1
            
            
        if carry > 0:
            sum_bin = "1"+sum_bin
            
        return sum_bin