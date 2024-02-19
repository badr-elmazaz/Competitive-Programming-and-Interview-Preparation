class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        # n = len(s)
        # Time Complexity:  O(n)
        # Space Compelxity: O(26) = O(1)
        
        hashmap = defaultdict(list)
        maximum = 1
        for char in s:
            if not hashmap[char]:
                hashmap[char] = [1, 0]
            else:
                hashmap[char][0] += 1
                maximum = max(maximum, hashmap[char][0])
        
        new_s = []
        for char in s:
            if hashmap[char][0] != maximum:
                continue
            hashmap[char][1] += 1
            if hashmap[char][1] == maximum:
                new_s.append(char)
                
        return "".join(new_s)
            
                
        
        
        