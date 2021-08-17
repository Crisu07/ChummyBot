import discord
import os
from replit import db
from keep_alive import keep_alive # Imports line 13 from keep_alive file

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True


# Inspirational Quote Feature
from inspirationalQuotes import get_quote

# Doujin Generator Feature
from doujinDigits import sauce_gen

# Dice Roll
from diceRoll import roll_dice

#Dad Jokes Feature
from dadJokes import get_joke

# Pick Up Lines
from pickupLine import flirt

# Slur Detection
from antiSlur import slur

@client.event
async def on_ready(): # Let's us know that the bot is online
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  # Help Command
  if msg.startswith('$help'):
    embed = discord.Embed(
      title = "Command List",
      description = "$help - List of commands from me!" +
      "\n$hey - Hello!" +
      "\n$inspire - Provides an inspirational quote to brighten your day <3" +
      "\n$sauce - Must be 18+ to use this command or otherwise be punished by my owner >:3"
      ,
      color = 0xFABFB2
    )
    await message.channel.send(embed=embed)


  # Inspirational Quote
  if msg.startswith('$inspire'):
    quote = get_quote() # Retrieves a random inspirational quote 
    await message.channel.send(quote) # Send it to channel that command was given

  # Greets the User
  if msg.startswith('$hey'):
    await message.add_reaction('😊')
    await message.channel.send("Hey, {}! You come here often?".format(message.author.mention))

  # Sauce Finder
  if msg.startswith('$sauce'):
    sauce = sauce_gen()
    await message.channel.send("What up boss! Here's yo sauce: " + sauce)
  
  # Dice Roll
  if msg.startswith('$diceroll'):
    dice = roll_dice()
    await message.channel.send("You rolled a " + dice)

  # Dad joke
  if msg.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

  # Pick Up Lines 
  if msg.startswith('$flirt'):
    pline = flirt()
    await message.channel.send(pline)

  # Slur Detection
  blacklist = slur()
  if any(word in msg for word in blacklist):
    await message.delete()
    await message.channel.send("That word is not permitted here, {}!".format(message.author.mention))

keep_alive()
client.run(os.getenv('TOKEN'))