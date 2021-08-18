#checks for exact matches of swear/bad words from someone's sentence and our dictionary 
def check_curse( curse, line):
  for i in line:
    if i in curse:
      return True
  return False