def twoNumberSum(array, targetSum):
    hashmap = {num:i for i, num in enumerate(array)}
    for i, num in enumerate(array):
        sub = targetSum-num
        if hashmap.get(sub) is not None and hashmap.get(sub) != i:
            return [num, sub]
    return []
