def find_pairs_with_given_difference(arr, k):
  # n = len(arr)
  # Time Complexity:  O(n)
  # Space Complexity: O(n) 
  
  hash_set = set(arr)  
  
  output = [] 
  
  for num in arr:
    missing_value = k + num 
    
    if missing_value in hash_set:
      output.append([missing_value, num])
      
  return output