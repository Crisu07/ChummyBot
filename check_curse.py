def curseCheck( curse, line):
  for i in line:
    if i in curse:
      return True
  return False