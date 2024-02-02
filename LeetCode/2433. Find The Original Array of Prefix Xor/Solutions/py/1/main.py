class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # n = len(pref)
        # Time Complexity:  O(n)
        # Space Complexity: O(n)

       xor = [pref[0]]

       running_xor = pref[0]

       for i in range(1, len(pref)):
           val = pref[i] ^ running_xor
           xor.append(val)
           running_xor ^= xor[-1]
           

       return xor