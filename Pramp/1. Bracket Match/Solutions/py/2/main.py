def bracket_match(text):
  # time O(n)
  # space O(1)
  opened = 0 
  closed = 0 
  
  for i, bracket in enumerate(text):
    if bracket == "(":
      opened += 1
    else:
      if opened > 0:
        opened -= 1
      else:
        closed += 1

  return opened+closed