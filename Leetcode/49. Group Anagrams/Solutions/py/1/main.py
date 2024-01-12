from collections import defaultdict
from typing import List

class Solution:
  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
      hashmap = defaultdict(list) 
      
      for s in strs:
        sorted_s = ''.join(sorted(s))
        hashmap[sorted_s].append(s)
      
      output = []
      
      for _, v in hashmap.items():
        output.append(v)

      return output
      
			
      
