def bracket_match(text):
  # time O(n)
  # space O(n)
  stack = [text[0]] 
  
  for i in range(1, len(text)):
    bracket = text[i]
    if stack and bracket == ")" and stack[-1] == "(":
      stack.pop()
    else:
      stack.append(bracket)
    
    
  return len(stack)