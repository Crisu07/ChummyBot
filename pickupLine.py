import random

def flirt():
  with open("pickupLines.txt") as file: # Read from pickupLines file and pick a random line
    lines = file.readlines()
    return random.choice(lines)