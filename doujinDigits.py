import random

def sauce_gen():
  code = ''
  for i in range(6):
    code += str(random.randint(0,9))
  return code