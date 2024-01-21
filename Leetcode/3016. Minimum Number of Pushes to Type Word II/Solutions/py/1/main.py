from collections import defaultdict, Counter, OrderedDict

class Solution:
    def minimumPushes(self, word: str) -> int:
        # n = len(word)
        # Time Complexity:  O(n * log(n))
        # Space Complexity: O(26) = O(1)

        char_freq = Counter(word)
        freq_char = defaultdict(set)
        
        
        for k, v in char_freq.items():
            freq_char[v].add(k)
            
        sorted_freq_char = OrderedDict(sorted(freq_char.items(), reverse = True))

        cost = 1
        counter = 0
        # map every char with its cost
        keymap = {}

        for freq, chars in sorted_freq_char.items():
            for char in chars:
                if counter % 8 == 0 and counter != 0:
                    cost += 1
                keymap[char] = cost
                counter += 1
        
        # calculate word cost
        ans = 0
        for char, freq in char_freq.items():
            char_cost = keymap[char]
            ans += char_cost * freq
            
            
        return ans