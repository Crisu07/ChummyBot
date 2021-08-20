import discord
import random 



async def play_tic(msg, client):
  await msg.channel.purge(limit=1)
  player = await get_char(msg, client)
  #await msg.channel.purge(limit=1)
  

async def get_char(msg, client):
  embed = discord.Embed(
    title = 'Choose your charcter for Tic Tac Toe!',
    decription = '❎ or 🅾️',
    color = 0xFABFB2
  )
  mes = await msg.channel.send(embed = embed)
  await mes.add_reaction('❎')
  await mes.add_reaction('🅾️')

  def check_reaction( reaction, user):
    return user != client.user
    
  reaction, user = await client.wait_for("reaction_add", timeout = 30.0, check = check_reaction)
  return str(reaction.emoji)
