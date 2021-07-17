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

def get_quote(): # Gets inspirational quotes from website listed
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

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

keep_alive()
client.run(os.getenv('TOKEN'))