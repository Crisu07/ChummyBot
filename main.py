import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$favorite"):
    starters = ["Bulbasaur", "Squirtle", "Charmander"]
    favorite = random.choice(starters)
    await message.channel.send("I kinda like {}...".format(favorite))

  if msg.startswith('$hey'):
    await message.channel.send("Hey, {}! You come here often?".format(message.author.mention))

keep_alive()
client.run(os.getenv('TOKEN'))