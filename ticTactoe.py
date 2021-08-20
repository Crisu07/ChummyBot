import discord
import random 


async def play_tic(msg, client):
  blank = '⬜'
  emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🛑']
  board = [blank, blank, blank,
           blank, blank, blank,
           blank, blank, blank,]
  await msg.channel.purge(limit=1)
  player = await get_char(msg, client)
  await print_board(msg, board)

  
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

async def print_board(msg,board):
  line  = ''
  for i in range(len(board)):
    if (i + 1) % 3 == 0:
      line += board[i] + '\n'
    else:
      line += board[i]
  embed = discord.Embed(
    title = line,
    color = 0xFABFB2
  )
  await msg.channel.send(embed = embed)
