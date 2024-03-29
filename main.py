import discord
import os
#import music
from replit import db
from keepAlive import keep_alive # Imports line 13 from keep_alive file

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

# Friend Codes Feature
import friendCodes

# Slur Detection
from curseGen import get_curse
blacklist = get_curse() # Imports the banned word list
from checkCurse import check_curse
disabled_chs = []
""""
# Tic Tac Toe Game
from ticTactoe import play_tic, game_options
"""
# Music Player 
from music import musicplayer
m = musicplayer()

@client.event
async def on_ready(): # Let's us know that the bot is online
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  msg = message.content

  # Help Command (MAKE SURE TO ADD COMMAND TO HELP WHENEVER ADDING SOMETHING NEW)
  if msg.startswith('$help'):
    embed = discord.Embed(
      title = "Command List",
      description = "I will be updated with more features in the near future! Thank you for the support <3"
      +"\n**$help** - List of commands from me!"
      +"\n**$hey** - Hello!"
      +"\n**$inspire** - Provides an inspirational quote to brighten your day <3"
      +"\n**$sauce** - Must be 18+ to use this command or otherwise be punished by my owner!😠"
      +"\n**$diceroll** - Roll a six sided die."
      +"\n**$joke** - Ever heard of lame jokes? Here's some!"
      +"\n**$flirt** - Feeling lonely? Here's some pickup lines for you!😉"
      +"\n**$tictac** - Play Tic Tac Toe with me!"
      +"\n**$setfc** - Set your Nintendo Switch Friendcode in the exact format as: SW-xxxx-xxxx-xxxx"
      +"\n**$setpogo** - Set your Pokemon Go friend code."
      +"\n**$setgenshin** - Set your Genshin Impact friend code."
      +"\n**$fc** - Pull up all your friend codes, likewise @someone after to pull up theirs."
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
  
#-------------------------------------------------------------------------------------------------------------------
  """# Music: Disconnect
  if msg.startswith("$disconnect"):
    await m.disconnect(message)

  # Music: Play
  if msg.startswith("$play"):
    await m.join(message)
    await m.play(message)

  # Music: Pause
  if msg.startswith("$pause"):
    await m.pause(message)

  # Music: Resume
  if msg.startswith("$resume"):
    await m.resume(message)"""

#-------------------------------------------------------------------------------------------------------------------
  # Friend Codes (Nintendo Switch by Default)
  if msg.startswith("$setfc"):
    await friendCodes.set_code(message)
  if msg.startswith("$fc"):
    await friendCodes.get_code(message)

  # Pokemon Go FCs
  if msg.startswith("$setpogo"):
    await friendCodes.set_code(message, type="Pokemon Go")

  # Genshin FCs
  if msg.startswith("$setgenshin"): 
    await friendCodes.set_code(message, type="Genshin Impact")

#-------------------------------------------------------------------------------------------------------------------
  # Slur Detection
  
  if msg.startswith("$slur disable"):
    if (str(message.channel.id) not in db.keys()) & message.author.top_role.permissions.administrator : 
      db[str(message.channel.id)] = message.channel.id
      await message.delete()
      await message.channel.send("Success, Slur detection disabled.")
    else:
      await message.channel.send("Error. Slur Detection already disabled.")

  if msg.startswith("$slur enable"):
    if (str(message.channel.id) in db.keys()) & message.author.top_role.permissions.administrator :
      del db[str(message.channel.id)]
      await message.delete()
      await message.channel.send("Success, Slur detection enabled.")
    else:
      await message.channel.send("Error. Slur Detection already enabled.")


  line = msg.lower().split(' ')
  if str(message.channel.id) not in db.keys():
    if check_curse(blacklist, line):
      await message.delete()
      await message.channel.send("That word is not permitted here, {}!".format(message.author.mention))

#-------------------------------------------------------------------------------------------------------------------
  # Tic Tac Toe Game
  #if msg.startswith('$tictac'):
  #  await play_tic(message, client)
  

keep_alive()
client.run(os.getenv('TOKEN'))
