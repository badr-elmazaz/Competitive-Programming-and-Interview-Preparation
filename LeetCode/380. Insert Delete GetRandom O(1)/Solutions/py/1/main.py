import random

class RandomizedSet:

    def __init__(self):
        self.val_idx = {}
        self.values = []
        

        

    def insert(self, val: int) -> bool:
        # time  -> O(1)
        # space -> O(n)

        if val not in self.val_idx:
            self.val_idx[val] = len(self.values)
            self.values.append(val)
            return True
        return False
            
        

    def remove(self, val: int) -> bool:
        # time  -> O(1)
        # space -> O(n)

        if val not in self.val_idx:
            return False
            
        idx_to_remove = self.val_idx.get(val)
        self.val_idx[self.values[-1]] = idx_to_remove
        self.values[idx_to_remove] = self.values[-1]
        
        self.val_idx.pop(val)
        self.values.pop()

        return True
        

        

    def getRandom(self) -> int:
        # time  -> O(1)
        # space -> O(n)
        
        return random.choice(self.values)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()