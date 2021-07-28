import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive # Imports line 13 from keep_alive file

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True

# Inspirational Quote Feature
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# Doujin Generator Feature
def sauce_gen():
  code = '' # String for code because need to plug into website and check if exists
  for i in range(6):
    code += str(random.randint(0,9))
  return code

# Dice Roll
def roll_dice():
  diceNumbers = [1, 2, 3, 4, 5, 6]
  return random.choice(diceNumbers)



@client.event
async def on_ready(): # Let's us know that the bot is online
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  # Inspirational Quote
  if msg.startswith('$inspire'):
    quote = get_quote() # Retrieves a random inspirational quote 
    await message.channel.send(quote) # Send it to channel that command was given

  # Picks Favorite Gen 1 Starter Pokemon
  if msg.startswith("$favorite"):
    starters = ["Bulbasaur", "Squirtle", "Charmander"]
    favorite = random.choice(starters)
    await message.channel.send("I kinda like {}...".format(favorite))

  # Greets the User
  if msg.startswith('$hey'):
    await message.channel.send("Hey, {}! You come here often?".format(message.author.mention))

  # Sauce Finder
  if msg.startswith('$sauce'):
    sauce = sauce_gen()
    await message.channel.send("What up boss! Here's yo sauce: " + sauce)
  
  # Dice Roll
  if msg.startswith('$diceroll'):
    dice = roll_dice()
    await message.channel.send("You rolled a: " + dice)

keep_alive()
client.run(os.getenv('TOKEN'))