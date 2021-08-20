import random
import discord

def roll_dice():
  diceNumbers = ['1', '2', '3', '4', '5', '6']
  return discord.Embed(random.choice(diceNumbers))